import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("AsiakasTietokanta.db")

# Query data from a table
query = "SELECT * FROM Asiakkaat"  # Replace 'Asiakkaat' with your table name
df = pd.read_sql_query(query, conn)
query2 = "SELECT * FROM Myynnit"
df2 = pd.read_sql_query(query2, conn)


# Export to CSV
df.to_csv("./data/Asiakkaat.csv", index=False)
df2.to_csv("./data/Myynnit.csv", index=False)

# Close the connection
conn.close()
