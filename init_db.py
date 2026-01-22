import io

import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql.duckdb", read_only=False)

# ----------
# EXERCISES LIST
# ----------
data = {
    "theme": ["cross_join", 'window_functions'],
    "exercise_name": ["beverage_and_food", "simple_window"],
    "tables": [["beverages", "food_items"], ["simple_window"]],
    "last_reviewed": ["1970-01-01", "1970-01-01"]
}

memory_state_df = pd.DataFrame(data)
con.execute(
    """
CREATE TABLE IF NOT EXISTS memory_state AS SELECT * from memory_state_df
"""
)

# ----------
# CROSS JOIN
# ----------
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

con.execute(
    """
CREATE TABLE IF NOT EXISTS beverages AS SELECT * from beverages
"""
)

con.execute(
    """
CREATE TABLE IF NOT EXISTS food_items AS SELECT * from food_items
"""
)
