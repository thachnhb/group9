import numpy as np
import pandas as pd

def compute_rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_sharpe_minute(
    returns: pd.Series,
    risk_free_rate: float = 0.03,
    minutes_per_day: int = 225,
    days_per_year: int = 252
) -> float:
    minutes_per_year = minutes_per_day * days_per_year
    excess_return = returns.mean() - (risk_free_rate / minutes_per_year)
    annual_return = excess_return * minutes_per_year
    annual_std = returns.std() * np.sqrt(minutes_per_year)
    return annual_return / annual_std

def sharpe_ratio(asset_df: pd.DataFrame) -> float:
    returns = asset_df['Asset'].pct_change().dropna()
    return calculate_sharpe_minute(returns)

def maximum_drawdown(asset_df: pd.DataFrame) -> float:
    peak = asset_df['Asset'].cummax()
    drawdown = asset_df['Asset'] / peak - 1
    return drawdown.min() * 100

def holding_period_return(asset_df: pd.DataFrame) -> float:
    initial = asset_df['Asset'].iloc[0]
    final = asset_df['Asset'].iloc[-1]
    return (final - initial) / initial
