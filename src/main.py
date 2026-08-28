from api_client import (get_city_list, get_weather_forecast,)
from formatter import (print_city_list,
                       get_chosen_city_data,
                       print_forecast,)


def main() -> None:
    
    city_list = get_city_list(input('Digite o nome da cidade: '))
    
    print_city_list(city_list)
    
    city_index = int(input("Choose the city: "))-1
    
    chosen_city = get_chosen_city_data(city_list, city_index)
    
    number_of_days = int(input("\nInform the number of days for the forecast: "))
    
    response_json = get_weather_forecast(chosen_city, number_of_days)

    if response_json:
        print_forecast(response_json)
    else:
        print("Could not complete task.")


if __name__ == '__main__':
    main()
