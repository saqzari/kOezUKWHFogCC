Sensor Rest API instructions:

1. Flask needs to be installed (pip install flask)
2. Set enviorment variables:
   a) '$env:FLASK_APP = "sensor_app.py"'
3. In http://127.0.0.1:5000/sensors, sensors will be viewable (by default latest one is only viewable)
4. To view other sensors:
   a) http://127.0.0.1:5000/sensors/<id>
   b) http://127.0.0.1:5000/sensors?before_date=<before date>&after_date=<after date>
NOTE: Using a GET curl command is also possible. Also when viewing multiple sensors, the averages of the metrics of the current displaying sensors will be displayed
5. To register new sensor, curl POST command:
   - e.g  """curl.exe -X POST http://127.0.0.1:5000/sensors  
            -H 'Content-Type: application/json' 
            -d '{\"id\": 123, \"country\": \"Spain\", \"city\": \"Madrid\", \"temperature (C)\": 24, \"wind-speed (km)\": 50, \"humidity (%)\": 42}'
    NOTE: Not including date will put in the current date/time as default
6. To update the fields of a current sensor including metrics, curl PUT command:
   - e.g """curl -X PUT http://127.0.0.1:5000/sensors/1 -H 'Content-Type: application/json' -d '{/"city/": /"Spain/"}"""
   NOTE: This above example changes the city of sensor with id 1 to Spain
7. To delete a sensor simply curl delete
   - "curl.exe -X DELETE http://127.0.0.1:5000/sensors/<id>"
8. To run tests:
- unit -> .\sensor_unit_test.py
- integration ->  python -m pytest .\sensor_integration_test.py



If I had more time:
1. Add more tests
2. Add more ways to query. For now, averages for the metrics are displayed along with sensors in the inputted date range
