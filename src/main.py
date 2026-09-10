from pathlib import Path
from api_client import (get_city_list, get_weather_forecast,)
from formatter import (print_city_list,
                       get_chosen_city_data,
                       validate_weather_data,
                       format_weather_summary,)
from storage import (initialize_database, save_city, get_saved_cities,)


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
DATABASE_PATH = DATA_DIR / "weather_api.db"


def main() -> None:
    initialize_database(DATABASE_PATH)

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
        print(format_weather_summary(response_json))
    else:
        if type(response_json) == str:
            print(response_json)
        print("Could not complete task.")

    if input("Do you wish to register the city? [y/n]: ").strip() == 'y':
        save_city(chosen_city, DATABASE_PATH)


if __name__ == '__main__':
    main()
