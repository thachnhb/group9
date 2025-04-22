# Strategy.py
import numpy as np
import pandas as pd
from src.evaluate import compute_rsi

# Constants
MARGIN_RATIO = 0.175
ACCOUNT_RATIO = 0.8
CONTRACT_MULTIPLIER = 100000
TRANSACTION_FEE_POINT = 0.47
initial_asset_value = 40000000

def run_strategy(data: pd.DataFrame, sma_window: int, rsi_lower: float, rsi_upper: float):
    df = data.copy()
    SMA_SYMBOL = f'SMA{sma_window}'
    df[SMA_SYMBOL] = df['Close'].rolling(window=sma_window).mean()
    df['RSI'] = compute_rsi(df['Close'], 14)

    asset_value = initial_asset_value
    holdings = []
    df['Asset'] = np.nan

    contract_margin = CONTRACT_MULTIPLIER * MARGIN_RATIO
    required_deposit = contract_margin / ACCOUNT_RATIO

    prev_date = None

    for date in df.index:
        if prev_date is None:
            prev_date = date
            continue

        cur_price = float(df.loc[date, "Close"])
        current_sma = float(df.loc[date, SMA_SYMBOL])
        current_rsi = float(df.loc[date, "RSI"])

        total_realized_pnl = 0

        for pos in holdings.copy():
            position_type, entry_point = pos
            if position_type == "LONG":
                if (current_rsi > 40) or (cur_price <= current_sma) or (cur_price < entry_point * (1 - 0.015)):
                    pnl = cur_price - entry_point - TRANSACTION_FEE_POINT
                    total_realized_pnl += (pnl * CONTRACT_MULTIPLIER) / contract_margin
                    holdings.remove(pos)
            elif position_type == "SHORT":
                if (current_rsi < 60) or (cur_price >= current_sma) or (cur_price > entry_point * (1 + 0.015)):
                    pnl = entry_point - cur_price - TRANSACTION_FEE_POINT
                    total_realized_pnl += (pnl * CONTRACT_MULTIPLIER) / contract_margin
                    holdings.remove(pos)

        asset_value += total_realized_pnl * contract_margin
        df.loc[date, "Asset"] = asset_value

        if not holdings:
            if (asset_value >= cur_price * required_deposit):
                if (current_rsi < rsi_lower) and (cur_price > current_sma):
                    holdings.append(["LONG", cur_price])
                elif (current_rsi > rsi_upper) and (cur_price < current_sma):
                    holdings.append(["SHORT", cur_price])

        prev_date = date

    df = df[df["Asset"].notna()]
    final_asset_value = df["Asset"].iloc[-1] if not df.empty else initial_asset_value
    return final_asset_value, df
