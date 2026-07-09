import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU ,Dense

df = pd.read_csv(
    r"C:\Users\user\Documents\GitHub\FULL-STACK-B-8-Wed-Thru-Fri\FinalAssessment\SpaceX SPCX Stock Price 30m Interval\spacex.csv"
)

print(df.head())
print(df.info())

print(df.info())


df["Datetime"] = pd.to_datetime(df["Datetime"])
df = df.sort_values("Datetime")

close_data = df[["Close"]]

scaler = MinMaxScaler()
close_data = scaler.fit_transform(close_data)

x = []
y = []

for i in range(20, len(close_data)):
    x.append(close_data[i-20:i])
    y.append(close_data[i])

x = np.array(x)
y = np.array(y)

split = int(len(x) * 0.8)

x_train = x[:split]
x_test = x[split:]

y_train = y[:split]
y_test = y[split:]

print("Training Shape :", x_train.shape)
print("Testing Shape :", x_test.shape)

# Simple RNN Model

model_rnn = Sequential()

model_rnn.add(SimpleRNN(50, activation="tanh", input_shape=(x_train.shape[1], 1)))
model_rnn.add(Dense(1))

model_rnn.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

model_rnn.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(x_test, y_test),
    verbose=1
)

# Prediction

pred_rnn = model_rnn.predict(x_test)

pred_rnn = scaler.inverse_transform(pred_rnn)
actual = scaler.inverse_transform(y_test.reshape(-1, 1))

rnn_mae = mean_absolute_error(actual, pred_rnn)
rnn_mse = mean_squared_error(actual, pred_rnn)
rnn_rmse = np.sqrt(rnn_mse)

print("\nRNN Results")
print("MAE :", rnn_mae)
print("MSE :", rnn_mse)
print("RMSE :", rnn_rmse)

# Graph

plt.figure(figsize=(10, 5))
plt.plot(actual, label="Actual Price")
plt.plot(pred_rnn, label="RNN Prediction")
plt.title("RNN Prediction")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.show()



# LSTM Model

model_lstm = Sequential()

model_lstm.add(LSTM(50, input_shape=(x_train.shape[1], 1)))
model_lstm.add(Dense(1))

model_lstm.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

model_lstm.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(x_test, y_test),
    verbose=1
)

# Prediction

pred_lstm = model_lstm.predict(x_test)

pred_lstm = scaler.inverse_transform(pred_lstm)


lstm_mae = mean_absolute_error(actual, pred_lstm)
lstm_mse = mean_squared_error(actual, pred_lstm)
lstm_rmse = np.sqrt(lstm_mse)

print("\nLSTM Results")
print("MAE :", lstm_mae)
print("MSE :", lstm_mse)
print("RMSE :", lstm_rmse)

# Graph

plt.figure(figsize=(10, 5))
plt.plot(actual, label="Actual Price")
plt.plot(pred_lstm, label="LSTM Prediction")
plt.title("LSTM Prediction")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

# GRU Model


model_gru = Sequential()

model_gru.add(GRU(32, input_shape=(x_train.shape[1], 1)))
model_gru.add(Dense(1))

model_gru.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

model_gru.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(x_test, y_test),
    verbose=1
)

# Prediction

pred_gru = model_gru.predict(x_test)

pred_gru = scaler.inverse_transform(pred_gru)

gru_mae = mean_absolute_error(actual, pred_gru)
gru_mse = mean_squared_error(actual, pred_gru)
gru_rmse = np.sqrt(gru_mse)

print("\nGRU Results")
print("MAE :", gru_mae)
print("MSE :", gru_mse)
print("RMSE :", gru_rmse)

# Graph

plt.figure(figsize=(10,5))
plt.plot(actual, label="Actual Price")
plt.plot(pred_gru, label="GRU Prediction")
plt.title("GRU Prediction")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.show()


# Final Comparison


print("\n========== Final Comparison ==========")

print("RNN")
print("MAE :", rnn_mae)
print("RMSE:", rnn_rmse)

print()

print("LSTM")
print("MAE :", lstm_mae)
print("RMSE:", lstm_rmse)

print()

print("GRU")
print("MAE :", gru_mae)
print("RMSE:", gru_rmse)