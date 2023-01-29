from flask import Flask, request
from dateutil import parser
import datetime

app = Flask(__name__)

in_memory_datastore = {
   "1": {"id": "1", "date": datetime.datetime(2003, 5, 11), "country": "Ireland", "city" : "Dublin", "temperature (C)" : 8, "wind-speed (km)": 23, "humidity (%)": 30},
   "2": {"id": "2", "date": datetime.datetime(2019, 11, 17), "country": "Germany", "city" : "Berlin", "temperature (C)" : 11, "wind-speed (km)": 33, "humidity (%)": 12},
   "3": {"id": "3", "date": datetime.datetime(2022, 4, 8), "country": "England", "city" : "London", "temperature (C)" : 12, "wind-speed (km)": 35, "humidity (%)": 65},
}

@app.route('/sensors', methods=['GET', 'POST', 'QUERY'])
def sensors_route():
   if request.method == 'GET':
       return list_sensors()
   elif request.method == "POST":
       return create_sensor(request.get_json(force=True))
   elif request.method == 'QUERY':
       return query_sensors()

def list_sensors():
   before_date = request.args.get('before_date')
   after_date = request.args.get('after_date')

   if isinstance(before_date, str):
      before_date = parser.parse(before_date)
   if isinstance(after_date, str):
      after_date = parser.parse(after_date)

   if before_date == None or after_date == None:
      return {"sensor": list(in_memory_datastore.items())[len(in_memory_datastore) - 1]}

   qualifying_data = list(
       filter(
           lambda pl: before_date > pl['date'] > after_date,
           in_memory_datastore.values()
       )
   )

   return {"sensors": qualifying_data, 
          "avg temp.": average("temperature (C)", qualifying_data),
          "avg wind.": average("wind-speed (km)", qualifying_data),
          "avg humidity": average("humidity (%)", qualifying_data)}

def create_sensor(new_sens):
   sensor_name = new_sens['id']
   in_memory_datastore[sensor_name] = new_sens
   return new_sens

def query_sensors():
   return "hi"

def average(field, data):
   total = 0
   count = 0
   for i in data:
      if i.get(field) != None:
         total += i[field]
         count = count + 1
   return round(total/count, 2)

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