import io

import duckdb
import pandas as pd
import streamlit as st

CSV1 = """
beverage,price
orange juice, 2
Expresso, 3
tea, 1
"""

CSV2 = """
food_item,food_price
cookie, 2.5
pain, 2.3
muffin, 4
"""

beverages = pd.read_csv(io.StringIO(CSV1))
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages, food_items
"""
solution = duckdb.sql(ANSWER_STR).df()

# SIDE BAR
with st.sidebar:
    option = st.selectbox(
        "what would you like to review?",
        ("Joins", "GroupBy", "Windows functions"),
        index=None,
        placeholder="select contact method...",
    )
    st.write("You selected ", option)

st.header("enter your code: ")
st.write("""Spaced repetition system SQL practice""")

query = st.text_area(label="votre sql ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solution.columns):
        st.write("some columns are missing")

    n_lines_diff = result.shape[0] - solution.shape[0]
    if n_lines_diff != 0:
        st.write(f"the are a difference of {n_lines_diff} lines")

    try:
        result = result[solution.columns]
        st.dataframe(result.compare(solution))
    except KeyError as e:
        st.write("Some columns are missing")

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("beverages")
    st.dataframe(beverages)
    st.write("food items")
    st.dataframe(food_items)

with tab3:
    st.write("query solution")
    st.write(ANSWER_STR)
    st.write("result")
    st.dataframe(solution)
