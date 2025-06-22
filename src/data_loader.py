import pandas as pd
from pathlib import Path

def load_inventory_data(path="data/raw/inventory.csv"):
    df = pd.read_csv(path, parse_dates=['date'])
    return df

def load_weather_data(path="data/external/weather.csv"):
    df = pd.read_csv(path, parse_dates=['date'])
    return df

def load_holidays(path="data/external/holidays.csv"):
    df = pd.read_csv(path, parse_dates=['date'])
    return df

def merge_datasets(inventory_df, weather_df, holidays_df):
    # Merge weather based on location
    merged_df = pd.merge(inventory_df, weather_df, how='left',
                         left_on=['date', 'warehouse_id'],
                         right_on=['date', 'location'])

    # Drop redundant column
    merged_df.drop(columns=['location'], inplace=True)

    # Add holiday flag
    merged_df['is_holiday'] = merged_df['date'].isin(holidays_df['date'])
    merged_df['is_holiday'] = merged_df['is_holiday'].astype(int)

    return merged_df
