import streamlit as st
import pandas as pd
import numpy as np
import time

data = pd.read_csv("data//Break-up of ETL-ELT Tool Accelerator.xlsx - Data warehouse destination.csv")

first = data["Platform Features"].dropna();
discard = ["description","Description"]
  
# drop rows that contain the partial string "description"
first = first[~first.str.contains('|'.join(discard))]
print(first)

st.write('Select feature:')
opts = list(first)
print(opts)

known_variables = {}
for i, todo_text in enumerate(opts):
        var = st.checkbox(label=f'{todo_text}', key=i)
        print(var)
        known_variables.update({todo_text:var})

print(known_variables)