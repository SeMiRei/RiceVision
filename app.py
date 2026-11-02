import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="RiceVision",
    page_icon="🌾",
    layout="wide"
)

# Define the pages
main_page = st.Page("pages/home.py", title="Home", icon="🏠")
rice_leaf_disease_classify = st.Page("pages/rice_leaf_disease_classification.py", title="Rice Leaf Analysis", icon="🔍")
disease_guide = st.Page("pages/disease_guide.py", title="Disease Guide", icon="🌱")
overview = st.Page("pages/overview.py", title="Project Overview", icon="📊")
about = st.Page("pages/about.py", title="About", icon="ℹ️")

# Set up navigation
pg = st.navigation([main_page, rice_leaf_disease_classify, disease_guide, overview, about])

# Run the selected page
pg.run()