import os

from sqlalchemy import create_engine


def get_engine():
    # Finds the folder where this specific script lives
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # This uses 'os' to build the path safely, which removes the yellow squiggle
    db_path = os.path.join(base_dir, "data", "rg_project_database.db")

    # Return the connection engine
    return create_engine(f"sqlite:///{db_path}")
