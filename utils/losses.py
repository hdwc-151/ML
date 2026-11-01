import numpy as np

class Loss:
    """Lớp cơ sở trừu tượng cho tất cả các hàm mất mát."""
    def forward(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        raise NotImplementedError
        
    def backward(self, y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        raise NotImplementedError

class MeanSquaredError(Loss):
    """
    Mean Squared Error (MSE): L = (1 / 2m) * ||y_true - y_pred||^2
    Hệ số 1/2 giúp triệt tiêu số 2 khi tính đạo hàm.
    """
    def forward(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        y_true = np.asarray(y_true).reshape(-1, 1)
        y_pred = np.asarray(y_pred).reshape(-1, 1)
        return float(0.5 * np.mean((y_true - y_pred) ** 2))
        
    def backward(self, y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        """Đạo hàm riêng theo y_pred: dL/d(y_pred) = (1 / m) * (y_pred - y_true)"""
        y_true = np.asarray(y_true).reshape(-1, 1)
        y_pred = np.asarray(y_pred).reshape(-1, 1)
        m = y_true.shape[0]
        return (y_pred - y_true) / m

class BinaryCrossEntropy(Loss):
    """
    Binary Cross-Entropy Loss (Log Loss):
    L = - (1 / m) * sum(y * log(p) + (1 - y) * log(1 - p))
    """
    def __init__(self, eps: float = 1e-15):
        self.eps = eps

    def forward(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        y_true = np.asarray(y_true).reshape(-1, 1)
        y_pred = np.asarray(y_pred).reshape(-1, 1)
        # Giới hạn xác suất tránh lỗi log(0)
        p = np.clip(y_pred, self.eps, 1.0 - self.eps)
        return float(-np.mean(y_true * np.log(p) + (1.0 - y_true) * np.log(1.0 - p)))
        
    def backward(self, y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        y_true = np.asarray(y_true).reshape(-1, 1)
        y_pred = np.asarray(y_pred).reshape(-1, 1)
        p = np.clip(y_pred, self.eps, 1.0 - self.eps)
        m = y_true.shape[0]
        return ((p - y_true) / (p * (1.0 - p))) / m