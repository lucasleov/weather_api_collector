def print_city_list(city_list: list) -> None:
    for index, city in enumerate(city_list):
        print(f"""{index+1}:
Name: {city['name']}
Country: {city['country_code']}, {city['country']}
Timezone: {city['timezone']}
Latitude: {city['latitude']}
Longitude: {city['longitude']}
            """)


def print_forecast(response_json: dict) -> None:

    parsed_data = parse_weather_response(response_json)
    unit_list = response_json['daily_units']

    for day in parsed_data:
        print(f'\nForecast for the day: {day["time"]}\n')
        for data, value in day.items():
            if data != 'time':
                print (f"{get_data_name(data)}: {value} {unit_list[data]}")
    

def parse_weather_response(response_json: dict) -> list:
    useful_data = response_json['daily']

    return [
        {key : useful_data[key][index] for key in useful_data}
            for index in range(len(useful_data['time']))
        ]


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

if __name__ == '__main__':
    sample = {
        'daily' : {
            'time': ['2026-09-01', '2026-09-02'],
            'temperature_2m_max': [29.2, 28.3],
            'temperature_2m_min': [19.2, 18.3]},
        'daily_units' : {
            'temperature_2m_max' : 'ºC',
            'temperature_2m_min' : 'ºC'}
        }

    print_forecast(sample)
            
