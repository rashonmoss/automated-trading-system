import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta
import time
import winsound

# 1. ADD YOUR KEYS HERE
account_id = 5047062035      # Your MT5 Login ID
password = "_dHa0rSq"   # Your MT5 Password
server = "MetaQuotes-Demo" # Your Server Name

# 2. Update the initialization to USE those keys
if not mt5.initialize(login=account_id, password=password, server=server):
    print(f"❌ Connection Failed! Error: {mt5.last_error()}")
    quit()

print("✅ Sniper Bot Logged In and Stalking...")

pair = "EURUSD"
lot_size = 0.1  # 0.1 = $1 per pip approx.
magic_number = 123456 # Unique ID for your bot's trades

def place_buy_order():
    price = mt5.symbol_info_tick(pair).ask
    point = mt5.symbol_info(pair).point
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": pair,
        "volume": lot_size,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": price - (200 * point), # Stop Loss: 20 pips away
        "tp": price + (400 * point), # Take Profit: 40 pips away
        "magic": magic_number,
        "comment": "Stalker Bot Entry",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print("🚀 TRADE PLACED SUCCESSFULLY!")
    else:
        print(f"❌ TRADE FAILED. Error: {result.comment}")

while True:
    # 1. Fetch market data
    bars = mt5.copy_rates_from_pos(pair, mt5.TIMEFRAME_H1, 0, 100)
    df = pd.DataFrame(bars)
    df['SMA50'] = ta.sma(df['close'], length=50)
    df['RSI'] = ta.rsi(df['close'], length=14)
    
    curr_price = df['close'].iloc[-1]
    curr_sma = df['SMA50'].iloc[-1]
    curr_rsi = df['RSI'].iloc[-1]

    # 2. THE DASHBOARD: Check for open trades
    positions = mt5.positions_get(symbol=pair)
    
    print("-" * 40)
    print(f"STALKING: {pair} | Price: {curr_price:.5f}")
    print(f"INDICATORS: SMA50: {curr_sma:.5f} | RSI: {curr_rsi:.2f}")

    if len(positions) > 0:
        # We have an active trade!
        pos = positions[0] # Get the first open trade
        pnl = pos.profit
        print(f"🎯 ACTIVE TRADE: Ticket #{pos.ticket} | PnL: ${pnl:.2f}")
    else:
        print("💡 STATUS: Looking for entry...")

    # 3. Trading Logic (Same as before)
    if curr_price < curr_sma and curr_rsi < 30:
        if len(positions) == 0:
            place_buy_order()
    
    print("-" * 40)
    time.sleep(60)
