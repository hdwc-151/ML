# Machine Learning From Scratch

**Hiểu toán học · Tự triển khai thuật toán · Kiểm chứng bằng thực nghiệm**

[🇻🇳 Tiếng Việt](README.md) · [🇬🇧 English](README.en.md) · [🇨🇳 简体中文](README.zh-CN.md)

Dự án học tập và thực nghiệm về **Machine Learning (ML)** và nền tảng **Deep Learning (DL)**, kết hợp suy luận toán học, triển khai bằng Python/NumPy, trực quan hóa và đối chiếu với thư viện tham chiếu.

> **Trạng thái:** Dự án giáo dục đang phát triển. Nội dung hiện gồm notebook học tập và một số tiện ích dùng chung. Độ hoàn thiện, tính ổn định API và khả năng tái lập khác nhau theo chủ đề. Đây chưa phải framework ML dùng trong production.

## Khám phá

- **[Đọc sách trực tuyến (Jupyter Book)](https://hdwc-151.github.io/ML/)** — trạng thái website phụ thuộc triển khai GitHub Pages.
- [Kho notebook](algorithms/notebooks)
- [Tiện ích dùng chung](utils)
- [Báo lỗi / đề xuất](https://github.com/hdwc-151/ML/issues)

## Phương pháp học

1. **Hiểu bài toán:** mục tiêu, giả định, ký hiệu và phạm vi áp dụng.
2. **Suy luận toán học:** hàm mục tiêu, công thức và logic tối ưu.
3. **Tự triển khai:** chuyển phép suy luận thành mã Python/NumPy dễ đọc.
4. **Thực nghiệm:** trực quan hóa, thay đổi tham số, khảo sát trường hợp biên.
5. **Kiểm chứng:** đối chiếu có chủ đích với tài liệu hoặc thư viện như scikit-learn.

“From scratch” là phương pháp học, không tự động đảm bảo đúng, tối ưu hay ổn định. So sánh chỉ có ý nghĩa khi giả định, dữ liệu, cách đánh giá và dung sai tương thích.

## Lộ trình nội dung

| Phần | Chủ đề | Notebook |
|---|---|---|
| 00 · Nền tảng | Đại số tuyến tính, giải tích, xác suất, MLE/MAP | [Mở](algorithms/notebooks/00_foundations) |
| 01 · Hồi quy | Normal equation, gradient descent, polynomial, Ridge/Lasso/Elastic Net | [Mở](algorithms/notebooks/01_regression) |
| 02 · Phân loại | Perceptron, logistic/softmax regression, SVM | [Mở](algorithms/notebooks/02_classification) |
| 03 · Lân cận & Bayes | KNN, Gaussian và Multinomial Naive Bayes | [Mở](algorithms/notebooks/03_instance_bayes) |
| 04 · Cây & tổ hợp | Decision trees, random forest, AdaBoost, gradient boosting | [Mở](algorithms/notebooks/04_trees_ensembles) |
| 05 · Không giám sát | K-means, clustering, DBSCAN, PCA/SVD, GMM/EM | [Mở](algorithms/notebooks/05_unsupervised) |
| 06 · Mạng nơ-ron | Computational graph, backpropagation, MLP, optimizer | [Mở](algorithms/notebooks/06_neural_networks) |

**Phạm vi:** Bảng mô tả chủ đề trong notebook, không khẳng định mọi thuật toán đã thành estimator hoàn chỉnh trong package.

## Cấu trúc repository

~~~text
ML/
├── algorithms/notebooks/
│   ├── 00_foundations/
│   ├── 01_regression/
│   ├── 02_classification/
│   ├── 03_instance_bayes/
│   ├── 04_trees_ensembles/
│   ├── 05_unsupervised/
│   └── 06_neural_networks/
├── utils/
│   ├── __init__.py
│   ├── activations.py
│   ├── distances.py
│   ├── losses.py
│   ├── metrics.py
│   └── preprocessing.py
├── .github/workflows/deploy.yml
├── _config.yml
├── _toc.yml
├── intro.md
├── pyproject.toml
├── requirements.txt
├── README.md
├── README.en.md
└── README.zh-CN.md
~~~

Sơ đồ lược bỏ artifact sinh tự động, bytecode và notebook cache.

## Bắt đầu

### Yêu cầu
- Python **3.9+** theo metadata dự án.
- Conda hoặc Python venv.
- Git và kết nối Internet để cài thư viện.

CI hiện dùng Python 3.11; khuyến nghị dùng cùng phiên bản.

### 1. Clone

~~~bash
git clone https://github.com/hdwc-151/ML.git
cd ML
~~~

### 2. Tạo môi trường

**Conda:**

~~~bash
conda create -n ml-from-scratch python=3.11 -y
conda activate ml-from-scratch
~~~

**Hoặc venv:**

~~~bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
~~~

### 3. Cài đặt

~~~bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements.txt
~~~

Metadata khai báo NumPy, Matplotlib, scikit-learn; requirements bổ sung Jupyter Book. Dependency chưa được khóa phiên bản đầy đủ, nên chưa đảm bảo tái lập tuyệt đối.

### 4. Chạy notebook

~~~bash
jupyter notebook
~~~

Mở notebook trong thư mục algorithms/notebooks. Nếu dùng JupyterLab:

~~~bash
python -m pip install jupyterlab
jupyter lab
~~~

### 5. Kiểm tra utility

~~~python
import utils
print(utils.__all__)
~~~

Các tiện ích hiện cung cấp một số hàm activation, loss, metric, khoảng cách và preprocessing. Xem [utils/__init__.py](utils/__init__.py) và từng module để biết API chính xác.

## Tái lập và kiểm chứng

- Chạy notebook theo thứ tự trong kernel mới.
- Ghi phiên bản thư viện, random seed và nguồn dữ liệu khi phù hợp.
- Chia dữ liệu trước khi fit preprocessing; chỉ fit transform trên tập train.
- Kiểm tra shape, ổn định số, trường hợp biên và hội tụ.
- So sánh với triển khai độc lập khi giả định và dung sai tương thích.
- Không commit dữ liệu lớn, checkpoint, credential hoặc file môi trường cá nhân.

**Khoảng trống:** Chưa có bộ automated test toàn diện và environment lockfile đầy đủ. Cài package thành công không chứng minh thuật toán đúng hay notebook tái lập.

## Đóng góp

1. Tạo nhánh riêng cho thay đổi có phạm vi rõ.
2. Giữ diff gọn, giải thích mục đích và cơ sở toán học.
3. Chạy notebook liên quan từ kernel sạch, kiểm thử utility đã đổi.
4. Mô tả tác động, giả định và giới hạn trong pull request.

Smoke checks:

~~~bash
python -m pip check
python -c "import utils; print('utils import OK')"
~~~

Đây chỉ là kiểm tra cơ bản, không thay thế unit test hay chạy notebook.

## Triển khai sách

Workflow [deploy.yml](.github/workflows/deploy.yml) build Jupyter Book và publish HTML lên GitHub Pages khi push vào main. Hãy kiểm tra TOC, kết quả build và trạng thái deploy.

## Tài liệu tham khảo

- Christopher M. Bishop, *Pattern Recognition and Machine Learning*.
- Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning*.
- Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning*.
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) · [API](https://scikit-learn.org/stable/modules/classes.html).
- [NumPy Documentation](https://numpy.org/doc/).

Khi dựa vào tài liệu, hãy dẫn rõ chương, ấn bản hoặc trang tham khảo.

## Giấy phép

Repository hiện **chưa có file LICENSE**. Khi chưa có license, quyền tái sử dụng, phân phối lại và đóng góp mã chưa được cấp phép rõ ràng. Hãy bổ sung license phù hợp trước khi giới thiệu dự án là phần mềm mở có thể tái sử dụng.

---
Được duy trì bởi [hdwc-151](https://github.com/hdwc-151).
