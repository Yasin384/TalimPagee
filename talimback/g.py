import psycopg2
import urllib.parse
import os

# Get environment variables
password = os.getenv('PGPASSWORD', 'ncfZmDqGdkDLIOOLRQNBBddytpSPwCmh')
encoded_password = urllib.parse.quote_plus(password)

# Connection string with SSL enabled
DATABASE_URL = f"postgresql://{os.getenv('PGUSER', 'postgres')}:{encoded_password}@{os.getenv('PGHOST', 'postgres.railway.internal')}:{os.getenv('PGPORT', '5432')}/{os.getenv('POSTGRES_DB', 'railway')}?sslmode=require"

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(DATABASE_URL)
    print("Connection successful")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
