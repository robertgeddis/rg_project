import os
import sys

import pandas as pd

# Path logic
project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

# Database engine
try:
    from sql_engine import engine
except ImportError:
    engine = None

# Dataframe formatting
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)


def list_tables():
    if engine:
        from sqlalchemy import inspect

        return inspect(engine).get_table_names()
    return []
