# Plutus Project Template

Template repository of a Plutus Project.

This templte project sturcture also specifies how to store and structure the source code and report of a standard Plutus Project.

This `README.md` file serves as an example how a this will look like in a standard Plutus project. Below listed out the sample section.

## Abstract

This project implements a hybrid trading strategy on the VN30F1M futures index using the Simple Moving Average (SMA-100) and the Relative Strength Index (RSI-14). The strategy aims to capture mean-reversion signals that occur when RSI reaches extreme levels (overbought/oversold) against the prevailing SMA trend. We backtest the strategy using data from Algotrade, evaluating performance through returns, Sharpe ratio, and drawdown. Results suggest the approach can yield consistent returns under specific market conditions.

## 1. Introduction

Algorithmic trading has become an essential component of modern financial markets, allowing traders to implement and automate strategies based on well-defined rules and quantitative signals. Among the various classes of strategies, mean-reversion and momentum-based approaches are two fundamental techniques widely used by both retail and institutional traders.

This project focuses on applying a hybrid mean-reversion and momentum strategy to the VN30F1M futures index, one of the most liquid and volatile derivatives instruments in the Vietnamese market. The strategy is built on two core technical indicators:

- Simple Moving Average (SMA) with a 100-period window is used to capture the long-term trend direction.
- The Relative Strength Index (RSI) with a 14-period window is employed to identify short-term overbought and oversold conditions.

## 2. Related Work (or Background)

- Prerequisite reading if the audience needs knowledge before exploring the project.
- Optional

## 3. Trading (Algorithm) Hypotheses

When the Relative Strength Index (RSI) indicates oversold or overbought conditions and aligns with the broader trend confirmed by a slower-moving average, prices are likely to revert to their mean. This creates opportunities to trade counter to short-term extremes while respecting the dominant trend.

## 4. Data

---

- Data source: Algotrade Internship Database
- Data type: CSV
- Data period:
  - In-sample data: 2021-02-08 to 2023-12-22
  - Out-sample data: 2023-12-22 to 2025-03-19
- To get the input data:
  - Option 1: Download [data](https://drive.google.com/drive/folders/1bK3aXEVfabASZs2xV8VBXYA0mXjQtB-A?usp=sharing) from google drive, extract then files into `data` folder
  - Option 2: Use this script at project folder to get data from Algotrade:
  ```bash
  python -m src.data.loaddata()
  ```
- If you use option 2, `in_sample_data.csv` and `out_sample_data.csv` is stored at `data` folder

### Data collection

---

The price of VN30F1M are collected from Algotrade database using SQL queries, then was pre-processed and used for this project.

### Data processing

---

Raw data was first cleaned by removing all records before 9:00 AM. Timestamps were rounded down to the nearest minute, and only the first record of each minute was retained to reduce noise. Column names were standardized, keeping only the essential fields: timestamp, ticker symbol, and closing price. The final dataset was then split into two sets: In-sample (70%) and Out-sample (30%), ensuring there was no overlap in timestamps between the two sets.

## 🚀 Implementation Guide

Follow the steps below to get the project up and running locally.

---

### 1. Clone this Repository

```bash
git clone "https://github.com/thachnhb/group9.git"
```

### 2. Create Environment

#### 2.1. Move into the project directory

```bash
   cd <repo>
```

#### 2.2 Create the virtual environment

```bash
   python -m venv venv
```

#### 2.3 Activate the virtual environment (Kích hoạt môi trường ảo):

```bash
.\venv\Scripts\activate (For Windows)
```

or

```bash
source venv/bin/activate (For MacOS/Linux)
```

### 3. Install required libraries from requirement.txt

```bash
pip install -r requirements.txt
```

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
