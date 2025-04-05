from data.handle_data import HandleData

def main():
    # Initialize the HandleData class
    data_handler = HandleData()
    
    # Load data for a specific year
    year = "2018"
    data = data_handler.load_data(year)
    
    # Clean the loaded data
    cleaned_data = data_handler.clean_data(data)
    
    # Get a summary of the cleaned data
    summary = data_handler.get_summary(cleaned_data)
    
    # Print the summary
    print(f"Summary for {year} data:")
    print(summary)

if __name__ == "__main__":
    main()