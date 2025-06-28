
from data_ingestion import fetch_stock_data
from strategy import generate_signals, backtest_strategy
from ml_model import train_model
from sheets_logger import init_gsheet_connection, log_to_sheet
from telegram_alert import send_telegram_alert
import pandas as pd

#File names
tickers = ['INFY.NS', 'TCS.NS', 'HDFCBANK.NS'] #Stock names
sheet_name = 'TradingLog' #Exel Sheet name
json_key_file = 'your_key.json' #API key

# Replace with your actual bot token and chat ID, You can get this from botfather on telegram
bot_token = "XYZ" 
chat_id = 987654321

stock_data = {}
signals = {}
summary_data = []

for ticker in tickers:
    print(f"\nProcessing: {ticker}")
    df = fetch_stock_data(ticker)

    if df.empty:
        print(f"{ticker}: No data fetched. Skipping.")
        continue

    df = generate_signals(df.copy())
    stock_data[ticker] = df
    signals[ticker] = df

    try:
        acc = train_model(df.copy())
        print(f"{ticker}: Prediction Accuracy = {acc:.2f}")
    except Exception as e:
        print(f"{ticker}: ML training failed: {e}")

    try:
        latest = df.iloc[-1]
        if latest['Signal']:
            message = (
                f"BUY Signal for {ticker}\n"
                f"Close: ₹{latest['Close']:.2f}\n"
                f"RSI: {latest['RSI']:.2f}\n"
                f"20DMA: {latest['20DMA']:.2f} > 50DMA: {latest['50DMA']:.2f}"
            )
            send_telegram_alert(message, bot_token, chat_id)
            print(f"{ticker}: Telegram alert sent.")
    except Exception as e:
        print(f"{ticker}: Telegram alert failed: {e}")

try:
    sheet = init_gsheet_connection(json_key_file, sheet_name)
except Exception as e:
    print(f"Failed to connect to Google Sheet: {e}")
    sheet = None

if sheet:
    # --- Log recent signals to Google Sheet ---
    for ticker, df in signals.items():
        try:
            log_to_sheet(sheet, ticker, df[['Close', 'RSI', '20DMA', '50DMA', 'Signal']].tail(10))
            print(f"{ticker}: Logged recent signals to Google Sheet.")
        except Exception as e:
            print(f"{ticker}:  Failed to log to sheet: {e}")

    for ticker, df in signals.items():
        try:
            result = backtest_strategy(df)
            summary_data.append([
                ticker, result['trades'], result['wins'],
                result['losses'], result['win_ratio'], result['total_pnl']
            ])
            print(f"{ticker}: Backtest complete.")
        except Exception as e:
            print(f"{ticker}: Backtest failed: {e}")

    if summary_data:
        summary_df = pd.DataFrame(summary_data, columns=["Stock", "Trades", "Wins", "Losses", "Win Ratio", "Total P&L"])
        try:
            log_to_sheet(sheet, "Backtest Summary", summary_df)
            print("Backtest Summary logged.")
        except Exception as e:
            print(f"Failed to log backtest summary: {e}")
    else:
        print("No summary data to log.")
