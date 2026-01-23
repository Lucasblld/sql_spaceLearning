import os
import logging

import duckdb
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercises_sql.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

SOLUTION_PATH = "answer"
con = duckdb.connect(database="data/exercises_sql.duckdb", read_only=False)

# SIDE BAR
with st.sidebar:
    theme = st.selectbox(
        "what would you like to review?",
        ("cross_join", "group_by", "window_functions"),
        index=None,
        placeholder="select contact method...",
    )
    st.write("You selected ", theme)

    exersice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exersice)

    try:
        exercise_name = exersice.loc[0, "exercise_name"]
        with open(
            f"{SOLUTION_PATH}/{exercise_name}.sql", "r", encoding="utf-8"
        ) as solution_file:
            answer = solution_file.read()

        SOLUTION = con.execute(answer).df()
    except (AttributeError, KeyError) as e:
        print(f"{e} no exercise selected")
        SOLUTION = None

st.header("enter your code: ")
st.write("""Spaced repetition system SQL practice""")

query = st.text_area(label="votre sql ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

    if len(result.columns) != len(SOLUTION.columns):
        st.write("some columns are missing")

    n_lines_diff = result.shape[0] - SOLUTION.shape[0]
    if n_lines_diff != 0:
        st.write(f"the are a difference of {n_lines_diff} lines")

    try:
        result = result[SOLUTION.columns]
        st.dataframe(result.compare(SOLUTION))
    except KeyError as e:
        st.write("Some columns are missing")

tab2, tab3 = st.tabs(["Tables", "Solution"])
#
with tab2:
    exersice_tables = exersice.loc[0, "tables"]
    for table in exersice_tables:
        st.write(f"table : {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    if query:
        st.text(answer)
        st.dataframe(SOLUTION)

#    st.write("query SOLUTION")
#    st.write(ANSWER_STR)
#    st.write("result")
#    st.dataframe(SOLUTION)
