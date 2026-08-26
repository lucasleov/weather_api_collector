import requests


GEOCODE_URL = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_URL = 'https://api.open-meteo.com/v1/forecast'


def main() -> None:
    city_list = get_city_list(input('Digite o nome da cidade: '))
    print_city_list(city_list['results'])
    chosen_city = get_chosen_city_data(city_list['results'], int(input("Choose the city: "))-1)
    print(chosen_city)
    get_weather_forecast(chosen_city['latitude'],
                         chosen_city['longitude'],
                         chosen_city['timezone'],
                         7)


def get_city_list(name: str):
    params = {'name' : name, 'language' : 'en', 'format' : 'json'}
    response = requests.get(GEOCODE_URL, params=params, timeout=5)
    response_json = response.json()
    return response_json

def print_city_list(city_list: list):
    for index, city in enumerate(city_list):
        print(f"""{index+1}:
Name: {city['name']}
Country: {city['country_code']}, {city['country']}
Timezone: {city['timezone']}
Latitude: {city['latitude']}
Longitude: {city['longitude']}
            """)

def get_chosen_city_data(city_list: list, chosen_index: int):
    name = city_list[chosen_index]['name']
    country_code = city_list[chosen_index]['country_code']
    country = city_list[chosen_index]['country']
    timezone = city_list[chosen_index]['timezone']
    latitude = city_list[chosen_index]['latitude']
    longitude = city_list[chosen_index]['longitude']
    return {'name' : name,
            'country_code' : country_code,
            'country' : country,
            'timezone' : timezone,
            'latitude' : latitude,
            'longitude' : longitude}

def get_weather_forecast(latitude: float, longitude: float, timezone: str, forecast_days: int) -> None:
    params = {
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
    try:
        response = requests.get(WEATHER_URL, params=params, timeout=5)
    except requests.exceptions.ConnectionError:
        print("A Connection error occurred.")
        return
    except requests.exceptions.Timeout:
        print("The server took too long.")
        return
    print(f"\nStatus code: {response.status_code}")
        
    try :
        response.raise_for_status()
        response_json = response.json()
            
        useful_data = response_json['daily']
        unit_list = response_json['daily_units']

        for index, date in enumerate(useful_data['time']):
            print_forecast(useful_data, date, index, unit_list)
    except requests.exceptions.HTTPError:
        print("An HTTP Error occurred.")

def print_forecast(useful_data, date, index, unit_list):
    print(f"\nForecast for the day: {date}\n")
    for data in useful_data:
        if data != "time":
            print (f"{get_data_name(data)}: {useful_data[data][index]} {unit_list[data]}")

def get_data_name(data_type):
    if data_type == 'time':
        data_name = 'Date'
    elif data_type == 'temperature_2m_max':
        data_name = 'Max Temperature'
    elif data_type == 'temperature_2m_min':
        data_name = 'Min Temperature'
    elif data_type == 'apparent_temperature_max':
        data_name = 'Max Apparent Temperature'
    elif data_type == 'apparent_temperature_min':
        data_name = 'Min Apparent Temperature'
    elif data_type == 'precipitation_sum':
        data_name = 'Precipitation'
    elif data_type == 'wind_speed_10m_max':
        data_name = 'Wind Speed'
    elif data_type == 'wind_direction_10m_dominant':
        data_name = 'Wind Direction'
    return data_name

if __name__ == '__main__':
    main()
