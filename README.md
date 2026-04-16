# AI Trading Bot

## Overview

This project is an automated trading system designed to execute trades based on predefined strategies, risk management rules, and continuous market monitoring.

The system is built to operate independently with minimal manual intervention while maintaining controlled risk exposure and consistent execution. It focuses on reliability, structured decision-making, and real-time responsiveness in a live trading environment.

---

## Project Structure

- `src/main.py` - Main bot loop, MT5 connection, order execution, and runtime monitoring
- `src/strategy.py` - Indicator calculations and signal generation logic (SMA, RSI)
- `src/config.py` - Centralized configuration for account settings, risk management, and trading parameters

---

## Features

- Automated trade execution based on technical indicators (SMA + RSI)
- Built-in risk management (stop loss, take profit, position control)
- Continuous execution loop with real-time market monitoring
- Trade state tracking (active positions, PnL visibility)
- Modular structure allowing easy expansion of strategies

---

## How It Works

1. Connects to MetaTrader 5 using account credentials
2. Pulls historical market data at defined intervals
3. Calculates indicators (SMA, RSI) using `pandas_ta`
4. Evaluates trade conditions based on strategy rules
5. Executes trades only if no active position exists
6. Continuously monitors open trades and market conditions

---

## Tech Stack

- Python
- MetaTrader5 API
- Pandas
- Pandas TA (technical analysis indicators)

---

## What I Learned

- Designing systems that run continuously without manual intervention
- Separating system components (execution, strategy, configuration)
- Handling edge cases such as failed connections and data retrieval issues
- Building structured logic for real-time decision-making systems

---

## Future Improvements

- Add backtesting engine for validating strategies against historical data
- Implement logging and monitoring for better observability
- Introduce multi-strategy support (scalping, trend-following, etc.)
- Integrate machine learning models for signal optimization
