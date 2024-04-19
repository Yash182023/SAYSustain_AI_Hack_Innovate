import streamlit as st
import pandas as pd
import plotly.express as px

# Load the environmental data CSV
df = pd.read_csv('environmental_data_new.csv')

# Define Streamlit app
st.title('Environmental Data Analytics Dashboard')

# Sidebar for filtering options
st.sidebar.subheader('Filter Data')
location_filter = st.sidebar.multiselect('Select Locations', df['Location'].unique())

# Filter data based on selected filters
filtered_df = df[df['Location'].isin(location_filter)]

# Define color palette
colors = px.colors.qualitative.Pastel

# Bar plot for Temperature
st.subheader('Temperature Variation')
temperature_fig = px.bar(filtered_df, x='Location', y='Temperature(C)', 
                         title='Temperature Variation by Location', color='Location', 
                         color_discrete_sequence=colors)
st.plotly_chart(temperature_fig)

# Bar plot for Humidity
st.subheader('Humidity Variation')
humidity_fig = px.bar(filtered_df, x='Location', y='Humidity(%)', 
                      title='Humidity Variation by Location', color='Location', 
                      color_discrete_sequence=colors)
st.plotly_chart(humidity_fig)

# Bar plot for Precipitation
st.subheader('Precipitation Variation')
precipitation_fig = px.bar(filtered_df, x='Location', y='Precipitation(mm)', 
                            title='Precipitation Variation by Location', color='Location', 
                            color_discrete_sequence=colors)
st.plotly_chart(precipitation_fig)

# Bar plot for Wind Speed
st.subheader('Wind Speed Variation')
wind_speed_fig = px.bar(filtered_df, x='Location', y='Wind_Speed(m/s)', 
                        title='Wind Speed Variation by Location', color='Location', 
                        color_discrete_sequence=colors)
st.plotly_chart(wind_speed_fig)

st.subheader('Air Quality Index (AQI)')
aqi_fig = px.bar(filtered_df, x='Location', y='AQI', 
                 title='Air Quality Index (AQI) by Location', color='Location', 
                 color_discrete_sequence=colors)
st.plotly_chart(aqi_fig)