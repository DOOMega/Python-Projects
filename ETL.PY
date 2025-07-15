import pandas as pd
import sqlite3

file_path = "Sales.csv"

def extract_data(file_path):
    df = pd.read_csv(file_path)
    print("Data is extracted.")
    print(df.head())
    return df

def transform_data(df):
    df["unit_price"] = df["unit_price"].fillna(df["unit_price"].mean())
    
    def valid_date(date_str):
        try:
            pd.to_datetime(date_str)
            return date_str
        except:
            return '2025-07-01'
        
    df["order_date"] = df["order_date"].apply(valid_date)
    df["order_date"] = pd.to_datetime(df["order_date"])

    df["total_price"] = df["unit_price"] * df["quantity"]

    print("Converted The Data: ")
    print(df.head())
    return df

def load_data(df, db_name='sales.db', table_name='sales'):
    if df is None:
        print("There is not have data for load.")
    
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists= "replace", index=False)
        conn.close()
        print(f"Data {table_name} loaded to table.")

    except Exception as e:
        print(f"Data load error: {e}")
    

def generate_report(df):
    report = df.groupby("category")["total_price"].sum().reset_index()
    print("Category based total sales report.")
    print(report)
    report.to_csv("Sales_report.csv", index=False)
    return report

def main():
    df = extract_data(file_path)
    df = transform_data(df)
    load_data(df)
    generate_report(df)

if __name__ == "__main__":
    main()