from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import urllib


server = "localhost"
database = "BankDW"

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}"
)


DATASET_PATH = Path("datasets")


TABLES = [
    "customers",
    "branches",
    "accounts",
    "loans",
    "transactions"
]


for table in TABLES:

    file_path = DATASET_PATH / f"{table}.csv"

    print(f"Loading {table}...")

    dataframe = pd.read_csv(file_path)

    dataframe.to_sql(
        name=table.capitalize(),
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"{table} Loaded Successfully")