import pandas as pd
import streamlit as st
import duckdb
import io

csv1 = """
beverage, price
orange juice, 2
Expresso, 3
tea, 1
"""

beverages = pd.read_csv(io.StringIO(csv1))

csv2 = '''
food_item, food_price
cookie, 2.5
pain, 2.3
muffin, 4
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer = '''
SELECT * FROM beverages, food_items
'''

solution = duckdb.sql(answer).df()
st.header("enter your code: ")
query = st.text_area(label="votre sql ici", key='user_input')

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("beverages")
    st.dataframe(beverages)
    st.write("food items")
    st.dataframe(food_items)
    st.write("solution")
    st.dataframe(solution)

with tab3:
    st.write(answer)

st.write("""
Spaced repetition system SQL practice
""")


option = st.selectbox(
    "what would you like to review?",
    ("Joins", "GroupBy", "Windows functions"),
    index=None,
    placeholder='select contact method...',
)

st.write("ou selected ", option)

sql_query = st.text_area(label='Entrez votre query')
result = duckdb.query(sql_query).df()
st.write('votre query : ', sql_query)
st.dataframe(result)


