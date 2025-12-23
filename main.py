from fastapi import FastAPI, APIRouter
from enum import Enum
from services.services import filter_city, max_value, min_value, avg_value

# Task 4: Expose results via REST API using FastAPI
app = FastAPI()
router = APIRouter()

class City(str, Enum):
    san_franciso = "San Francisco",
    new_york = "New York",
    london = "London"

# Temperature
@router.get("/max_temperature", tags=["Temperature"])
async def max_temperature(city: City):
    filter_df = filter_city(city)
    max_value_ = max_value(filter_df, 'temperature_c')
    return f"The max temperature in {city} is {max_value_}"

@router.get("/min_temperature", tags=["Temperature"])
async def min_temperature(city: City):
    filter_df = filter_city(city)
    min_value_ = min_value(filter_df, 'temperature_c')
    return f"The min temperature in {city} is {min_value_}"

@router.get("/avg_temperature", tags=["Temperature"])
async def avg_temperature(city: City):
    filter_df = filter_city(city)
    avg_value_ = avg_value(filter_df, 'temperature_c')
    return f"The avg temperature in {city} is {avg_value_}"

# Humidity
@router.get("/max_humidity", tags=["Humidity"])
async def max_humidity(city: City):
    filter_df = filter_city(city)
    max_value_ = max_value(filter_df, 'humidity')
    return f"The max humidity in {city} is {max_value_}"

@router.get("/min_humidity", tags=["Humidity"])
async def min_humidity(city: str):
    filter_df = filter_city(city)
    min_value_ = min_value(filter_df, 'humidity')
    return f"The min humidity in {city} is {min_value_}"

@router.get("/avg_humidity", tags=["Humidity"])
async def avg_humidity(city: City):
    filter_df = filter_city(city)
    avg_value_ = avg_value(filter_df, 'humidity')
    return f"The avg humidity in {city} is {avg_value_}"

# Pollution - PM10
@router.get("/max_pollution_pm10", tags=["Pollution PM10"])
async def max_pollution(city: City):
    filter_df = filter_city(city)
    max_value_ = max_value(filter_df, 'pm10')
    return f"The max pollution (pm10) in {city} is {max_value_}"

@router.get("/min_pollution_pm10", tags=["Pollution PM10"])
async def min_pollution(city: City):
    filter_df = filter_city(city)
    min_value_ = min_value(filter_df, 'pm10')
    return f"The min pollution (pm10) in {city} is {min_value_}"

@router.get("/avg_pollution_pm10", tags=["Pollution PM10"])
async def avg_pollution(city: City):
    filter_df = filter_city(city)
    avg_value_ = avg_value(filter_df, 'pm10')
    return f"The avg pollution (pm10) in {city} is {avg_value_}"

# Pollution - PM2.5
@router.get("/max_pollution_pm2.5", tags=["Pollution PM2.5"])
async def max_pollution(city: City):
    filter_df = filter_city(city)
    max_value_ = max_value(filter_df, 'pm2.5')
    return f"The max pollution (pm2.5) in {city} is {max_value_}"

@router.get("/min_pollution_pm2.5", tags=["Pollution PM2.5"])
async def min_pollution(city: City):
    filter_df = filter_city(city)
    min_value_ = min_value(filter_df, 'pm2.5')
    return f"The min pollution (pm2.5) in {city} is {min_value_}"

@router.get("/avg_pollution_pm2.5", tags=["Pollution PM2.5"])
async def avg_pollution(city: City):
    filter_df = filter_city(city)
    avg_value_ = avg_value(filter_df, 'pm2.5')
    return f"The min pollution (pm2.5) in {city} is {avg_value_}"

# Pollen
@router.get("/max_pollen", tags=["Pollen"])
async def max_pollen(city: City):
    filter_df = filter_city(city)
    max_value_ = max_value(filter_df, 'pollen_concentration')
    return f"The max pollen concentration in {city} is {max_value_}"

@router.get("/min_pollen", tags=["Pollen"])
async def min_pollen(city: City):
    filter_df = filter_city(city)
    min_value_ = min_value(filter_df, 'pollen_concentration')
    return f"The min pollen concentration in {city} is {min_value_}"

@router.get("/avg_pollen", tags=["Pollen"])
async def avg_pollen(city: City):
    filter_df = filter_city(city)
    avg_value_ = avg_value(filter_df, 'pollen_concentration')
    return f"The min pollen concentration in {city} is {avg_value_}"

app.include_router(router)