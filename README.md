# Plutus Project Template

Template repository of a Plutus Project.

This templte project sturcture also specifies how to store and structure the source code and report of a standard Plutus Project.

This `README.md` file serves as an example how a this will look like in a standard Plutus project. Below listed out the sample section.

## Abstract

This project presents the design, implementation, and evaluation of a hybrid trading strategy tailored for the VN30F1M futures index. The strategy combines two widely recognized technical indicators: the 100-period Simple Moving Average (SMA-100) and the 14-period Relative Strength Index (RSI-14). By integrating the concepts of trend-following and mean-reversion, the strategy seeks to exploit temporary mispricings in the market. Specifically, it generates trading signals when the RSI reaches extreme levels—indicating overbought or oversold conditions—relative to the direction of the SMA-defined trend. These entry signals are then evaluated for profitability within the broader context of the prevailing market regime. We utilize historical price data provided by Algotrade to backtest the strategy across multiple timeframes and market conditions. Key performance metrics, including cumulative returns, Sharpe ratio, and maximum drawdown, are used to assess robustness and risk-adjusted performance. The results indicate that the hybrid approach holds potential for consistent profitability, particularly during trending but volatile market phases, underscoring the value of blending momentum and reversal signals in systematic trading.

## Introduction

In recent years, algorithmic trading has revolutionized financial markets by enabling systematic, rule-based decision-making that minimizes human emotion and error. These algorithms can process vast amounts of market data in real time and execute trades based on predefined strategies, significantly improving efficiency and consistency in trading operations. Two of the most commonly used strategies in this domain are momentum strategies, which follow the direction of existing trends, and mean-reversion strategies, which capitalize on the tendency of prices to revert to their historical average after reaching extreme levels.

This project explores a hybrid approach that synthesizes both strategy types, focusing on the VN30F1M futures contract—a key derivative instrument tied to the VN30 Index, which tracks the 30 largest and most liquid stocks on the Ho Chi Minh Stock Exchange. The VN30F1M is known for its high trading volume and price volatility, making it an ideal candidate for technical-based trading strategies.

The foundation of the hybrid strategy lies in the use of two technical indicators:

The Simple Moving Average (SMA) with a 100-period window serves as a proxy for long-term market trend direction, helping to identify whether the overall sentiment is bullish or bearish.

The Relative Strength Index (RSI) with a 14-period window is used to detect short-term momentum extremes. When RSI values cross certain thresholds—typically above 70 for overbought and below 30 for oversold conditions—they may signal potential turning points in price action.

By aligning RSI signals with the direction suggested by the SMA, the strategy aims to enter trades with higher probability setups, favoring mean-reversion trades that are in harmony with the broader trend. This hybrid structure is designed to reduce false signals and improve trade timing, which are common challenges in purely mean-reversion or momentum-based systems.

## Related Work (or Background)

- Prerequisite reading if the audience needs knowledge before exploring the project.
- Optional

## Trading (Algorithm) Hypotheses

When the Relative Strength Index (RSI) indicates oversold or overbought conditions and aligns with the broader trend confirmed by a slower-moving average, prices are likely to revert to their mean. This creates opportunities to trade counter to short-term extremes while respecting the dominant trend.

## Data

- Data source: Algotrade Internship Database
- Data type: CSV
- Data period:
- How to get the input data?
- How to store the output data?

### Data collection

- Step 2 of the Nine-Step

### Data Processing

- Step 3 of the Nine-Step

## 🚀 Implementation Guide

Follow the steps below to get the project up and running locally.  
Make sure you have **Python 3.x** installed.

---

### 🔧 1. Clone the Repository

```bash
git clone "https://github.com/your-username/your-repo.git"
```
### ⚙️ 2. Create Environment
```bash
1. Move into the project directory
- cd <repo>

2. Create the virtual environment
python -m venv venv
# or
python3 -m venv venv

3. Activate the virtual environment (Kích hoạt môi trường ảo):

🪟 Windows
.\venv\Scripts\activate

🍎 MacOS / 🐧 Linux
source venv/bin/activate
```


## In-sample Backtesting
- Describe the In-sample Backtesting step
  - ## Parameters

| Parameter    | Description                      | Default Value  |
|--------------|----------------------------------|----------------|
| sma_window   | calculate a Simple Moving Average| 120            |
| rsi_lower    | The buy threshold                | 28             |
| rsi_upper    | The sell thresold                | 72             |

- Step 4 of the Nine-Step

### In-sample Backtesting Result

- ![In-sample Backtesting Result](./graph/backtest_InSample/asset_overtime.png)

## Optimization

- 🔍 Optimization Step
The project uses Optuna — an automatic hyperparameter optimization framework — to find the best combination of trading strategy parameters that maximize returns.

- 💡 Optimization Method
The optimization uses Optuna's TPE Sampler (Tree-structured Parzen Estimator).

The goal is to maximize the final asset value at the end of the trading period.

The process automatically explores parameter combinations and records their performance, helping find the most profitable strategy.


### 🧮 Parameters to Optimize
| Parameter    | Description                      | Search space               |
|--------------|----------------------------------|----------------------------|
| sma_window   | calculate a Simple Moving Average| Integer from `50` to `200` |
| rsi_lower    | The buy threshold                | Float from `20.0` to `35.0`|
| rsi_upper    | The sell thresold                | Float from `65.0` to `80.0`|

### ⚙️ Hyperparameters of the Optimization Process

| Hyperparameter  | Description                                                    | Value                   |
|-----------------|--------------------------------------------------------------- |-------------------------|
| `n_trials`      | Number of optimization trials to explore parameter combinations| `80` (default in script)|
| `seed`          | Random seed for reproducibility of results.                    | `710` (used in example) |
| `sampler`       | Sampling algorithm used to suggest new parameter values.       | `TPESampler`            |



### In-sample Optimization Result

- ![Optimization Result](./graph/optimization_insample/asset_over_time_optimized.png)

### Out-sample Optimization Resut

- ![Optimization Result](./graph/optimization_outsample/asset_over_time.png)

## Out-of-sample Backtesting

| Parameter    | Description                      | Default Value     |
|--------------|----------------------------------|-------------------|
| sma_window   | calculate a Simple Moving Average| 200               |
| rsi_lower    | The buy threshold                | 29.140662837219445|
| rsi_upper    | The sell thresold                | 65.00361398539523 |

### Out-of-sample Backtesting Reuslt

- ![In-sample Backtesting Result](./graph/backtest_OutSample/Asset_Over_Time.png)

## Paper Trading

- Describe the Paper Trading step
- Step 7 of the Nine-Step
- Optional

### Optimization Result

- Brieftly shown the result: table, image, etc.
- Has link to the Paper Trading Report

## Conclusion:

- The backtesting results reveal a significant discrepancy between the in-sample and out-sample performance of the strategy, despite using the same optimized parameters. While the in-sample phase showed strong profit growth, the out-sample test suffered from both negative returns and high drawdowns, suggesting potential overfitting to historical data rather than genuine robustness.

- Additionally, during further testing with conventional parameters (SMA window = 100, RSI 30/70), the asset curve flattened for a large part of the period. This indicates that the strategy’s signal conditions were either too restrictive or the market conditions did not trigger any trades for extended periods. Such behavior highlights that the strategy's logic may have low adaptability and high sensitivity to parameter settings, especially in varying market environments.

- In summary, the current algorithm exhibits signs of overfitting and structural fragility. Further review is recommended to:

- Reconsider entry/exit rules to avoid dead zones.

- Allow more dynamic thresholds.

- Add market regime detection or parameter stability testing before deployment.

## Reference

- All the reference goes here.

## Other information

- Link to the Final Report (Paper) should be somewhere in the `README.md` file.
- Please make sure this file is relatively easy to follow.
