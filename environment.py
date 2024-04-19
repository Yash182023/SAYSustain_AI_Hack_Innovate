# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta
# import random

# # Function to generate random timestamps
# def random_timestamps(start, end, n):
#     delta = end - start
#     return [start + timedelta(seconds=random.randint(0, delta.total_seconds())) for _ in range(n)]

# # Generate random timestamps for the next 30 days
# start_date = datetime.now()
# end_date = start_date + timedelta(days=30)
# timestamps = random_timestamps(start_date, end_date, 10)

# # Real location coordinates (latitude, longitude)
# locations = [
#     (40.7128, -74.0060),  # New York City
#     (34.0522, -118.2437), # Los Angeles
#     (51.5074, -0.1278),   # London
#     (48.8566, 2.3522),    # Paris
#     (35.6895, 139.6917),  # Tokyo
#     (37.7749, -122.4194), # San Francisco
#     (55.7558, 37.6173),   # Moscow
#     (19.0760, 72.8777),   # Mumbai
#     (-33.8688, 151.2093),# Sydney
#     (-22.9068, -43.1729)  # Rio de Janeiro
# ]

# # Generate synthetic environmental data
# data = []
# for location, timestamp in zip(locations, timestamps):
#     latitude, longitude = location
#     altitude = random.randint(0, 100)
#     temperature = round(np.random.uniform(15, 30), 1)
#     humidity = random.randint(40, 80)
#     precipitation = round(np.random.uniform(0, 5), 2)
#     wind_speed = round(np.random.uniform(1, 10), 1)
#     wind_direction = random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
#     solar_radiation = random.randint(50, 300)
#     pm25 = random.randint(5, 25)
#     pm10 = random.randint(10, 50)
#     no2 = random.randint(5, 20)
#     so2 = random.randint(2, 10)
#     co = random.randint(1, 5)
#     o3 = random.randint(20, 50)
#     aqi = max(pm25, pm10, no2, so2, co, o3)
#     water_ph = round(np.random.uniform(6.5, 8.5), 1)
#     do = round(np.random.uniform(5, 10), 1)
#     turbidity = round(np.random.uniform(1, 20), 1)
#     nitrate = random.randint(5, 20)
#     phosphate = round(np.random.uniform(0.1, 1), 1)
#     soil_ph = round(np.random.uniform(5.5, 7.5), 1)
#     organic_matter = round(np.random.uniform(1, 5), 1)
#     nitrogen = round(np.random.uniform(0.3, 1), 1)
#     phosphorus = round(np.random.uniform(0.1, 0.5), 1)
#     potassium = round(np.random.uniform(0.2, 1), 1)
#     vegetation_cover = random.randint(30, 80)
#     land_use = random.choice(['Urban', 'Grassland', 'Industrial', 'Forest', 'Wetland', 'Shrubland'])
#     green_space = random.randint(10, 50)
#     biodiversity_index = round(np.random.uniform(0.5, 0.9), 2)
#     species_abundance = random.randint(50, 100)
#     habitat_characteristics = random.choice(['Polluted', 'Clean', 'Natural', 'Degraded'])
#     data.append([latitude, longitude, altitude, temperature, humidity, precipitation, wind_speed,
#                  wind_direction, solar_radiation, pm25, pm10, no2, so2, co, o3, aqi, water_ph, do,
#                  turbidity, nitrate, phosphate, soil_ph, organic_matter, nitrogen, phosphorus,
#                  potassium, vegetation_cover, land_use, green_space, biodiversity_index,
#                  species_abundance, habitat_characteristics, timestamp])

# # Create a DataFrame
# columns = ['Latitude', 'Longitude', 'Altitude', 'Temperature(C)', 'Humidity(%)', 'Precipitation(mm)',
#            'Wind_Speed(m/s)', 'Wind_Direction', 'Solar_Radiation(W/m^2)', 'PM2.5(µg/m^3)', 'PM10(µg/m^3)',
#            'NO2(µg/m^3)', 'SO2(µg/m^3)', 'CO(µg/m^3)', 'O3(µg/m^3)', 'AQI', 'Water_pH', 'DO(mg/L)',
#            'Turbidity(NTU)', 'Nitrate(µg/L)', 'Phosphate(µg/L)', 'Soil_pH', 'Organic_Matter(%)',
#            'Nitrogen(%)', 'Phosphorus(%)', 'Potassium(%)', 'Vegetation_Cover(%)', 'Land_Use',
#            'Green_Space(%)', 'Biodiversity_Index', 'Species_Abundance', 'Habitat_Characteristics', 'Time_Stamp']

# df = pd.DataFrame(data, columns=columns)

# # Save DataFrame to CSV file
# df.to_csv('environmental_data.csv', index=False)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Function to generate random timestamps
def random_timestamps(start, end, n):
    delta = end - start
    return [start + timedelta(seconds=random.randint(0, delta.total_seconds())) for _ in range(n)]

# Generate random timestamps for the next 30 days
start_date = datetime.now()
end_date = start_date + timedelta(days=30)
timestamps = random_timestamps(start_date, end_date, 10)

# Real location coordinates (latitude, longitude) with location names
locations = [
    ('New York City', 40.7128, -74.0060),
    ('Los Angeles', 34.0522, -118.2437),
    ('London', 51.5074, -0.1278),
    ('Paris', 48.8566, 2.3522),
    ('Tokyo', 35.6895, 139.6917),
    ('San Francisco', 37.7749, -122.4194),
    ('Moscow', 55.7558, 37.6173),
    ('Mumbai', 19.0760, 72.8777),
    ('Sydney', -33.8688, 151.2093),
    ('Rio de Janeiro', -22.9068, -43.1729)
]

# Generate synthetic environmental data
data = []
for location, timestamp in zip(locations, timestamps):
    location_name, latitude, longitude = location
    altitude = random.randint(0, 100)
    temperature = round(np.random.uniform(15, 30), 1)
    humidity = random.randint(40, 80)
    precipitation = round(np.random.uniform(0, 5), 2)
    wind_speed = round(np.random.uniform(1, 10), 1)
    wind_direction = random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    solar_radiation = random.randint(50, 300)
    pm25 = random.randint(5, 25)
    pm10 = random.randint(10, 50)
    no2 = random.randint(5, 20)
    so2 = random.randint(2, 10)
    co = random.randint(1, 5)
    o3 = random.randint(20, 50)
    aqi = max(pm25, pm10, no2, so2, co, o3)
    water_ph = round(np.random.uniform(6.5, 8.5), 1)
    do = round(np.random.uniform(5, 10), 1)
    turbidity = round(np.random.uniform(1, 20), 1)
    nitrate = random.randint(5, 20)
    phosphate = round(np.random.uniform(0.1, 1), 1)
    soil_ph = round(np.random.uniform(5.5, 7.5), 1)
    organic_matter = round(np.random.uniform(1, 5), 1)
    nitrogen = round(np.random.uniform(0.3, 1), 1)
    phosphorus = round(np.random.uniform(0.1, 0.5), 1)
    potassium = round(np.random.uniform(0.2, 1), 1)
    vegetation_cover = random.randint(30, 80)
    land_use = random.choice(['Urban', 'Grassland', 'Industrial', 'Forest', 'Wetland', 'Shrubland'])
    green_space = random.randint(10, 50)
    biodiversity_index = round(np.random.uniform(0.5, 0.9), 2)
    species_abundance = random.randint(50, 100)
    habitat_characteristics = random.choice(['Polluted', 'Clean', 'Natural', 'Degraded'])
    data.append([location_name, latitude, longitude, altitude, temperature, humidity, precipitation, wind_speed,
                 wind_direction, solar_radiation, pm25, pm10, no2, so2, co, o3, aqi, water_ph, do,
                 turbidity, nitrate, phosphate, soil_ph, organic_matter, nitrogen, phosphorus,
                 potassium, vegetation_cover, land_use, green_space, biodiversity_index,
                 species_abundance, habitat_characteristics, timestamp])

# Create a DataFrame
columns = ['Location', 'Latitude', 'Longitude', 'Altitude', 'Temperature(C)', 'Humidity(%)', 'Precipitation(mm)',
           'Wind_Speed(m/s)', 'Wind_Direction', 'Solar_Radiation(W/m^2)', 'PM2.5(µg/m^3)', 'PM10(µg/m^3)',
           'NO2(µg/m^3)', 'SO2(µg/m^3)', 'CO(µg/m^3)', 'O3(µg/m^3)', 'AQI', 'Water_pH', 'DO(mg/L)',
           'Turbidity(NTU)', 'Nitrate(µg/L)', 'Phosphate(µg/L)', 'Soil_pH', 'Organic_Matter(%)',
           'Nitrogen(%)', 'Phosphorus(%)', 'Potassium(%)', 'Vegetation_Cover(%)', 'Land_Use',
           'Green_Space(%)', 'Biodiversity_Index', 'Species_Abundance', 'Habitat_Characteristics', 'Time_Stamp']

df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV file
df.to_csv('environmental_data_new.csv', index=False)
