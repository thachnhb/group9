# backtesting.py

from strategy import run_strategy
from evaluate import sharpe_ratio, maximum_drawdown
from data import load_data
from matplotlib import pyplot as plt

def run_backtest(params, data):
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

    # Ví dụ giả định về tham số tốt nhất, bạn nên thay bằng tham số thực tế từ optimize
    best_params = {
        "sma_window": 120,
        "rsi_lower": 28.0,
        "rsi_upper": 72.0
    }

    run_backtest(best_params, out_sample_df)
