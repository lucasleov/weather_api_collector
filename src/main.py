from api_client import (get_city_list, get_weather_forecast,)
from formatter import (print_city_list,
                       get_chosen_city_data,
                       validate_weather_data,
                       print_forecast,)


def main() -> None:

    while True:
        city_name = input('Inform the name of the city: ')
        city_list = get_city_list(city_name)

        if type(city_list) == list:
            print_city_list(city_list)
            break
        elif city_list:
            print(city_list)
            exit()
        else:
            print(f'No results have been found for "{city_name}".\n')
    
    city_index = int(input("Choose the city: "))-1
    
    chosen_city = get_chosen_city_data(city_list, city_index)
    
    number_of_days = int(input("\nInform the number of days for the forecast: "))
    
    response_json = get_weather_forecast(chosen_city, number_of_days)

    if validate_weather_data(response_json):
        print_forecast(response_json)
    else:
        if type(response_json) == str:
            print(response_json)
        print("Could not complete task.")


if __name__ == '__main__':
    main()
