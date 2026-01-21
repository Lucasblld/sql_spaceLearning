import pandas as pd
import streamlit as st
import duckdb

df = pd.DataFrame(
    {"lot" : [1,2,3,4],
     "prix" : [10, 11, 24, 30],
     "quantite" : [5,2,3,4]}
)

sql = st.text_area("sql query")
st.dataframe(duckdb.query(sql))
st.write("hello world")


