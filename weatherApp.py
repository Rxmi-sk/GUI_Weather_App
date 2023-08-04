import requests

def main():

    # Getting location information from user
    latitude = input('Enter latitude: ')
    longitude = input("Enter longitude: ")

    # Fetching weather data using user's latitude and longitude
    r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=GMT')
    status_code = r.status_code # Getting the API's status

    
    # Checking if the API is working
    if status_code == 200:
       data = r.json()  # Getting the API response as a JSON
       max_temps = data["daily"]["temperature_2m_max"]  # Getting max weekly temperature from the 'daily' section
       todays_max = max_temps[0]    # Getting today's max temperature
       min_temps = data["daily"]["temperature_2m_min"]  # Getting min weekly temperature from the 'daily' section
       todays_min = min_temps[0]    # Getting today's min temperature
     
       print(f'High: {todays_max}°C\nLow: {todays_min}°C') # printing the high and low temps for the day

    else:
        print('Failed to fetch metadata.') # prints if the API is not working


if __name__ == '__main__':
    main()
