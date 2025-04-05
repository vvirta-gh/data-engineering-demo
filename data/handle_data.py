import pandas as pd

class HandleData():
    def __init__(self):
        """
        Initialize the class with the base path to the data
        """
        self.base_path = '/workspaces/data-engineering-demo/data'
    
    def load_data(self, year: str) -> pd.DataFrame:
        file_path = f"{self.base_path}/{year}.csv"
        try:
            df = pd.read_csv(file_path)
            print(f"Successfully loaded data for {year}.")
            return df
        except FileNotFoundError:
            print(f"File for {year} not found at {file_path}.")
            return pd.DataFrame()
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the DataFrame by handling missing values, removing duplicates,
        and standardizing column names.
        """
        if df.empty:
            print("DataFrame is empty. No cleaning performed.")
            return df

        # Drop duplicate rows
        df = df.drop_duplicates()
        
        # Handle missing values (e.g., fill with a placeholder or drop rows/columns)
        df = df.fillna("N/A")  # Replace NaN with "N/A" (customize as needed)
        
        # Standardize column names (e.g., lowercase and replace spaces with underscores)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        print("Data cleaning completed.")
        return df
    
    def get_summary(self, df: pd.DataFrame) -> dict:
        
        if df.empty:
            return {"message:": "DataFrame is empty."}
        return {
            "row_count": len(df),
            "columns": list(df.columns),
            "head": df.head().to_dict(),
            "tail": df.tail().to_dict(),
            "describe": df.describe().to_dict
        }
    
        

if __name__ == "__main__":
    data_handler = HandleData()
    data_2019 = data_handler.load_data("2019")
    cleaned_data = data_handler.clean_data(data_2019)
    summary = data_handler.get_summary(cleaned_data)
    print(summary)