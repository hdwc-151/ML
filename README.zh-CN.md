# 从零实现机器学习（Machine Learning From Scratch）

**理解数学 · 动手实现 · 实验验证**

[🇻🇳 Tiếng Việt](README.md) · [🇬🇧 English](README.en.md) · [🇨🇳 简体中文](README.zh-CN.md)

本项目通过数学推导、Python/NumPy 实现、可视化和参考库对比，帮助学习经典**机器学习（ML）**与基础**深度学习（DL）**。

> **项目状态：** 持续开发中的教育项目，包含学习 Notebook 与共享工具。各主题的完整度、API 稳定性及可复现性有所不同；本项目不是面向生产环境的 ML 框架。

## 项目入口
- **[阅读在线教材（Jupyter Book）](https://hdwc-151.github.io/ML/)**
- [浏览 Notebook](algorithms/notebooks)
- [共享工具](utils)
- [提交问题或建议](https://github.com/hdwc-151/ML/issues)

## 学习流程
1. **理解问题：** 明确目标、假设、符号和适用范围。
2. **数学推导：** 梳理目标函数、公式和优化逻辑。
3. **动手实现：** 使用清晰易读的 Python/NumPy 编写。
4. **实验探索：** 可视化、调整参数、分析边界情况。
5. **验证结果：** 在适当条件下与 scikit-learn 等参考实现比较。

“从零实现”是一种学习方式，不自动保证正确、高效或数值稳定。比较时需确保假设、数据、评估方式与容差一致。

## 学习内容

| 模块 | 主题 | Notebook |
|---|---|---|
| 00 · 基础 | 线性代数、微积分、概率、MLE/MAP | [查看](algorithms/notebooks/00_foundations) |
| 01 · 回归 | 正规方程、梯度下降、多项式、Ridge/Lasso/Elastic Net | [查看](algorithms/notebooks/01_regression) |
| 02 · 分类 | 感知机、逻辑回归、Softmax 回归、SVM | [查看](algorithms/notebooks/02_classification) |
| 03 · 邻域与贝叶斯 | KNN、Gaussian/Multinomial Naive Bayes | [查看](algorithms/notebooks/03_instance_bayes) |
| 04 · 树与集成 | 决策树、随机森林、AdaBoost、梯度提升 | [查看](algorithms/notebooks/04_trees_ensembles) |
| 05 · 无监督学习 | K-means、聚类、DBSCAN、PCA/SVD、GMM/EM | [查看](algorithms/notebooks/05_unsupervised) |
| 06 · 神经网络 | 计算图、反向传播、MLP、优化器 | [查看](algorithms/notebooks/06_neural_networks) |

**范围说明：** 此表代表 Notebook 教学内容，不表示每种算法都已实现为完整、可复用的 estimator。

## 仓库结构

~~~text
ML/
├── algorithms/notebooks/
│   ├── 00_foundations/  01_regression/  02_classification/
│   ├── 03_instance_bayes/  04_trees_ensembles/
│   ├── 05_unsupervised/  06_neural_networks/
├── utils/
├── .github/workflows/deploy.yml
├── _config.yml  _toc.yml  intro.md
├── pyproject.toml  requirements.txt
├── README.md  README.en.md  README.zh-CN.md
~~~

此处省略自动生成文件、字节码与 Notebook 缓存。

## 快速开始

### 环境要求
- Python **3.9+**（项目元数据要求）。
- Conda 或 Python venv、Git 和网络连接。

CI 使用 Python 3.11，建议本地采用相同版本。

### 1. 克隆仓库

~~~bash
git clone https://github.com/hdwc-151/ML.git
cd ML
~~~

### 2. 创建环境

**Conda（Python 3.13.12）：**

~~~bash
conda env create -f environment.yml
conda activate ml-from-scratch
~~~

更新已有环境：`conda env update -f environment.yml --prune`。

**或 venv（Python 3.13.12）：**

~~~bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
~~~

### 3. 安装依赖

~~~bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements.txt
~~~

项目声明 NumPy、Matplotlib 和 scikit-learn；requirements 还包含 Jupyter Book。依赖未完全锁定，暂不能保证环境间完全一致的复现。

### 4. 运行 Notebook

~~~bash
jupyter notebook
~~~

打开 algorithms/notebooks 下的 Notebook。使用 JupyterLab：

~~~bash
python -m pip install jupyterlab
jupyter lab
~~~

### 5. 查看工具包

~~~python
import utils
print(utils.__all__)
~~~

工具包提供部分激活函数、损失函数、指标、距离计算与预处理。具体 API 请查看 [utils/__init__.py](utils/__init__.py) 及各模块。

## 可复现性与验证
- 在全新 kernel 中依次运行 Notebook。
- 适当记录依赖版本、随机种子和数据来源。
- 先划分数据再拟合预处理；仅在训练集上 fit transform。
- 检查形状、数值稳定性、边界情况和收敛性。
- 在假设与容差一致时对比独立参考实现。
- 不要提交大型数据集、模型 checkpoint、凭证或本地环境文件。

**当前不足：** 尚无全面自动化测试套件和完整依赖锁定文件。安装成功并不代表算法正确或结果可复现。

## 参与贡献
1. 为具体改动创建独立分支。
2. 说明改动范围与数学依据。
3. 在干净 kernel 中运行相关 Notebook，并验证修改。
4. 在 Pull Request 中说明影响、假设与局限。

~~~bash
python -m pip check
python -c "import utils; print('utils import OK')"
~~~

这些基础检查不能替代测试与 Notebook 执行。

## 教材部署

[部署工作流](.github/workflows/deploy.yml) 会在推送到 main 时构建 Jupyter Book，并将 HTML 发布到 GitHub Pages。请分别检查 TOC、构建与部署状态。

## 参考资料

### 机器学习数学基础

- Marc Peter Deisenroth、A. Aldo Faisal、Cheng Soon Ong，*Mathematics for Machine Learning* — [官方网站与教材资源](https://mml-book.github.io/)。
- **越南语 ML 基础与 Vũ Khắc Tiệp 相关学习资料：** [AIVietnam Machine Learning course（GitHub）](https://github.com/thanhhff/AIVN-Machine-Learning)。该社区课程引用了 Vũ Khắc Tiệp 的数学学习资料；此链接是 AIVietnam 课程仓库，并非将其误称为作者个人仓库。
- Christopher M. Bishop，*Pattern Recognition and Machine Learning*。
- Trevor Hastie、Robert Tibshirani、Jerome Friedman，*The Elements of Statistical Learning*。
- Ian Goodfellow、Yoshua Bengio、Aaron Courville，*Deep Learning*。
- [scikit-learn 用户指南](https://scikit-learn.org/stable/user_guide.html) · [API](https://scikit-learn.org/stable/modules/classes.html)。
- [NumPy 文档](https://numpy.org/doc/)。

引用推导或结论时，请注明对应章节、版本或文档页面。

## 许可证

目前仓库**尚无 LICENSE 文件**。添加合适许可证前，复用、再分发和贡献条款尚未得到明确授权。

---
由 [hdwc-151](https://github.com/hdwc-151) 维护。
