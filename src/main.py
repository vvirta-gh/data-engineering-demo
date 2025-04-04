import pandas as pd
import plotly.express as px



def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    # Esimerkiksi täytetään puuttuvat arvot
    df['Score'] = df['Score'].fillna(df['Score'].mean())
    return df

def plot_top10(df: pd.DataFrame):
    top_10 = df.head(10)
    fig = px.histogram(top_10, x='Country or region', y='Score')
    fig.update_yaxes(range=[7, 8])
    fig.show()
    
def main():
    data_path = '/workspaces/data-engineering-demo/data/2019.csv'
    df = load_data(data_path)
    df = clean_data(df)
    plot_top10(df) 


if __name__ == "__main__":
    main()