import pandas as pd

def add_time_features(df):
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['week'] = df['date'].dt.isocalendar().week
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    return df

def create_rolling_features(df, group_cols=['warehouse_id', 'product_id'], target='units_sold'):
    df = df.sort_values(['warehouse_id', 'product_id', 'date'])
    df['rolling_mean_7'] = df.groupby(group_cols)[target].transform(lambda x: x.rolling(7, min_periods=1).mean())
    df['rolling_std_7'] = df.groupby(group_cols)[target].transform(lambda x: x.rolling(7, min_periods=1).std().fillna(0))
    return df
