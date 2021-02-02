import streamlit as st
import pandas as pd
import numpy as np

st.title('New Food Balances')

#Download the CSV file from FAO website and upload it to your own AWS S3 bucket. Paste the url below.
DATA_URL = ('https://your-bucket.s3-eu-west-1.amazonaws.com/FoodBalanceSheets_E_All_Data_Normalized.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
