# AI Trading Bot

## Overview

This project is an automated trading bot designed to execute trades based on predefined strategies, risk management rules, and continuous market monitoring. The goal was to build a system that can operate independently with minimal manual intervention while maintaining controlled risk exposure.

## Project Structure

- `src/main.py` - Main bot loop, MT5 connection, order execution, and dashboard output
- `src/strategy.py` - Indicator calculations and signal generation logic
- `src/config.py` - Trading, account, and risk configuration settings

## Features

* Automated trade execution based on strategy signals
* Risk management with stop loss and max daily loss thresholds
* Continuous monitoring and re-entry logic after trade completion
* Scalable structure for adding new strategies (scalping, trend-based)

## Tech Stack

* Python (core logic)
* API integration (broker / market data)
* Basic data analysis and signal processing

## What I Learned

* Designing systems that run continuously without manual intervention
* Handling edge cases like failed trades and reconnections
* Structuring logic for reliability and repeatability in real-time environments

## Future Improvements

* Add backtesting engine for strategy validation
* Implement logging and performance tracking dashboard
* Integrate machine learning models for signal optimization
