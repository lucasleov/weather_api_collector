import pytest
from src import (api_client, formatter,)

def test_build_weather_params() -> None:
    sample_city_name = "Test City"
    sample_city_timezone = "Europe/Paris"
    sample_city_latitude = 10.5
    sample_city_longitude = -20.5
    sample_forecast_days = 3
    
    sample_city = {'name' : sample_city_name,
            'timezone' : sample_city_timezone,
            'latitude' : sample_city_latitude,
            'longitude' : sample_city_longitude}

    params = api_client.build_weather_params(sample_city, sample_forecast_days)

    assert params['latitude'] == sample_city_latitude
    assert params['longitude'] == sample_city_longitude
    assert params['timezone'] == sample_city_timezone
    assert params['forecast_days'] == sample_forecast_days
    assert params['daily'] == ['temperature_2m_max',
                               'temperature_2m_min',
                               'apparent_temperature_max',
                               'apparent_temperature_min',
                               'precipitation_sum',
                               'wind_speed_10m_max',
                               'wind_direction_10m_dominant']


def test_parse_weather_response() -> None:
    sample_days = ['day1', 'day2']
    sample_max_temperature = [27, 25]
    sample_min_temperature = [17, 15]
    
    sample_response_json = {'daily': {'time': sample_days,
                                      'temperature_2m_max' : sample_max_temperature,
                                      'temperature_2m_min' : sample_min_temperature}}

    parsed_sample_data = formatter.parse_weather_response(sample_response_json)

    assert type(parsed_sample_data) == list
    assert len(parsed_sample_data) == 2
    assert parsed_sample_data[0]['time'] == sample_days[0]
    assert parsed_sample_data[0]['temperature_2m_max'] == sample_max_temperature[0]
    assert parsed_sample_data[0]['temperature_2m_min'] == sample_min_temperature[0]
    assert parsed_sample_data[1]['time'] == sample_days[1]
    assert parsed_sample_data[1]['temperature_2m_max'] == sample_max_temperature[1]
    assert parsed_sample_data[1]['temperature_2m_min'] == sample_min_temperature[1]


def test_get_data_name() -> None:
    assert formatter.get_data_name('time') == 'Date'
    assert formatter.get_data_name('temperature_2m_max') == 'Max Temperature'
    assert formatter.get_data_name('temperature_2m_min') == 'Min Temperature'
    assert formatter.get_data_name('apparent_temperature_max') == 'Max Apparent Temperature'
    assert formatter.get_data_name('apparent_temperature_min') == 'Min Apparent Temperature'
    assert formatter.get_data_name('precipitation_sum') == 'Precipitation'
    assert formatter.get_data_name('wind_speed_10m_max') == 'Wind Speed'
    assert formatter.get_data_name('wind_direction_10m_dominant') == 'Wind Direction'
    assert formatter.get_data_name('non_existing_data_type') == 'non_existing_data_type'
