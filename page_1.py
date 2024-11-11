import streamlit as st
import pandas as pd

# Sample data
data = {
    'Business Name': ['Coffee House', 'Downtown Deli', 'Book Haven', 'Urban Gym', 'Clothing Corner', 'Movie Magic', 'Techie Electronics', 'Local Market'],
    'Monday': [120, 100, 50, 90, 40, 150, 40, 160],
    'Tuesday': [130, 110, 55, 95, 45, 160, 45, 170],
    'Wednesday': [125, 115, 60, 100, 50, 170, 50, 175],
    'Thursday': [140, 120, 65, 105, 55, 180, 55, 180],
    'Friday': [160, 180, 70, 120, 60, 200, 60, 220],
    'Saturday': [200, 220, 80, 130, 75, 250, 75, 240],
    'Sunday': [180, 210, 85, 125, 70, 230, 70, 230],
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Streamlit app setup
st.title("Interactive Downtown San Jose Foot Traffic Analysis")

# User selects a day of the week and a business
selected_day = st.selectbox("Select a day of the week", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
selected_business = st.selectbox("Select a business", df['Business Name'])

# User slider for filtering foot traffic data
traffic_threshold = st.slider("Set minimum foot traffic threshold", min_value=0, max_value=300, value=50)

# Filter the data based on the slider value
filtered_df = df[df[selected_day] >= traffic_threshold]

# Display the average foot traffic for the selected business and day
traffic_value = df.loc[df['Business Name'] == selected_business, selected_day].values[0]
st.write(f"Average foot traffic for {selected_business} on {selected_day}: {traffic_value} people")

# Display a bar chart for businesses that meet the threshold
st.write(f"Businesses with foot traffic >= {traffic_threshold} on {selected_day}:")
st.bar_chart(filtered_df.set_index('Business Name')[selected_day])
