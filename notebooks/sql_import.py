from nb_setup_v2 import get_assets, list_tables

pd, engine = get_assets()
print(f"Success! Tables: {list_tables()}")

# Enter the code above as the first cell in .ipynb files
# Use syntax below afterwards to pull data


''' 
query = """
SELECT 
    m.Date, 
    m.M2, 
    f.SP500, 
    f.BTC, 
    f.Gold
FROM macro_data m
LEFT JOIN market_data_filled f ON m.Date = f.Date
WHERE f.SP500 IS NOT NULL
ORDER BY m.Date ASC
"""

df = pd.read_sql(query, engine)
df['Date'] = pd.to_datetime(df['Date'])
df.head() '''
