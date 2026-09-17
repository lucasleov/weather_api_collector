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
        main_menu()

        choice = get_valid_choice("Select an option: ", range(3))

        match choice:

            case 1:
                city_list = search_city_flow()

                if city_list:
                    chosen_city = forecast_flow(city_list)
                    if chosen_city is None:
                        continue
                    save_city_flow(chosen_city)
                else:
                    continue

            case 2:
                city_list = get_saved_cities(DATABASE_PATH)

                if city_list:
                    print("\nSaved cities:")
                    chosen_city = forecast_flow(city_list)
                    if chosen_city is None:
                        continue
                else:
                    print("\nThere are no saved cities.")

            case 0:
                print("\nGoodbye!")
                break

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

    city_index = get_valid_choice("Choose the city: ", range(len(city_list)+1))
    if city_index == 0:
        return None

    chosen_city = get_chosen_city_data(city_list, city_index-1)

    number_of_days = get_valid_choice("\nInform the number of days for the forecast (1 to 16, 0 to go back): ", range(17))
    if number_of_days == 0:
        return None
    
    response_json = get_weather_forecast(chosen_city, number_of_days)

    if validate_weather_data(response_json):
        print(format_weather_summary(response_json))
    else:
        if type(response_json) == str:
            print(response_json)
        print("Could not complete task.")
    return chosen_city


def save_city_flow(chosen_city: dict) -> None:
    while True:
        wants_to_save = input("Do you wish to save the city? [y/n]: ").strip().lower()
        if wants_to_save == 'y':
            save_city(chosen_city, DATABASE_PATH)
            break
        elif wants_to_save == 'n':
            break
        else:
            print('\nPlease answer with "y" for yes or "n" for no.\n')


def search_city_flow() -> list | None:
    city_name = input('\n0 - Back\nInform the name of the city: ').strip()
    if city_name == "0":
        return None
    
    city_list = get_city_list(city_name)
    
    if type(city_list) == list:
        return city_list
    
    elif city_list:
        print(city_list)
        
    else:
        print(f'No results have been found for "{city_name}".\n')
        
    input("\nPress Enter to go back to menu")
    return None


def get_valid_choice(message: str, choice_range: range) -> int:
    while True:
        chosen_option = input(message).strip()

        try:
            chosen_option = int(chosen_option)
            if chosen_option in choice_range:
                return chosen_option
            else:
                print("\nPlease inform a valid option!")
        except ValueError:
            print("\nYou must inform a number!")
        
    

if __name__ == '__main__':
    main()
