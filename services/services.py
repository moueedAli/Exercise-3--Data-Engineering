import os
import pandas as pd
import json

from pandas.core.interchange.dataframe_protocol import DataFrame
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("DB_PASSWORD")

# Task 1: Load data from .json files
with open("data/weather_data.json", "r", encoding="utf-8") as weather_data:
    weather_docs = json.load(weather_data)

with open("data/weather_data_2.json", "r", encoding="utf-8") as weather_data2:
    pollution_and_pollen_docs = json.load(weather_data2)

# Connect to MongoDB
mongo_uri = f"mongodb+srv://moueed2701_db_user:{password}@dataengineering.adtgztn.mongodb.net/?appName=DataEngineering"

client = MongoClient(mongo_uri)
db = client["demoDB"]
collection_weather = db["weather_data"]
collection_pollution = db["pollution_and_pollen_data"]

# Task 2: Store everything in MongoDB
collection_weather.insert_many(weather_docs)
collection_pollution.insert_many(pollution_and_pollen_docs)

# Task 3: Combine data by city and date, and perform analysis
df_weather = pd.DataFrame(weather_docs)
df_pollution = pd.DataFrame(pollution_and_pollen_docs)

# Combining the data on city and date attributes
merge_df = pd.merge(df_weather, df_pollution, on=['city', 'date'], how='inner')

# Analysis on the data
def filter_city(city: str):
    filtered_df = merge_df[merge_df['city'] == city]
    return filtered_df

def max_value(df: DataFrame, attribute: str):
    return df[attribute].max()

def min_value(df: DataFrame, attribute: str):
    return df[attribute].min()

def avg_value(df: DataFrame, attribute: str):
    return df[attribute].mean()
