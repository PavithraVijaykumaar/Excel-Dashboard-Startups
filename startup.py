import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import openpyxl

st.set_page_config(page_title='STARTUP DASHBOARD')
st.header('INDIAN STARTUPS 2021')

#LOADING THE DATAFRAME
excel_file='INDIAN STARTUP FUNDING 2021.xlsx'
sheet_name='Pivot sheet'

df_field=pd.read_excel(excel_file, 
                 sheet_name=sheet_name, 
                 usecols='A:B',
                 header=2)
df_city=pd.read_excel(excel_file,
                      sheet_name=sheet_name,
                      usecols='A:B',
                      header=31)

df=pd.read_excel(excel_file,
                 sheet_name=sheet_name,
                 usecols='A:C',
                 header=45)

st.dataframe(df_field)
st.dataframe(df_city)
st.dataframe(df)

pie_chart = px.pie(df_city,
                  title='City Involved',
                  values='City',
                  names='Startups')
st.plotly_chart(pie_chart)

img=Image.open('st.jpg')
st.image(img,
         caption='Indian Startup Funding',
         use_column_width=True)

groupby_column=st.selectbox('Sector','City')

output_column=['Startups']
df_grouped=df.groupby(by=[groupby_column],as_index=False)[output_column].sum()
st.dataframe(df_grouped)


