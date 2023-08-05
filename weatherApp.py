import weather_codes
import requests
from tkinter import *

# root= Tk()
# root.title("Weather App")
# root.geometry("750x400")

# city_name= StringVar()
# city_input = Entry(root, textvariable=city_name)

# myLabel = Label(root, text="Hello World")
# myLabel.pack()
# root.mainloop()

def get_user_location(city):
    link=f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    r = requests.get(link)
    data = r.json()
    location_info = data["results"][0]  # Get the first element from the "results" list
    latitude = location_info["latitude"]  # Access "latitude"
    longitude = location_info["longitude"]  # Access "longitude"
    country = location_info["country"]  # Access "country"
    return latitude, longitude, country
    
def main():

    # Getting location information from user
    city = input("What city do you live in?\n--> ")
    latitude, longitude, country= get_user_location(city)   # Converting city name to latitude and longitude
    api_link=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=auto"
    # Fetching weather data using user's latitude and longitude
    r = requests.get(api_link)
    status_code = r.status_code # Getting the API's status
    
    # Checking if the API is working
    if status_code == 200:
       data = r.json()  # Getting the API response as a JSON
       print(city+", "+country)
       weatherCode = data["daily"]["weathercode"]  # Getting max weekly temperatures from the 'daily' section
       forecast = weatherCode[0]    # Getting today's max temperature
       max_temps = data["daily"]["temperature_2m_max"]  # Getting max weekly temperatures from the 'daily' section
       todays_max = max_temps[0]    # Getting today's max temperature
       min_temps = data["daily"]["temperature_2m_min"]  # Getting min weekly temperatures from the 'daily' section
       todays_min = min_temps[0]    # Getting today's min temperature
       city_sunrise = data["daily"]["sunrise"]
       sunrise = city_sunrise[0] 
       city_sunset = data["daily"]["sunset"]
       sunset = city_sunset[0] 

     
       print('Forecast: ' + str(weather_codes.decode(forecast))+ f'\nHigh: {todays_max}°C\nLow: {todays_min}°C\nSunrise: {sunrise[-5:]}\nSunset: {sunset[-5:]}') # printing the high and low temps for the day

    else:
        print('Failed to fetch metadata.') # prints if the API is not working


if __name__ == '__main__':
    main()
    
