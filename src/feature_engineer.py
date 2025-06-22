import pandas as pd

def create_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['is_weekend'] = df['day_of_week'] >= 5
    df['rolling_avg'] = df['units_sold'].rolling(window=7).mean()
    return df
