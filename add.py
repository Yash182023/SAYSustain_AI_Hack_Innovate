import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('energy_data_500_cities.csv')

# Function to assign consumption level based on energy consumption
def assign_consumption_level(energy_consumption):
    if energy_consumption > 1500:
        return "High_Consumption"
    elif energy_consumption < 1200:
        return "Low_Consumption"
    else:
        return "Medium_Consumption"

# Apply the function to create the Consumption_Level column
data['Consumption_Level'] = data['Energy_Consumption'].apply(assign_consumption_level)

# Save the updated DataFrame to CSV
data.to_csv('energy_data_500_cities_with_consumption_level.csv', index=False)