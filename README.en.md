# Machine Learning From Scratch

**Build intuition from mathematics. Implement algorithms. Verify results.**

[🇻🇳 Tiếng Việt](README.md) · [🇬🇧 English](README.en.md) · [🇨🇳 简体中文](README.zh-CN.md)

An educational lab for classical **Machine Learning (ML)** and foundational **Deep Learning (DL)** through mathematical derivations, Python/NumPy implementations, visualizations, and comparisons with reference libraries.

> **Status:** In active development. This repository contains learning notebooks and shared utilities. Maturity, API stability, and reproducibility vary by topic; this is not a production ML framework.

## Explore
- **[Read the online book (Jupyter Book)](https://hdwc-151.github.io/ML/)**
- [Browse notebooks](algorithms/notebooks)
- [Shared utilities](utils)
- [Report an issue](https://github.com/hdwc-151/ML/issues)

## Learning workflow
1. **Understand:** problem, assumptions, notation, scope.
2. **Derive:** objective, equations, optimization logic.
3. **Implement:** readable Python/NumPy.
4. **Experiment:** visualize, vary parameters, inspect edge cases.
5. **Verify:** compare with documentation or references such as scikit-learn.

“From scratch” is a learning method, not a guarantee of correctness, efficiency, or stability. Comparisons require aligned assumptions, data, evaluation, and tolerances.

## Curriculum

| Section | Topics | Notebooks |
|---|---|---|
| 00 · Foundations | Linear algebra, calculus, probability, MLE/MAP | [Open](algorithms/notebooks/00_foundations) |
| 01 · Regression | Normal equation, gradient descent, polynomial, Ridge/Lasso/Elastic Net | [Open](algorithms/notebooks/01_regression) |
| 02 · Classification | Perceptron, logistic/softmax regression, SVM | [Open](algorithms/notebooks/02_classification) |
| 03 · Instance-based & Bayesian | KNN, Gaussian and Multinomial Naive Bayes | [Open](algorithms/notebooks/03_instance_bayes) |
| 04 · Trees & ensembles | Decision trees, random forest, AdaBoost, gradient boosting | [Open](algorithms/notebooks/04_trees_ensembles) |
| 05 · Unsupervised | K-means, clustering, DBSCAN, PCA/SVD, GMM/EM | [Open](algorithms/notebooks/05_unsupervised) |
| 06 · Neural networks | Computational graphs, backpropagation, MLP, optimizers | [Open](algorithms/notebooks/06_neural_networks) |

**Scope:** Topics reflect notebook coverage, not necessarily complete reusable estimators in the package.

## Repository structure

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

Generated artifacts, bytecode, and notebook caches are omitted.

## Getting started

### Requirements
- Python **3.9+** per project metadata.
- Conda or Python venv, Git, and internet access.

CI currently uses Python 3.11; matching it locally is recommended.

### 1. Clone

~~~bash
git clone https://github.com/hdwc-151/ML.git
cd ML
~~~

### 2. Environment

**Conda:**

~~~bash
conda create -n ml-from-scratch python=3.11 -y
conda activate ml-from-scratch
~~~

**Or venv:**

~~~bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
~~~

### 3. Install

~~~bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements.txt
~~~

Metadata declares NumPy, Matplotlib, and scikit-learn; requirements add Jupyter Book. Dependencies are not fully pinned, so this is not a reproducible lockfile.

### 4. Run notebooks

~~~bash
jupyter notebook
~~~

Open notebooks in algorithms/notebooks. For JupyterLab:

~~~bash
python -m pip install jupyterlab
jupyter lab
~~~

### 5. Inspect utilities

~~~python
import utils
print(utils.__all__)
~~~

Utilities expose selected activations, losses, metrics, distance calculations, and preprocessing. See [utils/__init__.py](utils/__init__.py) and module APIs.

## Reproducibility and validation
- Run notebooks in order from a fresh kernel.
- Record dependency versions, random seeds, and data sources where relevant.
- Split data before fitting preprocessing; fit transforms on training data only.
- Check shapes, numerical stability, edge cases, and convergence.
- Compare against independent references under aligned assumptions and tolerances.
- Do not commit large datasets, checkpoints, credentials, or local environment files.

**Current gap:** No comprehensive automated test suite or fully pinned environment lockfile yet. Successful installation does not prove correctness or reproducibility.

## Contributing
1. Create a focused branch.
2. Explain scope and mathematical motivation.
3. Run affected notebooks from a clean kernel and validate changed utilities.
4. Describe impact, assumptions, and limitations in your pull request.

~~~bash
python -m pip check
python -c "import utils; print('utils import OK')"
~~~

These smoke checks do not replace tests or notebook execution.

## Book deployment

[The deployment workflow](.github/workflows/deploy.yml) builds Jupyter Book and publishes HTML to GitHub Pages on pushes to main. Validate TOC paths, build results, and deployment status separately.

## References
- Christopher M. Bishop, *Pattern Recognition and Machine Learning*.
- Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning*.
- Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning*.
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) · [API](https://scikit-learn.org/stable/modules/classes.html).
- [NumPy documentation](https://numpy.org/doc/).

Cite the relevant chapter, edition, or documentation page.

## License

**No LICENSE file is currently present.** Reuse, redistribution, and contribution terms are not explicitly granted until an appropriate license is added.

---
Maintained by [hdwc-151](https://github.com/hdwc-151).
