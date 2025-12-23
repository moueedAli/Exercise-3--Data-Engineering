from pymongo import MongoClient

import json

with open("data/weather_data.json", "r", encoding="utf-8") as weather_data:
    weather_docs = json.load(weather_data)

with open("data/weather_data_2.json", "r", encoding="utf-8") as weather_data2:
    pollution_and_pollen_docs = json.load(weather_data2)

# Legg til .env

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client["demoDB"]
collection_weather = db["weather_data"]
collection_pollution = db["pollution_and_pollen_data"]

collection_weather.insert_many(weather_docs)
collection_pollution.insert_many(pollution_and_pollen_docs)


