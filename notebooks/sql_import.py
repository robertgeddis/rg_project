# SQL Engine
import sqlalchemy as sa

db_path = r"C:\Users\rober\Documents\Python\rg_project\data\rg_project_database.db"
engine = sa.create_engine(f"sqlite:///{db_path}")

inspector = sa.inspect(engine)
print(f"Tables found: {inspector.get_table_names()}")
