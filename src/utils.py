# utils.py

import matplotlib.pyplot as plt
from optuna.visualization import (
    plot_optimization_history,
    plot_parallel_coordinate,
    plot_contour,
    plot_slice,
    plot_param_importances
)

def plot_all_optuna(study):
    """
    Hàm này vẽ các biểu đồ đánh giá tối ưu hóa từ Optuna.
    """
    # Biểu đồ quá trình tối ưu hóa
    plot_optimization_history(study).show()

    # Biểu đồ biểu diễn các tham số trong quá trình tối ưu hóa
    plot_parallel_coordinate(study).show()

    # Biểu đồ Contour để thấy sự tương quan giữa các tham số
    plot_contour(study).show()

    # Biểu đồ phân đoạn của quá trình tối ưu hóa
    plot_slice(study).show()

    # Biểu đồ quan trọng của các tham số
    plot_param_importances(study).show()
