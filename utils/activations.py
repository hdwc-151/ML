import numpy as np

def sigmoid(z: np.ndarray) -> np.ndarray:
    """Hàm Sigmoid: 1 / (1 + exp(-z)), ổn định số học tránh tràn số exp."""
    z_safe = np.clip(z, -500, 500)
    return 1.0 / (1.0 + np.exp(-z_safe))

def sigmoid_derivative(z: np.ndarray) -> np.ndarray:
    """Đạo hàm của Sigmoid: s'(z) = s(z) * (1 - s(z))"""
    s = sigmoid(z)
    return s * (1.0 - s)

def relu(z: np.ndarray) -> np.ndarray:
    """Hàm ReLU: max(0, z)"""
    return np.maximum(0.0, z)

def relu_derivative(z: np.ndarray) -> np.ndarray:
    """Đạo hàm của ReLU: 1 nếu z > 0, ngược lại bằng 0"""
    return (z > 0).astype(float)

def softmax(z: np.ndarray) -> np.ndarray:
    """Hàm Softmax với kỹ thuật trừ max để chống tràn số float."""
    z_shifted = z - np.max(z, axis=-1, keepdims=True)
    exp_z = np.exp(z_shifted)
    return exp_z / np.sum(exp_z, axis=-1, keepdims=True)