import pandas as pd
from sqlalchemy import create_engine
import warnings 

warnings.filterwarnings("ignore")

# Step 1: Read Excel file
df = pd.read_csv("../data/raw/creditcard.csv" , low_memory=False)

print(df.shape)
print(df.head())

# Step 2: Connect to MySQL
engine = create_engine("mysql+pymysql://root:Krishna1%40%23%24@localhost/credit_fraud" , echo=False)

# Step 3: Upload full dataset into MySQL
df.to_sql("transaction", engine, if_exists="replace", index=False ,chunksize=10000,
    method="multi")

print("Data loaded into MySQL successfully!")