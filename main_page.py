import streamlit as st
import pandas as pd
import numpy as np
import time

st.markdown("Welcome Home")
st.sidebar.markdown("Amethyst Insights")

message = "Welcome to Amethyst Insights!"
message += "A thorough AI-powered analysis using foot traffic data for all your business questions!"
st.write(message)

st.subheader('Dive into our features: ', divider='grey')
col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("main_page.py", label="Home", icon="🏠", disabled=True)

with col2:
   st.page_link("pages/page_1.py", label="Foot Traffic Overview", icon="1️⃣")

with col3:
   st.page_link("pages/page_2.py", label="AI Insight Reports", icon="2️⃣")

with col4:
   st.page_link("pages/page_3.py", label="Feedback", icon="3️⃣")

