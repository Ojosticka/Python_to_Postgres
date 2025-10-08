# main.py
import os
import pandas as pd
from sqlalchemy import create_engine
from cred import db_config

def upload_csv_to_postgres(folder_path):
    """Uploads all CSV files in the folder to PostgreSQL."""
    
    # Create connection string
    engine = create_engine(
        f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@"
        f"{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )
    
    # Check if path exists
    if not os.path.exists(folder_path):
        print(f"Folder path does not exist: {folder_path}")
        return
    
    # Loop through files in folder
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            table_name = os.path.splitext(file)[0]  # table name from filename
            
            print(f"Importing {file} into table: {table_name}")
            
            # Load CSV
            df = pd.read_csv(file_path)
            
            # Upload to Postgres
            df.to_sql(table_name, engine, if_exists="replace", index=False)
            
            print(f"Successfully imported {file} into '{table_name}'\n")
    
    print("🎯 All CSVs imported successfully!")

if __name__ == "__main__":
    folder_path = input("Enter full path to folder containing CSV files: ").strip()
    upload_csv_to_postgres(folder_path)
