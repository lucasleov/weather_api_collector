import requests


GEOCODE_URL = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_URL = 'https://api.open-meteo.com/v1/forecast'



def get_city_list(name: str) -> list:
    params = {'name' : name, 'language' : 'en', 'format' : 'json'}
    response = requests.get(GEOCODE_URL, params=params, timeout=5)
    response_json = response.json()

    return response_json['results']


def get_weather_forecast(chosen_city: dict, forecast_days: int) -> dict | None:
    params = build_weather_params(chosen_city, forecast_days)
    
    return fetch_weather(params)

def build_weather_params(chosen_city: dict, forecast_days: int) -> dict:
    latitude = chosen_city['latitude']
    longitude = chosen_city['longitude']
    timezone = chosen_city['timezone']

    return {
    'latitude' : latitude,
    'longitude' : longitude,
    'daily' : ['temperature_2m_max',
               'temperature_2m_min',
               'apparent_temperature_max',
               'apparent_temperature_min',
               'precipitation_sum',
               'wind_speed_10m_max',
               'wind_direction_10m_dominant'],
    'timezone' : timezone,
    'forecast_days' : forecast_days
    }

def fetch_weather(params: dict) -> dict | None:
    try:
        response = requests.get(WEATHER_URL, params=params, timeout=5)
    except requests.exceptions.ConnectionError:
        print("A Connection error occurred.")
        return None
    except requests.exceptions.Timeout:
        print("The server took too long.")
        return None
    print(f"\nStatus code: {response.status_code}")
        
    try :
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        print("An HTTP Error occurred.")
        return None
