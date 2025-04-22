# backtesting.py

from strategy import run_strategy
from evaluate import sharpe_ratio, maximum_drawdown
from data import load_data
from matplotlib import pyplot as plt

def run_backtest(data, params):
    """
    Chạy backtest với các tham số đã cho và hiển thị kết quả.
    
    Args:
        params (dict): Dictionary chứa các tham số tốt nhất từ quá trình optimize.
        data (DataFrame): Dataset để backtest.
    """
    final_asset, asset_over_time_df = run_strategy(data, **params)

    print("\nBacktesting Evaluation:")
    print(f"  Final Asset Value: {final_asset}")
    print(f"  Sharpe Ratio: {sharpe_ratio(asset_over_time_df):.4f}")
    print(f"  Maximum Drawdown: {maximum_drawdown(asset_over_time_df):.2f}%")

    # Vẽ biểu đồ tài sản theo thời gian
    asset_over_time_df.plot(kind='line', figsize=(10, 5), title="Asset Over Time (Backtest)")
    plt.ylabel("Asset Value")
    plt.xlabel("Date")
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Load data
    in_sample_df, out_sample_df = load_data()

    # best_params = {
    #     "sma_window": 200,
    #     "rsi_lower": 29.140662837219445,
    #     "rsi_upper": 65.00361398539523
    # }

    best_params = {
        "sma_window": 100,
        "rsi_lower": 25.0,
        "rsi_upper": 75.0
    }

    run_backtest(in_sample_df, best_params)
