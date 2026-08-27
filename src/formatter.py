

def print_city_list(city_list: list):
    for index, city in enumerate(city_list):
        print(f"""{index+1}:
Name: {city['name']}
Country: {city['country_code']}, {city['country']}
Timezone: {city['timezone']}
Latitude: {city['latitude']}
Longitude: {city['longitude']}
            """)


def print_forecast(response_json: dict):
    useful_data = response_json['daily']
    unit_list = response_json['daily_units']

    for index, date in enumerate(useful_data['time']):
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
