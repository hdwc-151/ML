import numpy as np

class StandardScaler:
    """Chuẩn hóa dữ liệu về phân phối có trung bình bằng 0 và phương sai bằng 1."""
    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, X: np.ndarray):
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        # Tránh chia cho 0 nếu một cột đặc trưng là hằng số
        self.std[self.std == 0.0] = 1.0
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        return (X - self.mean) / self.std

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.fit(X).transform(X)

def train_test_split(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, random_state: int = None):
    """Phân tách tập dữ liệu thành train set và test set."""
    if random_state is not None:
        np.random.seed(random_state)
    m = X.shape[0]
    indices = np.random.permutation(m)
    test_count = int(m * test_size)
    test_idx = indices[:test_count]
    train_idx = indices[test_count:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

class PolynomialFeatures:
    """Tạo đặc trưng đa thức lên đến bậc degree."""
    def __init__(self, degree: int = 2):
        self.degree = degree

    def fit(self, X: np.ndarray):
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        # Chỉ tạo các bậc từ 1 đến degree (Bậc 0 sẽ do tham số fit_intercept của Model tự xử lý)
        features = [X ** i for i in range(1, self.degree + 1)]
        return np.hstack(features)

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        return self.transform(X)