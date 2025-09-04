import os
import pandas as pd
from sqlalchemy import create_engine

# --- Load queries from file ---
def load_queries(path="sql/queries.sql"):
    queries = {}
    with open(path) as f:
        blocks = f.read().split(";")

    for block in blocks:
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if len(lines) > 1:  # needs name + query
            name = lines[0].lstrip("--").strip()
            sql = " ".join(lines[1:]).strip()
            if sql:  # only keep if not empty
                queries[name] = sql
    return queries

# --- DB connection ---
engine = create_engine("mysql+pymysql://root:Krishna1%40%23%24@localhost/credit_fraud")

# --- Export queries ---
queries = load_queries("sql/queries.sql")
os.makedirs("excel", exist_ok=True)
output_file = "excel/fraud_analysis.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for name, sql in queries.items():
        try:
            df = pd.read_sql(sql, engine)
            if df.empty:
                print(f"Skipped {name}: query returned no data")
                continue
            df.to_excel(writer, sheet_name=name[:30], index=False)  # sheet names max 31 chars
            print(f"Exported {name}")
        except Exception as e:
            print(f"Failed {name}: {e}")

print(f"All valid queries saved in {output_file}")
