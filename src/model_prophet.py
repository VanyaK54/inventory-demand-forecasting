from prophet import Prophet
import pandas as pd

def prepare_prophet_data(df, date_col='date', target_col='units_sold'):
    df_prophet = df[[date_col, target_col]].copy()
    df_prophet.columns = ['ds', 'y']
    return df_prophet

def forecast_with_prophet(df, holidays_df=None, periods=30):
    df_prophet = prepare_prophet_data(df)

    if holidays_df is not None:
        holidays_df.columns = ['ds', 'holiday', 'country']
        m = Prophet(holidays=holidays_df[['ds', 'holiday']])
    else:
        m = Prophet()

    m.fit(df_prophet)
    future = m.make_future_dataframe(periods=periods)
    forecast = m.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
