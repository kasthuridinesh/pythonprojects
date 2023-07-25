# Api weather checking
# importing libraries
import requests

#  giving API keys and getting location input from user
user_api = "1eb4806d518f1d86d8d8006dcd462f47"
location = input("Enter the city name: ")
# opening url with user input location
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?"
complete_url = complete_api_link + "appid=" + user_api + "&q=" + location
api_link = requests.get(complete_url)
api_data = api_link.json()

if api_data["cod"] != "404":

    y = api_data["main"]

    # storing the value equal to "temp key of y
    current_tempetature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = api_data["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_tempetature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")
