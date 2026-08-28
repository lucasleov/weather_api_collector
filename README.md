# Weather API Collector



A simple CLI application for searching cities using the Open-Meteo Geocoding API and retrieving weather forecasts using the Open-Meteo Forecast API.



Work in progress.



## Goal



This project was created with the goal to practice use of APIs, requests, json and data processing, as well as consolidate error handling, code modularization, data persistence and unit testing.



## Utilized APIs



Open-Meteo Geocoding API

→ searches for cities and provides their locations



Open-Meteo Forecast API

→ provides weather forecasts



## Current Features



→ Searches for a city

→ Lists possible locations

→ Selecting a city

→ Searches the forecast

→ Possibility to choose the amount of days for the forecast

→ Shows temperature and apparent temperature

→ Shows precipitation

→ Shows wind speed

→ Basic error handling



## Planned Features



→ Input validation

→ No results handling

→ Geocoding error handling

→ Persistence of already consulted cities

→ Unit testing

→ CLI menu and improvements



## Project Structure



weather_api_collector/

├── data/

├── src/

│   ├── api_client.py

│   ├── formatter.py

│   ├── main.py

│   └── storage.py

├── tests/

├── README.md

└── requirements.txt



Where:



api_client.py → communication with the APIs

formatter.py → data formatting

main.py → Application flow

storage.py → data persistence



## Status



Work in progress — initial API integration and modular structure completed.