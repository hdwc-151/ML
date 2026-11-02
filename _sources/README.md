# Machine Learning From Scratch

**Hiểu toán học · Tự triển khai thuật toán · Kiểm chứng bằng thực nghiệm**

[🇻🇳 Tiếng Việt](README.md) · [🇬🇧 English](README.en.md) · [🇨🇳 简体中文](README.zh-CN.md)

Dự án học tập và thực nghiệm về Machine Learning và nền tảng Deep Learning, kết hợp suy luận toán học, triển khai Python/NumPy, trực quan hóa và đối chiếu với thư viện tham chiếu.

> **Trạng thái:** Dự án giáo dục đang phát triển; chưa phải framework ML dùng trong production.

## Khám phá

- [Đọc sách trực tuyến — Jupyter Book](https://hdwc-151.github.io/ML/)
- [Notebook algorithms](algorithms/notebooks)
- [Tài liệu tham khảo học thuật](docs/references/README.md)
- [Chỉ mục Toán học](docs/references/indexes/mathematics.md) · [ML](docs/references/indexes/machine-learning.md) · [DL](docs/references/indexes/deep-learning.md)
- [Topic → Notebook → Reference](docs/references/indexes/topic-to-notebook.md)
- [CI/CD và xử lý lỗi GitHub Actions](docs/ci/github-actions.md)
- [Báo lỗi / đề xuất](https://github.com/hdwc-151/ML/issues)

## Phương pháp học

1. Hiểu bài toán, giả định, ký hiệu và phạm vi áp dụng.
2. Suy luận toán học: hàm mục tiêu, công thức và logic tối ưu.
3. Tự triển khai bằng Python/NumPy.
4. Thực nghiệm, trực quan hóa và khảo sát trường hợp biên.
5. Kiểm chứng với tài liệu hoặc thư viện tham chiếu.

“From scratch” là phương pháp học, không tự động đảm bảo đúng, tối ưu hay ổn định.

## Lộ trình nội dung

| Phần | Chủ đề |
|---|---|
| 00 | Đại số tuyến tính, giải tích, xác suất, MLE/MAP |
| 01 | Normal equation, gradient descent, polynomial regression, regularization |
| 02 | Perceptron, logistic/softmax regression, SVM |
| 03 | KNN, Gaussian và Multinomial Naive Bayes |
| 04 | Decision trees, random forest, AdaBoost, gradient boosting |
| 05 | K-means, clustering, DBSCAN, PCA/SVD, GMM/EM |
| 06 | Computational graph, backpropagation, MLP, optimizers |

Xem [danh mục notebook](algorithms/notebooks). Bảng này mô tả chủ đề hiện có, không khẳng định mọi thuật toán đã là estimator hoàn chỉnh.

## Tài liệu tham khảo

Catalog chuẩn hóa nằm tại [docs/references](docs/references/README.md). Các tài liệu chính:
- Deisenroth, Faisal, Ong — *Mathematics for Machine Learning*: https://mml-book.github.io/
- Vũ Hữu Tiệp — *Machine Learning cơ bản*: https://machinelearningcoban.com/
- James et al. — *An Introduction to Statistical Learning*: https://www.statlearning.com/
- Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*: https://hastie.su.domains/ElemStatLearn/
- Bishop — *Pattern Recognition and Machine Learning*: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
- Goodfellow, Bengio, Courville — *Deep Learning*: https://www.deeplearningbook.org/

**Lưu ý tên tác giả:** nguồn *Machine Learning cơ bản* được biết đến rộng rãi gắn với Vũ Hữu Tiệp. Repository AIVietnam là học liệu cộng đồng, không phải repo cá nhân của tác giả. Xem [ghi chú nguồn](docs/references/books/VHT-001.md).

Ưu tiên website tác giả, nhà xuất bản và thư viện học thuật. Không đưa PDF không rõ quyền phát hành vào repo. Đọc/tải miễn phí không đồng nghĩa với quyền tái phân phối.

## Cài đặt

Yêu cầu Python 3.9+ theo metadata package. CI dùng Python 3.13.

```bash
git clone https://github.com/hdwc-151/ML.git
cd ML
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements.txt
```

Chạy notebook bằng `jupyter notebook` hoặc cài JupyterLab. Môi trường Conda có thể tạo từ `environment.yml`.

## Kiểm tra và build sách

```bash
python -m pip check
python -c "import utils; print('utils import OK')"
jupyter-book build .
```

Workflow deploy nằm tại [.github/workflows/deploy.yml](.github/workflows/deploy.yml). CI xanh chỉ xác nhận các bước đã chạy thành công; không thay thế unit tests, kiểm chứng thuật toán hay đánh giá khoa học. Xem [hướng dẫn xử lý lỗi](docs/ci/github-actions.md).

## Cấu trúc chính

```text
ML/
├── algorithms/notebooks/
├── docs/
│   ├── references/
│   │   ├── books/
│   │   ├── indexes/
│   │   └── taxonomy/
│   └── ci/
├── utils/
├── .github/workflows/
├── _config.yml
├── _toc.yml
└── README*.md
```

## Đóng góp

Tạo nhánh riêng, giữ diff nhỏ, nêu rõ cơ sở toán học và chạy notebook liên quan từ kernel sạch. Không commit dữ liệu lớn, checkpoint, secrets hoặc file môi trường cá nhân.

## Giấy phép

Repository hiện chưa có file LICENSE. Khi chưa có license, quyền tái sử dụng và phân phối lại mã chưa được cấp phép rõ ràng.
