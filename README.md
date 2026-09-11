# Weather API Collector



A simple CLI application for searching cities using the Open-Meteo Geocoding API and retrieving weather forecasts using the Open-Meteo Forecast API.



Work in progress.



## Goal



This project was created with the goal to practice use of APIs, requests, JSON and data processing, as well as consolidate error handling, code modularization, data persistence and unit testing.



## Utilized APIs



Open-Meteo Geocoding API

→ searches for cities and provides their locations



Open-Meteo Forecast API

→ provides weather forecasts



## Current Features



→ Searches for cities using Geocoding API

→ Lists possible locations

→ Handles searches with no results

→ Retrieves weather forecast for chosen location

→ User-defined forecast window

→ Shows temperature and apparent temperature

→ Shows precipitation

→ Shows wind speed and direction

→ API error handling

→ Weather API response validation

→ Invalid/incomplete API response handling

→ SQLite persistence for saved cities

→ Duplicate city protection

→ Weather summary formatting

→ Automated tests with temporary SQLite database



## Planned Features



→ Input validation

→ CLI menu and improvements

→ Use saved cities for new forecasts

→ Final refactoring and documentation



## Project Structure



weather\_api\_collector/

├── data/

├── src/

│   ├── api\_client.py

│   ├── formatter.py

│   ├── main.py

│   └── storage.py

├── tests/

│   └── test_api.py

├── README.md

└── requirements.txt



Where:



api\_client.py → communication with the APIs

formatter.py → data formatting

main.py → application flow

storage.py → data persistence

test_api.py -> automated tests


## Example



```text
Inform the name of the city: Villeurbanne


1:
Name: Villeurbanne
Country: FR, France
Timezone: Europe/Paris
Latitude: 45.76601
Longitude: 4.8795

Choose the city: 1

Inform the number of days for the forecast: 1


Forecast for the day: 2026-09-04

Max Temperature: 34.4 °C
Min Temperature: 18.5 °C
Max Apparent Temperature: 34.2 °C
Min Apparent Temperature: 19.2 °C
Precipitation: 0.0 mm
Wind Speed: 5.6 km/h
Wind Direction: 56 °
```



## Tests



Run:

```bash
python -m pytest -v
```



9 automated tests currently passing.



Current automated tests cover:



- weather request parameter construction;

- weather response parsing;

- weather data label formatting;

- weather response validation;

- missing and inconsistent weather data;

- weather summary formatting;

- SQLite city persistence;

- duplicate city protection.



## Limitations



- saved cities are stored but cannot yet be selected from the CLI;

- user inputs still have limited validation;

- API errors are handled, but the error/result contract can still be improved;

- the application is CLI-only;

- forecasts are not cached or stored.



## Status



Work in progress — API integration, response validation, SQLite persistence and automated testing implemented.

