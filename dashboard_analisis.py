import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

# Load data
data_suhu = pd.read_csv('data_kualitas_udara_dengan_ISPU.csv')
data_air_quality = pd.read_csv('data_kualitas_udara_dengan_ISPU.csv')
data_suhu['Date'] = pd.to_datetime(data_suhu['year'].astype(str) + data_suhu['month'].astype(str).str.zfill(2), format='%Y%m')
data_air_quality['Date'] = pd.to_datetime(data_air_quality['year'].astype(str) + data_air_quality['month'].astype(str).str.zfill(2), format='%Y%m')

# Sidebar for user options
st.sidebar.title("Options")

# Select data for temperature
st.sidebar.subheader("Temperature Data")
temp_columns = st.sidebar.multiselect('Select temperature columns:', ['TEMP', 'TEMP_kelvin'])
show_temp_raw_data = st.sidebar.checkbox('Show Raw Temperature Data')

# Select data for air quality
st.sidebar.subheader("Air Quality Data")
air_quality_columns = st.sidebar.multiselect('Select air quality columns:', ['PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP'])
show_air_quality_raw_data = st.sidebar.checkbox('Show Raw Air Quality Data')

# Title
st.title('Interactive Air Quality and Temperature Dashboard')

# Data Display
st.subheader("Temperature Data")
if temp_columns:
    temp_data = data_suhu.set_index('Date')[temp_columns]
    st.line_chart(temp_data)
    
if show_temp_raw_data:
    st.subheader('Raw Temperature Data')
    st.write(data_suhu)

st.subheader("Air Quality Data")
if air_quality_columns:
    air_quality_data = data_air_quality.set_index('Tanggal')[air_quality_columns]
    st.line_chart(air_quality_data)

if show_air_quality_raw_data:
    st.subheader('Raw Air Quality Data')
    st.write(data_air_quality)

# Correlation and Heatmap
st.subheader("Correlation and Heatmap")
st.write("Correlation between selected air quality parameters and temperature.")
selected_columns = air_quality_columns + temp_columns
correlation = data_air_quality[selected_columns].corr()
st.write(correlation)

# Create a heatmap using Altair
st.write("Heatmap of Correlation")
chart = alt.Chart(correlation.unstack().reset_index(name='corr'), height=200, width=200).mark_rect().encode(
    x=alt.X('level_0:N', title=None),
    y=alt.X('level_1:N', title=None),
    color=alt.Color('corr:Q', scale=alt.Scale(scheme='redblue', domain=[-1, 1])),
    tooltip=[alt.Tooltip('corr:Q', format='.2f')]
).properties(title='Heatmap of Correlation')
st.altair_chart(chart, use_container_width=True)
