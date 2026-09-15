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
        while True:
            main_menu()

            choice = input("Select an option: ").strip()

            try:
                choice = int(choice)

                match choice:

                    case 1:
                        city_name = input('\nInform the name of the city: ')
                        city_list = get_city_list(city_name)

                        if type(city_list) == list:
                            chosen_city = forecast_flow(city_list)
                            if chosen_city is None:
                                continue
                            if input("Do you wish to register the city? [y/n]: ").strip() == 'y':
                                save_city(chosen_city, DATABASE_PATH)
                            break
                        elif city_list:
                            print(city_list)
                            input("\nPress Enter to go back to menu")
                        else:
                            print(f'No results have been found for "{city_name}".\n')
                            input("\nPress Enter to go back to menu")

                    case 2:
                        city_list = get_saved_cities(DATABASE_PATH)

                        if city_list:
                            print("\nSaved cities:")
                            chosen_city = forecast_flow(city_list)
                            if chosen_city is None:
                                continue
                            break
                        else:
                            print("\nThere are no saved cities.")
                            input("\nPress Enter to go back to menu")

                    case 0:
                        print("Goodbye!")
                        exit()

                    case _:
                        print("\nPlease select a valid option!")
                        input("\nPress Enter to go back to menu")
                        
            except ValueError:
                print("\nYou must inform a number!")
                input("\nPress Enter to go back to menu")
        
        input("\nPress Enter to go back to menu")


def main_menu() -> None:
    print("""\n Weather API Collector

            1 - Search new city
            2 - Saved cities
            0 - Exit
        """)


def forecast_flow(city_list: list) -> dict | None:
    print_city_list(city_list)

    print("0 - Back\n")
    
    while True:
        city_index = input("Choose the city: ")

        try:
            city_index = int(city_index)
            if city_index in range(1, len(city_list)+1):
                city_index -= 1
                break
            elif city_index == 0:
                return None
            else:
                print("\nPlease select a valid option!")
        except ValueError:
            print("\nYou must inform a number!")
            
    
    chosen_city = get_chosen_city_data(city_list, city_index)

    while True:
        number_of_days = input("\nInform the number of days for the forecast (1 to 16, 0 to go back): ")

        try:
            number_of_days = int(number_of_days)
            if number_of_days in range(1, 17):
                break
            elif number_of_days == 0:
                return None
            else:
                print("\nPlease inform a valid number")
        except ValueError:
            print("\nYou must inform a number!")
    
    response_json = get_weather_forecast(chosen_city, number_of_days)

    if validate_weather_data(response_json):
        print(format_weather_summary(response_json))
    else:
        if type(response_json) == str:
            print(response_json)
        print("Could not complete task.")
    return chosen_city


if __name__ == '__main__':
    main()
