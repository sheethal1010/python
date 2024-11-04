#Import necessary libraries
import seaborn as sns #Importing for visual
import plotly.express as px
import pandas as pd
import numpy as np

# load datasheet
tips = sns.load_dataset('tips')

#visual using plotly

fig1 = px.bar(tips,x="day",y="tip")

fig2 = px.scatter(tips,x="total_bill",y="tip")

# streamlit web app layout
st.title("Data Visualizatyion with Plotly")

#Section 1: Bar plot

st.header("Plot 1: Bar Plot - tips by Day")
st.plotly_chart(fig1)
st.markdown('''saturday has more tips''')
