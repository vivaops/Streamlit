import streamlit as st
from gsheetsdb import connect
import json

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     return rows

# sheet_url = st.secrets["public_gsheets_url"]
# print(sheet_url)
# # run_query(f'SELECT * FROM "{sheet_url}"')
# rows = run_query(f'SELECT * FROM "{sheet_url}"')
# # info = json.loads(rows.decode("utf-8"))
# print(rows)

# # Print results.
# for row in rows:
#     st.write(f"{row.Description}")

# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     return rows

# sheet_url = st.secrets["public_gsheets_url"]
# rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
# for row in rows:
#     st.write(f"{row.Fivetran}")


@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

# Query first sheet
sheet1_url = st.secrets["source_connectors"]
rows = run_query(f'SELECT * FROM "{sheet1_url}"')

st.subheader('Sheet 1:')
# Print results.
for row in rows:
    st.write(f"{row.PlatformFeatures} ")

# Query second sheet
sheet2_url = st.secrets["Transformation_at_source"]
rows = run_query(f'SELECT * FROM "{sheet2_url}"')
print(rows)

st.subheader('Sheet 2:')
# Print results.
for row in rows:
    st.write(f"{row.PlatformFeatures}")