import numpy as np

def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Hệ số xác định R²: 1 - (SS_res / SS_tot)"""
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return float(1.0 - (ss_res / ss_tot)) if ss_tot != 0 else 0.0

def root_mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """RMSE = sqrt(mean((y_true - y_pred)^2))"""
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))

def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Tỷ lệ phân loại chính xác: count(y_true == y_pred) / N"""
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()
    return float(np.mean(y_true == y_pred))