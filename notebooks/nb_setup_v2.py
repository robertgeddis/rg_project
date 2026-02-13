import os
import sys

# The GPS must come BEFORE the imports
_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _root not in sys.path:
    sys.path.append(_root)


def get_assets():
    import pandas as pd

    from sql_engine import engine

    return pd, engine


def list_tables():
    _, engine = get_assets()
    if engine:
        from sqlalchemy import inspect

        return inspect(engine).get_table_names()
    return []
