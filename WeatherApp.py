import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key }"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        # The API call was successful
        data = response.json()
        
        # Now you can extract the parts of the data you need, for example:
        main_data = data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_description = data['weather'][0]['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Description: {weather_description}")
    else:
        # The API call failed
        print("Error in the HTTP request")

# Example usage
api_key = "ae2682c2de22df2f19dc4eb0a18481e5"
city_name = "Cedartown"
get_weather(city_name, api_key)




