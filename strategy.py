from indicators import calculate_indicators

def generate_signals(df):
    df = calculate_indicators(df)
    df['Signal'] = (df['RSI'] < 30) & (df['20DMA'] > df['50DMA'])
    return df

def backtest_strategy(df, signal_col='Signal', holding_period=5):
    trades = []
    for i in range(len(df)):
        if df[signal_col].iloc[i]:
            buy_price = df['Close'].iloc[i]
            sell_index = min(i + holding_period, len(df) - 1)
            sell_price = df['Close'].iloc[sell_index]
            profit = sell_price - buy_price
            trades.append(profit)
    if not trades:
        return {"trades": 0, "wins": 0, "losses": 0, "win_ratio": 0, "total_pnl": 0}
    wins = sum(1 for p in trades if p > 0)
    return {
        "trades": len(trades),
        "wins": wins,
        "losses": len(trades) - wins,
        "win_ratio": round(wins / len(trades), 2),
        "total_pnl": round(sum(trades), 2)
    }
