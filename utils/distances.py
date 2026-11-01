import numpy as np

def euclidean_distance_matrix(X: np.ndarray, Z: np.ndarray) -> np.ndarray:
    """
    Tính ma trận khoảng cách Euclid giữa mọi cặp điểm trong X (N, d) và Z (M, d)
    Dựa trên khai triển: ||x_i - z_j||^2 = ||x_i||^2 + ||z_j||^2 - 2 * x_i^T * z_j
    """
    X2 = np.sum(X ** 2, axis=1, keepdims=True)    # Shape: (N, 1)
    Z2 = np.sum(Z ** 2, axis=1, keepdims=True).T  # Shape: (1, M)
    distances_squared = X2 + Z2 - 2.0 * np.dot(X, Z.T)
    # Khử sai số số học làm xuất hiện các giá trị âm rất nhỏ (-1e-16)
    return np.sqrt(np.maximum(0.0, distances_squared))