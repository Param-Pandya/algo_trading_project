
# 📈 Algo-Trading System with ML, Google Sheets & Telegram Automation

This is a modular, Python-based mini **algo-trading system** that uses technical indicators and machine learning to generate buy signals, backtest strategies, log results to Google Sheets, and send real-time alerts via Telegram.

---

## 🧠 Features

✅ Fetches **6 months of daily stock data** (using Yahoo Finance)  
✅ Implements **RSI < 30** + **20-DMA > 50-DMA** crossover strategy  
✅ Trains a **Logistic Regression model** to predict next-day movement  
✅ Performs **backtesting** to calculate trades, win ratio, and P&L  
✅ Logs trades and summaries into a **Google Sheet (via service account)**  
✅ Sends **Telegram alerts** when a buy signal is detected  
✅ Modular, robust, and production-ready

---

## 🛠️ Tech Stack

- Python 3.8+
- [yfinance](https://pypi.org/project/yfinance/) – Stock data
- [pandas](https://pandas.pydata.org/) – Data manipulation
- [scikit-learn](https://scikit-learn.org/) – ML model
- [gspread](https://docs.gspread.org/) – Google Sheets API
- [oauth2client](https://pypi.org/project/oauth2client/) – Auth for Google
- [requests](https://pypi.org/project/requests/) – Telegram API

---

## 📁 Project Structure

```
algo_trading_project/
├── main.py                    # Main controller script
├── data_ingestion.py          # Fetches stock data from yfinance
├── strategy.py                # Contains RSI strategy + backtesting
├── ml_model.py                # Machine Learning model (Logistic Regression)
├── sheets_logger.py           # Logs to Google Sheets using gspread
├── telegram_alert.py          # Sends Telegram alerts for buy signals
├── requirements.txt           # Dependency list
└── service_account_key.json   # Google Sheets API key (You have to add yours)
```

---

## ⚙️ Setup Instructions

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. 🔑 Google Sheets Setup

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a project → Enable:
  - Google Sheets API
  - Google Drive API
- Create a **service account** → Generate JSON key → Save as `service_account_key.json`
- Share your Google Sheet (e.g., `TradingLog`) with the **service account email**

### 3. 🤖 Telegram Bot Setup

- Talk to [@BotFather](https://t.me/botfather) → `/newbot`
- Save the token provided (looks like `123456789:ABC...`)
- Send a message to your bot
- Visit this URL to get your `chat_id`:
  ```
  https://api.telegram.org/bot<your-token>/getUpdates
  ```

---

## 🔄 How It Works

1. `main.py` fetches historical data for each stock
2. Applies the RSI and DMA strategy
3. Trains an ML model (Logistic Regression) on RSI, MACD, and Volume
4. Logs trades and predictions into Google Sheets
5. Sends a Telegram alert when a buy signal is detected
6. Backtests the strategy over 6 months and logs performance


---
## ▶️ How to Run

```bash
python main.py
```

Expected Output:
- Prints prediction accuracy for each stock
- Sends Telegram alerts if any buy signals are detected
- Logs signals and backtest summary to Google Sheet

---

## 📊 Trading Strategy

- **Buy Signal:**  
  - RSI < 30  
  - AND 20-DMA > 50-DMA

- **Backtest Simulation:**  
  - Buy and hold for 5 days  
  - Track profit/loss  
  - Logs total trades, wins, losses, win ratio, and cumulative P&L

---

## 💡 Sample Telegram Alert

```
📈 BUY Signal for TCS.NS
Close: ₹3540.00
RSI: 28.21
20DMA: 3555.32 > 50DMA: 3531.88
```

---

## ✅ Example Google Sheet Tabs

- `INFY.NS` → Recent 10 signals  
- `TCS.NS` → Recent 10 signals  
- `Backtest Summary` → Summary of trades, wins, P&L

---

## 🙋‍♂️ Author

- 👨‍💻 Built by: Param Pandya
- 🎓 For: Algo-Trading + ML Automation Assignment