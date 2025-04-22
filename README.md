# Plutus Project Template

Template repository of a Plutus Project.

This templte project sturcture also specifies how to store and structure the source code and report of a standard Plutus Project.

This `README.md` file serves as an example how a this will look like in a standard Plutus project. Below listed out the sample section.

## Abstract

This project implements a hybrid trading strategy on the VN30F1M futures index using the Simple Moving Average (SMA-100) and the Relative Strength Index (RSI-14). The strategy aims to capture mean-reversion signals that occur when RSI reaches extreme levels (overbought/oversold) against the prevailing SMA trend. We backtest the strategy using data from Algotrade, evaluating performance through returns, Sharpe ratio, and drawdown. Results suggest the approach can yield consistent returns under specific market conditions.

## Introduction

Algorithmic trading has become an essential component of modern financial markets, allowing traders to implement and automate strategies based on well-defined rules and quantitative signals. Among the various classes of strategies, mean-reversion and momentum-based approaches are two fundamental techniques widely used by both retail and institutional traders.

This project focuses on applying a hybrid mean-reversion and momentum strategy to the VN30F1M futures index, one of the most liquid and volatile derivatives instruments in the Vietnamese market. The strategy is built on two core technical indicators:

- Simple Moving Average (SMA) with a 100-period window is used to capture the long-term trend direction.
- The Relative Strength Index (RSI) with a 14-period window is employed to identify short-term overbought and oversold conditions.

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

⚙️ 2. Create Environment
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


## In-sample Backtesting

- Describe the In-sample Backtesting step
  - Parameters
  - Data
- Step 4 of the Nine-Step

### In-sample Backtesting Result

- Brieftly shown the result: table, image, etc.
- Has link to the In-sample Backtesting Report

## Optimization

- Describe the Optimization step
  - Optimization process/methods/library
  - Parameters to optimize
  - Hyper-parameter of the optimize process
- Step 5 of the Nine-Step

### Optimization Result

- Brieftly shown the result: table, image, etc.
- Has link to the Optimization Report

## Out-of-sample Backtesting

- Describe the Out-of-sample Backtesting step
  - Parameter
  - Data
- Step 6 of th Nine-Step

### Out-of-sample Backtesting Reuslt

- Brieftly shown the result: table, image, etc.
- Has link to the Out-of-sample Backtesting Report

## Paper Trading

- Describe the Paper Trading step
- Step 7 of the Nine-Step
- Optional

### Optimization Result

- Brieftly shown the result: table, image, etc.
- Has link to the Paper Trading Report

## Conclusion

- What is the conclusion?
- Optional

## Reference

- All the reference goes here.

## Other information

- Link to the Final Report (Paper) should be somewhere in the `README.md` file.
- Please make sure this file is relatively easy to follow.
