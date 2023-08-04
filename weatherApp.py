import requests


def get_user_location(city):
    r = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json')
    data = r.json()
    location_info = data["results"][0]  # Get the first element from the "results" list
    latitude = location_info["latitude"]  # Access "latitude"
    longitude = location_info["longitude"]  # Access "longitude"
    return latitude, longitude


def main():

    # Getting location information from user
    city = input("What city do you live in?\n--> ")
    latitude, longitude = get_user_location(city)   # Converting city name to latitude and longitude
    
    # Fetching weather data using user's latitude and longitude
    r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=GMT')
    status_code = r.status_code # Getting the API's status
    
    # Checking if the API is working
    if status_code == 200:
       data = r.json()  # Getting the API response as a JSON
       max_temps = data["daily"]["temperature_2m_max"]  # Getting max weekly temperatures from the 'daily' section
       todays_max = max_temps[0]    # Getting today's max temperature
       min_temps = data["daily"]["temperature_2m_min"]  # Getting min weekly temperatures from the 'daily' section
       todays_min = min_temps[0]    # Getting today's min temperature
     
       print(f'High: {todays_max}°C\nLow: {todays_min}°C') # printing the high and low temps for the day

    else:
        print('Failed to fetch metadata.') # prints if the API is not working


if __name__ == '__main__':
    main()
