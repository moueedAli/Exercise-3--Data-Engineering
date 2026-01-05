# Exercise 3 – Data Engineering (Weather + Pollution/Pollen)

## Overview
This project demonstrates a simple data engineering pipeline end-to-end: reading JSON files, persisting them to MongoDB, combining the datasets with pandas, and exposing basic aggregations through a FastAPI REST API.

## Repository structure

### `data/`
This folder contains the raw input datasets as JSON files:
`weather_data.json` contains weather observations (for example temperature, humidity, rain, wind) per city and date.
`weather_data_2.json` contains pollution and pollen observations (for example pm10, pm2.5, pollen concentration) per city and date.

These files are loaded at runtime and used both for database insertion and for building the in-memory analysis dataset.

### `services/`
This package contains the data and analysis logic used by the API layer. In practice, it is responsible for:
- Loading and parsing the JSON documents.
- Creating pandas DataFrames and merging them on the shared keys `city` and `date`.
- Providing helper functions used by the API, such as filtering by city and computing max, min, and average for a chosen attribute.

### `.env` and MongoDB connection
MongoDB credentials are read from environment variables using `python-dotenv`.
`DB_PASSWORD` is expected in `.env`, and is used to build the MongoDB Atlas connection string.

The application connects via `pymongo.MongoClient` to:
Database: `demoDB`
Collections: `weather_data` and `pollution_and_pollen_data`

On startup, the JSON documents are inserted into these collections. If you run the program multiple times without clearing the collections, you may create duplicates.

## API (`main.py`)
`main.py` defines a FastAPI application and exposes a set of GET endpoints that return simple aggregations (max, min, avg). The endpoints rely on the service-layer functions (for example `filter_city`, `max_value`, `min_value`, `avg_value`) applied to the merged dataset.

Cities are selected through a query parameter (an enum), intended to support:
San Francisco, New York, and London.

At a high level, the endpoints are grouped by topic:
Temperature: max/min/avg of `temperature_c`
Humidity: max/min/avg of `humidity`
Pollution PM10: max/min/avg of `pm10`
Pollution PM2.5: max/min/avg of `pm2.5`
Pollen: max/min/avg of `pollen_concentration`

Once running, you can query endpoints by providing a city parameter, for example:
`GET /max_temperature?city=San%20Francisco`
