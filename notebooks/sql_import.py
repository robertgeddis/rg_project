# SQL Engine
import sqlalchemy as sa

# SQL Engine

db_path = r"C:\Users\rober\Documents\Python\bitcoin_gold_analysis\data\bitcoin_gold_database.db"
engine = sa.create_engine(f"sqlite:///{db_path}")

inspector = sa.inspect(engine)
print(f"Tables found: {inspector.get_table_names()}")
engine = sa.create_engine(f"sqlite:///{db_path}")

inspector = sa.inspect(engine)
print(f"Tables found: {inspector.get_table_names()}")
