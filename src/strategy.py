import pandas as pd
import pandas_ta as ta


def prepare_market_data(bars, sma_length, rsi_length):
    df = pd.DataFrame(bars)
    df["SMA50"] = ta.sma(df["close"], length=sma_length)
    df["RSI"] = ta.rsi(df["close"], length=rsi_length)
    return df


def get_latest_signal(df):
    curr_price = df["close"].iloc[-1]
    curr_sma = df["SMA50"].iloc[-1]
    curr_rsi = df["RSI"].iloc[-1]

    return {
        "price": curr_price,
        "sma": curr_sma,
        "rsi": curr_rsi,
        "buy_signal": curr_price < curr_sma and curr_rsi < 30,
    }
