from flask import Flask, request

app = Flask(__name__)

in_memory_datastore = {
   "1": {"id": "1", "date": 1960, "country": "Ireland", "city" : "Dublin"},
   "2": {"id": "2", "date": 1958, "country": "Germany", "city" : "Berlin"},
   "3": {"id": "3", "date": 1962, "country": "England", "city" : "London"},
}

@app.route('/sensors', methods=['GET', 'POST'])
def sensors_route():
   if request.method == 'GET':
       return list_sensors()
   elif request.method == "POST":
       return create_sensor(request.get_json(force=True))

def list_sensors():
   before_year = request.args.get('before_year') or '30000'
   after_year = request.args.get('after_year') or '0'
   qualifying_data = list(
       filter(
           lambda pl: int(before_year) > pl['date'] > int(after_year),
           in_memory_datastore.values()
       )
   )

   return {"sensors": qualifying_data}

def create_sensor(new_sens):
   sensor_name = new_sens['id']
   in_memory_datastore[sensor_name] = new_sens
   return new_sens

@app.route('/sensors/<sensor_name>', methods=['GET', 'PUT', 'DELETE'])
def sensor_route(sensor_name):
   if request.method == 'GET':
       return get_sensor(sensor_name)
   elif request.method == "PUT":
       return update_sensor(sensor_name, request.get_json(force=True))
   elif request.method == "DELETE":
       return delete_sensor(sensor_name)

def get_sensor(sensor_name):
   return in_memory_datastore[sensor_name]

def update_sensor(sens_name, new_sens_attributes):
   sens_getting_update = in_memory_datastore[sens_name]
   sens_getting_update.update(new_sens_attributes)
   return sens_getting_update

def delete_sensor(sens_name):
   deleting_sens = in_memory_datastore[sens_name]
   del in_memory_datastore[sens_name]
   return deleting_sens