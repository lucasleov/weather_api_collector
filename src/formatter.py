def print_city_list(city_list: list) -> None:
    for index, city in enumerate(city_list):
        print(f"""{index+1}:
Name: {city['name']}
Country: {city['country_code']}, {city['country']}
Timezone: {city['timezone']}
Latitude: {city['latitude']}
Longitude: {city['longitude']}
            """)


def format_weather_summary(response_json: dict) -> str:

    parsed_data = parse_weather_response(response_json)
    unit_list = response_json['daily_units']
    weather_summary = ""

    for day in parsed_data:
        weather_summary += f'\nForecast for the day: {day["time"]}\n'
        for data, value in day.items():
            if data != 'time':
                weather_summary += f"\n{get_data_name(data)}: {value} {unit_list[data]}"
        weather_summary += "\n"

    return weather_summary
    

def parse_weather_response(response_json: dict) -> list:
    useful_data = response_json['daily']

    return [
        {key : useful_data[key][index] for key in useful_data}
            for index in range(len(useful_data['time']))
        ]

def validate_weather_data(response: dict) -> bool:
    if not type(response) == dict:
        return False
    
    if not response.get('daily') or not response.get('daily_units'):
        return False
    
    mandatory_fields = ['time',
                        'temperature_2m_max',
                        'temperature_2m_min',
                        'apparent_temperature_max',
                        'apparent_temperature_min',
                        'precipitation_sum',
                        'wind_speed_10m_max',
                        'wind_direction_10m_dominant']
    
    for i in mandatory_fields:
        if not response['daily'].get(i) or not response['daily_units'].get(i):
            return False
        
    number_of_days = len(response['daily']['time'])
    
    if number_of_days == 0:
        return False
    
    for i in mandatory_fields:
        if not len(response['daily'][i]) == number_of_days:
            return False
        
    return True


def get_data_name(data_type: str) -> str:
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
    else:
        data_name = data_type
    return data_name


def get_chosen_city_data(city_list: list, chosen_index: int) -> dict:
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
            
