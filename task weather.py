import requests, json
import psutil
mem = psutil.virtual_memory()
print(mem)

if mem.percent > 20:
    print("Hoiatusteate täituvus % peab olema seadistatav")

apikey = "6a510111b84cff5b8c802e815f020781" #these are the encryption keys for authenticating the user in the system
base_url = "http://api.openweathermap.org/data/2.5/weather?" #this is a variable that is pre-defined in the CI framework

city = "Tallinn"
answer_url = base_url + "appid=" + apikey + city
response = requests.get(answer_url)

x = response.json()
temp_kelvin = ["x"]
temp_celsius = temp_kelvin - 273.15

print(x)

work = open("task.txt")   




