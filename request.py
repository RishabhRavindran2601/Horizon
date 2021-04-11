import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Year':2014, 'Runtime':121, 'Global_intensity':18.400, 'Sub_metering_1':0.000, 'Sub_metering_2':1.000,'Sub_metering_3':17.0})

print(r.json())



