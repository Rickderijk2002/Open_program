import pandas as pd
import streamlit as st
import plotly.express as px

import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Set the layout to the Streamlit app as wide
st.set_page_config(page_title='Crime Rate Prediction', page_icon=':bar_chart:', layout='wide')

# Define the image URL and caption
image_url = 'https://www.usatoday.com/gcdn/-mm-/8feaaab14d7b65ae58708871aa2b081b20258548/c=0-48-4034-2324/local/-/media/USATODAY/test/2013/12/14//1387050313000-XXX-chicago-murder-capital09.JPG?width=3200&height=1806&fit=crop&format=pjpg&auto=webp'
image_caption = 'Chicago'

# Display the image
st.sidebar.image(image_url)

# Display the information text
st.sidebar.title('Crime Rate Prediction')
st.sidebar.info('This is the web application for predicting the crime rate in Chicago.')

st.sidebar.title('Which models has been used for this prediction ?')
st.sidebar.info('The model RandomForest has been used for the predictions and neural networks')

st.sidebar.title('The Data')
st.sidebar.info('The data has been obtained through the website of kaggle')
st.sidebar.text('The website can be found here: https://www.kaggle.com/datasets/currie32/crimes-in-chicago?select=Chicago_Crimes_2012_to_2017.csv')

# Load the DataFrame from the file
df_final = pd.read_csv('crimes_chicago.csv')

# Create a Streamlit app
st.title('Crime Visualization')
st.write('This app visualizes the amount of crimes for different community areas.')

# Get unique community areas and primary types
unique_community_areas = df_final['community_area'].unique()
unique_primary_types = df_final['primary_type'].unique()

# Prompt the user to select a community area
selected_area = st.selectbox('Select Community Area', unique_community_areas)

# Prompt the user to select a primary type of crime
selected_type = st.selectbox('Select Primary Crime Type', unique_primary_types)

if selected_area and selected_type:
    # Filter the data based on the selected area and primary type
    filtered_data = df_final[(df_final['community_area'] == selected_area) & (df_final['primary_type'] == selected_type)]

    # Create the plot using Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=filtered_data['dates'], y=filtered_data['amount_crimes'], name='Amount of Crimes'))
    fig.add_trace(go.Scatter(x=filtered_data['dates'], y=filtered_data['prediction_NN'], name='Predicted (NN)'))
    fig.add_trace(go.Scatter(x=filtered_data['dates'], y=filtered_data['prediction_RF'], name='Predicted (RF)'))

    fig.update_layout(xaxis_title='Date', yaxis_title='Amount of Crimes',
                      title=f'Amount of {selected_type} Crimes for Community Area {selected_area}')

    # Display the plot
    st.plotly_chart(fig)
