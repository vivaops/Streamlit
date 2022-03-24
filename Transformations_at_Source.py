import streamlit as st
import pandas as pd
import numpy as np
import time

data = pd.read_csv("data//Break-up of ETL-ELT Tool Accelerator.xlsx - Transformations at Source.csv")
# dataframe = data.to_string()
# print(data)
# print("hello")
# st.dataframe(data)
first = data["Platform Features"]

# print(list(first))

# st.dataframe(dataframe[["Platform Features"]], width=2000, height=900)
# st.write(list(first))
# page = ['hello'] 
# st.title("hello")
# select = st.radio("select the feature", list(first))

# @st.cache
# def ret_time():
#     time.sleep(5)
#     return time.time()
# loc = st.checkbox(first)
# st.write(loc)

# if st.checkbox("2"):cd 
#     st.write(ret_time())

st.write('Select feature:')
opts = list(first)
known_variables = {name: st.checkbox(f"{name}") for  name in opts}  
print(known_variables)
print(known_variables.values())  

# if sum(known_variables.values()) < 3:
#     st.write('You have to select minimum 3 variables.')
# elif sum(known_variables.values()) == 3:
#     st.write('Now put the values of your selected variables in SI units.')
# else:
#     st.write('You can select maximum 3 variables.')