import requests as rq
import json as js
from time import sleep as sp
check = 0
try:
  print("Loading...")
  response = rq.get("https://api.openweathermap.org/data/2.5/weather?q={NAME_OF_THE_AREA}&appid={API_KEY}")
  location = input('Enter location:')
  sp(.2)
  if location == '!location':
    User_location = rq.get("https://ipinfo.io/json")
    User_location = User_location.json()
    with open("user_location.json","w") as f:
      js.dump(User_location,f)
    #Accessing lat n long
    lat_lon_arr = User_location['loc'].split(",")
    lat = lat_lon_arr[0]
    lon = lat_lon_arr[1]
    #Network request for users location
    response = rq.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    check = 1
  else:
    #Network Request
    response = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}")
  if response.status_code == 200:
    print()
    data = response.json()
    with open("weather_data.json","w") as f:
      js.dump(data,f)
  elif response.status_code == 404:
    print()
    print("404 cannot reach API 🥵🥵")
  else:
    print()
    print('Unable to reach URL 😔😔')
except (rq.ConnectionError,rq.ConnectTimeout) as exception:
  print()
  print("No internet connection ❌. Make sure you a connected to the internet 💻.")
#Data output
Area_Name =  data['name']
Temp = ((data['main']['temp']) - 273)
Description = data['weather'][0]['description'] 
country = data['sys']['country']
print()
# check if user wants to get weather for his or her current location
if check == 1:
  U_statement = f'The weather 🌥 at your current location latitude {lat} and longitude {lon} in {country}  is {Description}. And the temperature is {Temp:0.2f} degree celsius.'
  print(U_statement)
else:
  G_statement = f'The weather 🌥 at {Area_Name} in {country} is {Description}. And the temperature is {Temp:0.2f} degree celsius.'
  print(G_statement)

  #END OF CODE
