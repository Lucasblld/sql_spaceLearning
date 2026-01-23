import duckdb
import streamlit as st

SOLUTION_PATH = "answer"
con = duckdb.connect(database="data/exercises_sql.duckdb", read_only=False)

# solution = duckdb.sql(ANSWER_STR).df()

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

st.header("enter your code: ")
st.write("""Spaced repetition system SQL practice""")

query = st.text_area(label="votre sql ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)
#
#    if len(result.columns) != len(solution.columns):
#        st.write("some columns are missing")
#
#    n_lines_diff = result.shape[0] - solution.shape[0]
#    if n_lines_diff != 0:
#        st.write(f"the are a difference of {n_lines_diff} lines")
#
#    try:
#        result = result[solution.columns]
#        st.dataframe(result.compare(solution))
#    except KeyError as e:
#        st.write("Some columns are missing")
#
tab2, tab3 = st.tabs(["Tables", "Solution"])
#
with tab2:
    exersice_tables = exersice.loc[0, "tables"]
    for table in exersice_tables:
        st.write(f"table : {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    exercise_name = exersice.loc[0, "exercise_name"]
    with open(
        f"{SOLUTION_PATH}/{exercise_name}.sql", "r", encoding="utf-8"
    ) as solution_file:
        sql = solution_file.read()
        st.text(sql)
        solution_table = con.execute(sql).df()
        st.dataframe(solution_table)

#    st.write("query solution")
#    st.write(ANSWER_STR)
#    st.write("result")
#    st.dataframe(solution)
