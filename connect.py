import streamlit as st
from gsheetsdb import connect
# Create a connection object.
conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows
sheet1_url = st.secrets["gsheets"]["source_connectors"]
rows = run_query(f'SELECT * FROM "{sheet1_url}"')
st.subheader('Source Connectors:')
# Print results.
for row in rows:
    st.write(f"{row.Description} has a :{row.Hevo}:")
sheet2_url = st.secrets["gsheets"]["miscellaneous"]
rows = run_query(f'SELECT * FROM "{sheet2_url}"')
st.subheader('Miscellaneous:')
# Print results.
for row in rows:
    st.write(f"{row.Description}")