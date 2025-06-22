import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def prepare_lstm_data(series, time_steps=7):
    X, y = [], []
    for i in range(len(series) - time_steps):
        X.append(series[i:i+time_steps])
        y.append(series[i+time_steps])
    return np.array(X), np.array(y)

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(64, activation='relu', input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_lstm_model(df, column='units_sold', time_steps=7):
    scaler = MinMaxScaler()
    values = df[[column]].values
    scaled = scaler.fit_transform(values)

    X, y = prepare_lstm_data(scaled, time_steps)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    model = build_lstm_model((X.shape[1], 1))
    model.fit(X, y, epochs=10, verbose=1)

    return model, scaler
