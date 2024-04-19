# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
#           'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Washington',
#           'Boston', 'El Paso', 'Detroit', 'Nashville', 'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore',
#           'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Mesa', 'Sacramento', 'Atlanta', 'Kansas City', 'Colorado Springs', 'Miami',
#           'Raleigh', 'Omaha', 'Long Beach', 'Virginia Beach', 'Oakland', 'Minneapolis', 'Tulsa', 'Arlington', 'New Orleans', 'Wichita',
#           'Cleveland', 'Tampa', 'Bakersfield', 'Aurora', 'Honolulu', 'Anaheim', 'Santa Ana', 'Riverside', 'Corpus Christi', 'Lexington',
#           'Stockton', 'St. Louis', 'Saint Paul', 'Henderson', 'Pittsburgh', 'Cincinnati', 'Anchorage', 'Greensboro', 'Plano', 'Newark',
#           'Lincoln', 'Orlando', 'Irvine', 'Toledo', 'Jersey City', 'Chula Vista', 'Durham', 'Fort Wayne', 'St. Petersburg', 'Laredo',
#           'Buffalo', 'Madison', 'Lubbock', 'Chandler', 'Scottsdale', 'Reno', 'Glendale', 'Gilbert', 'Winston–Salem', 'North Las Vegas',
#           'Norfolk', 'Chesapeake', 'Garland', 'Irving', 'Hialeah', 'Fremont', 'Boise', 'Richmond', 'Baton Rouge', 'Spokane', 'Des Moines']

# # Randomly select 100 cities from the list
# geographic_location = np.random.choice(cities, size=100)

# # Generate sample data for hundred rows
# timestamps = pd.date_range(start='2024-01-01', periods=100, freq='H')
# weather_temperature = np.random.randint(10, 30, size=100)
# weather_humidity = np.random.randint(40, 80, size=100)
# weather_precipitation = np.random.rand(100) * 5
# weather_wind_speed = np.random.randint(5, 20, size=100)
# weather_solar_radiation = np.random.randint(500, 500                                                                 , size=100)
# building_size = np.random.randint(5000, 500                                                                 0, size=100)
# building_age = np.random.randint(5, 20, size=100)
# building_construction = ['Concrete', 'Steel', 'Brick', 'Wood', 'Concrete']*20
# building_insulation = ['High', 'Medium', 'Low']*33 + ['High']
# building_usage_type = ['Office', 'Warehouse']*50
# occupancy_count = np.random.randint(50, 200, size=100)
# equipment_usage_hvac = np.random.randint(100, 300, size=100)
# equipment_usage_lighting = np.random.randint(200, 500, size=100)
# equipment_usage_machinery = np.random.randint(30, 100, size=100)
# operational_schedule = ['Mon-Fri 9am-5pm']*50 + ['Sat-Sun 9am-5pm']*50
# energy_consumption = np.random.randint(500                                                                 , 2000, size=100)
# electricity_price = np.random.uniform(0.1, 0.15, size=100)
# gas_price = np.random.uniform(0.05, 0.08, size=100)
# utility_tariff_type = ['Time-of-Use']*50 + ['Flat-Rate']*50

# # Create DataFrame
# data = pd.DataFrame({
#     'Timestamp': timestamps,
#     'Weather_Temperature': weather_temperature,
#     'Weather_Humidity': weather_humidity,
#     'Weather_Precipitation': weather_precipitation,
#     'Weather_Wind_Speed': weather_wind_speed,
#     'Weather_Solar_Radiation': weather_solar_radiation,
#     'Building_Size': building_size,
#     'Building_Age': building_age,
#     'Building_Construction': building_construction,
#     'Building_Insulation': building_insulation,
#     'Building_Usage_Type': building_usage_type,
#     'Occupancy_Count': occupancy_count,
#     'Equipment_Usage_HVAC': equipment_usage_hvac,
#     'Equipment_Usage_Lighting': equipment_usage_lighting,
#     'Equipment_Usage_Machinery': equipment_usage_machinery,
#     'Operational_Schedule': operational_schedule,
#     'Energy_Consumption': energy_consumption,
#     'Electricity_Price': electricity_price,
#     'Gas_Price': gas_price,
#     'Utility_Tariff_Type': utility_tariff_type,
#     'Geographic_Location': geographic_location
# })

# # Save DataFrame to CSV
# data.to_csv('energy_data_100_rows.csv', index=False)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
          'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Washington',
          'Boston', 'El Paso', 'Detroit', 'Nashville', 'Memphis', 'Portland', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore',
          'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Mesa', 'Sacramento', 'Atlanta', 'Kansas City', 'Colorado Springs', 'Miami',
          'Raleigh', 'Omaha', 'Long Beach', 'Virginia Beach', 'Oakland', 'Minneapolis', 'Tulsa', 'Arlington', 'New Orleans', 'Wichita',
          'Cleveland', 'Tampa', 'Bakersfield', 'Aurora', 'Honolulu', 'Anaheim', 'Santa Ana', 'Riverside', 'Corpus Christi', 'Lexington',
          'Stockton', 'St. Louis', 'Saint Paul', 'Henderson', 'Pittsburgh', 'Cincinnati', 'Anchorage', 'Greensboro', 'Plano', 'Newark',
          'Lincoln', 'Orlando', 'Irvine', 'Toledo', 'Jersey City', 'Chula Vista', 'Durham', 'Fort Wayne', 'St. Petersburg', 'Laredo',
          'Buffalo', 'Madison', 'Lubbock', 'Chandler', 'Scottsdale', 'Reno', 'Glendale', 'Gilbert', 'Winston–Salem', 'North Las Vegas',
          'Norfolk', 'Chesapeake', 'Garland', 'Irving', 'Hialeah', 'Fremont', 'Boise', 'Richmond', 'Baton Rouge', 'Spokane', 'Des Moines',
          'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur',
                'Lucknow', 'Kanpur', 'Nagpur', 'Visakhapatnam', 'Indore', 'Thane', 'Bhopal', 'Patna', 'Vadodara', 'Ghaziabad',
                'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Varanasi', 'Srinagar', 'Aurangabad', 'Dhanbad',
                'Amritsar', 'Navi Mumbai', 'Allahabad', 'Howrah', 'Ranchi', 'Gwalior', 'Jabalpur', 'Vijayawada', 'Jodhpur', 'Raipur',
                'Kota', 'Guwahati', 'Chandigarh', 'Thiruvananthapuram', 'Solapur', 'Tiruchirappalli', 'Bareilly', 'Moradabad', 'Mysore',
                'Tiruppur', 'Gurgaon', 'Aligarh', 'Jalandhar', 'Bhubaneswar', 'Salem', 'Warangal', 'Guntur', 'Bhiwandi', 'Saharanpur',
                'Gorakhpur', 'Bikaner', 'Amravati', 'Noida', 'Jamshedpur', 'Bhilai', 'Cuttack', 'Firozabad', 'Kochi', 'Nellore',
                'Bhavnagar', 'Dehradun', 'Durgapur', 'Asansol', 'Rourkela', 'Nanded', 'Kolhapur', 'Ajmer', 'Akola', 'Gulbarga', 'Jamnagar',
                'Ujjain', 'Loni', 'Siliguri', 'Jhansi', 'Ulhasnagar', 'Jammu', 'Sangli-Miraj & Kupwad', 'Mangalore', 'Erode', 'Belgaum',
                'Ambattur', 'Tirunelveli', 'Malegaon', 'Gaya', 'Jalgaon', 'Udaipur', 'Maheshtala', 'Davanagere', 'Kozhikode', 'Akbarpur',
                'Shanghai', 'Beijing', 'Tianjin', 'Guangzhou', 'Shenzhen', 'Wuhan', 'Dongguan', 'Chongqing', 'Chengdu', 'Nanjing',
                'Taiyuan', 'Xian', 'Hangzhou', 'Harbin', 'Suzhou', 'Shantou', 'Jinan', 'Shijiazhuang', 'Dalian', 'Zhengzhou',
                'Qingdao', 'Ningbo', 'Shenyang', 'Changsha', 'Nanning', 'Xiamen', 'Wenzhou', 'Changchun', 'Fuzhou', 'Guiyang',
                'Lanzhou', 'Nanchang', 'Hefei', 'Haikou', 'Yinchuan', 'Kunming', 'Nanchong', 'Yantai', 'Nantong', 'Zhanjiang',
                'Huaian', 'Shaoxing', 'Zibo', 'Linyi', 'Wuxi', 'Yangzhou', 'Changzhou', 'Taizhou', 'Nantong', 'Jiangmen',
                'Zhangzhou', 'Guilin', 'Xuzhou', 'Huizhou', 'Jilin', 'Wuhu', 'Foshan', 'Yichang', 'Luoyang', 'Anshan', 'Nanchang',
                'Changzhi', 'Wuhu', 'Maoming', 'Liuzhou', 'Datong', 'Xiangyang', 'Shaoyang', 'Xiangtan', 'Shangrao', 'Luohe',
                'Huaian', 'Jinzhou', 'Huangshi', 'Nantong', 'Yueyang', 'Jingdezhen', 'Suqian', 'Dongying', 'Tongliao', 'Jining',
                'Hengyang', 'Xiangyang', 'Chaozhou', 'Huzhou', 'Suining', 'Wuhai', 'Jiamusi', 'Yangzhou', 'Lianyungang', 'Hulunbuir',
                'Yulin', 'Guangyuan', 'Yanbian Korean Autonomous Prefecture', 'Meizhou', 'Jiaxing', 'Yancheng', 'Bijie', 'Hegang',
                'London', 'Birmingham', 'Leeds', 'Glasgow', 'Sheffield', 'Bradford', 'Manchester', 'Liverpool', 'Edinburgh', 'Bristol',
            'Cardiff', 'Leicester', 'Wakefield', 'Coventry', 'Nottingham', 'Newcastle upon Tyne', 'Sunderland', 'Belfast', 'Brighton',
            'Hull', 'Plymouth', 'Stoke-on-Trent', 'Wolverhampton', 'Derby', 'Swansea', 'Southampton', 'Aberdeen', 'Portsmouth',
            'York', 'Peterborough', 'Dundee', 'Lancaster', 'Oxford', 'Newport', 'Preston', 'St Albans', 'Norwich', 'Chester',
            'Cambridge', 'Salisbury', 'Exeter', 'Gloucester', 'Lisburn', 'Chichester', 'Winchester', 'Derry', 'Armagh', 'Bangor',
            'Newry', 'Londonderry', 'Saint Asaph', 'Truro', 'Ely', 'Wells', 'St Davids', 'Ripon', 'Inverness', 'Stirling',
            'Dumfries', 'Perth', 'Fort William', 'Lerwick', 'Kirkwall', 'Kilmarnock', 'Ayr', 'Galashiels', 'Hawick', 'Selkirk',
            'Cupar', 'Crieff', 'Oban', 'Kirkcudbright', 'Newton Stewart', 'Melrose', 'Whitby', 'Scarborough', 'Filey', 'Bridlington',
            'Pickering', 'Pateley Bridge', 'Masham', 'Northallerton', 'Stokesley', 'Thirsk', 'Malton', 'Helmsley', 'Easingwold',
            'Richmond', 'Middlesbrough', 'Saltburn-by-the-Sea', 'Guisborough', 'Redcar', 'Skelton-in-Cleveland', 'Yarm', 'Billingham','Johannesburg', 'Cape Town', 'Durban', 'Pretoria', 'Port Elizabeth', 'Bloemfontein', 'East London', 'Kimberley',
                        'Polokwane', 'Nelspruit', 'Mbombela', 'Mahikeng', 'Rustenburg', 'Klerksdorp', 'Welkom', 'Botshabelo', 'Witbank',
                        'Richards Bay', 'Vanderbijlpark', 'Centurion', 'Uitenhage', 'Roodepoort', 'Paarl', 'Springs', 'Carletonville',
                        'Krugersdorp', 'George', 'Midrand', 'Westonaria', 'Middelburg', 'Vryheid', 'Orkney', 'Kimberley', 'Ermelo', 'Sasolburg',
                        'Ballito', 'Worcester', 'Bethal', 'Lichtenburg', 'Potchefstroom', 'Brits', 'Nigel', 'Parys', 'Kroonstad', 'Thohoyandou',
                        'Vereeniging', 'Secunda', 'Standerton', 'Komatipoort', 'Kroondal', 'Jansenville', 'Pietermaritzburg', 'Randfontein',
                        'Klerksdorp', 'Randburg', 'Ladysmith', 'Phalaborwa', 'Umtata', 'Queenstown', 'Eshowe', 'Zululand', 'Vryburg', 'Barberton',
                        'Port Shepstone', 'Simons Town', 'Oudtshoorn', 'Cradock', 'Bloemhof', 'Plettenberg Bay', 'Hermanus', 'Vredenburg',
                        'Springbok', 'Swartland', 'Harrismith', 'Upington', 'Richards Bay', 'De Aar', 'Upington', 'Mossel Bay', 'Beaufort West',
                        'Clanwilliam', 'Port Nolloth', 'Postmasburg', 'Graaff-Reinet', 'Calvinia', 'Prince Albert', 'Sutherland', 'Franschhoek',
                        'Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Brescia', 'Taranto']
                                                             

print(len(cities))
if len(cities) < 500:
    raise ValueError("Number of cities must be at least 500.")

# Assign unique cities to each row
geographic_location = cities[:500]

# Generate sample data for 500 cities
timestamps = pd.date_range(start='2024-01-01', periods=500, freq='H')
weather_temperature = np.random.randint(10, 30, size=500)
weather_humidity = np.random.randint(40, 80, size=500)
weather_precipitation = np.random.rand(500) * 5
weather_wind_speed = np.random.randint(5, 20, size=500)
weather_solar_radiation = np.random.randint(100, 500, size=500)
building_size = np.random.randint(500, 1000, size=500)
building_age = np.random.randint(5, 20, size=500)
building_construction = np.random.choice(['Concrete', 'Steel', 'Brick', 'Wood'], size=500)
building_insulation = np.random.choice(['High', 'Medium', 'Low'], size=500)
building_usage_type = np.random.choice(['Office', 'Warehouse'], size=500)
occupancy_count = np.random.randint(50, 200, size=500)
equipment_usage_hvac = np.random.randint(100, 300, size=500)
equipment_usage_lighting = np.random.randint(200, 500, size=500)
equipment_usage_machinery = np.random.randint(30, 100, size=500)
operational_schedule = np.random.choice(['Mon-Fri 9am-5pm', 'Sat-Sun 9am-5pm'], size=500)
energy_consumption = np.random.randint(1000, 2000, size=500)
electricity_price = np.random.uniform(0.1, 0.15, size=500)
gas_price = np.random.uniform(0.05, 0.08, size=500)
utility_tariff_type = np.random.choice(['Time-of-Use', 'Flat-Rate'], size=500)
# Create DataFrame
data = pd.DataFrame({
    'Timestamp': timestamps,
    'Weather_Temperature': weather_temperature,
    'Weather_Humidity': weather_humidity,
    'Weather_Precipitation': weather_precipitation,
    'Weather_Wind_Speed': weather_wind_speed,
    'Weather_Solar_Radiation': weather_solar_radiation,
    'Building_Size': building_size,
    'Building_Age': building_age,
    'Building_Construction': building_construction,
    'Building_Insulation': building_insulation,
    'Building_Usage_Type': building_usage_type,
    'Occupancy_Count': occupancy_count,
    'Equipment_Usage_HVAC': equipment_usage_hvac,
    'Equipment_Usage_Lighting': equipment_usage_lighting,
    'Equipment_Usage_Machinery': equipment_usage_machinery,
    'Operational_Schedule': operational_schedule,
    'Energy_Consumption': energy_consumption,
    'Electricity_Price': electricity_price,
    'Gas_Price': gas_price,
    'Utility_Tariff_Type': utility_tariff_type,
    'Geographic_Location': geographic_location
})

# Save DataFrame to CSV
data.to_csv('energy_data_500_cities.csv', index=False)
