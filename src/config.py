import MetaTrader5 as mt5

# Broker / MT5 configuration
ACCOUNT_ID = 000000
PASSWORD = "000000"
SERVER = "ABCDEFG"

# Trading configuration
PAIR = "EURUSD"
LOT_SIZE = 0.1
MAGIC_NUMBER = 123456

# Risk / indicator settings
TIMEFRAME = mt5.TIMEFRAME_H1
BAR_COUNT = 100
SMA_LENGTH = 50
RSI_LENGTH = 14

# Trade parameters
STOP_LOSS_POINTS = 200
TAKE_PROFIT_POINTS = 400

# Loop timing
SLEEP_SECONDS = 60
