# Machine Learning From Scratch

**Derive the mathematics. Implement the algorithms. Verify the results.**

A learning and experimentation repository for understanding classical Machine Learning (ML) and foundational Deep Learning (DL) through mathematical derivations, NumPy-based implementations, visualizations, and comparisons with established tools.

> **Status:** Educational project in active development. The repository contains learning notebooks and shared utilities. Coverage, API stability, and reproducibility vary by topic; this is not a production-ready ML framework.

[![Python](https://img.shields.io/badge/Python-%3E%3D3.9-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/Core-NumPy-013243?logo=numpy)](https://numpy.org/)
[![Online Book](https://img.shields.io/badge/Read-Online%20Book-brightgreen)](https://hdwc-151.github.io/ML/)

## Explore

- **[Read the online book](https://hdwc-151.github.io/ML/)** — hosted material; freshness depends on successful deployment.
- **[Browse notebooks](https://github.com/hdwc-151/ML/tree/main/algorithms/notebooks)** — derivations, implementations, experiments.
- **[Explore shared utilities](https://github.com/hdwc-151/ML/tree/main/utils)** — reusable ML helpers.
- **[Report an issue](https://github.com/hdwc-151/ML/issues)** — bugs, corrections, suggestions.

## Learning approach

The intended workflow for each topic:

1. **Understand:** define the problem, assumptions, and notation.
2. **Derive:** work through objectives, equations, and optimization logic.
3. **Implement:** translate the derivation into readable Python/NumPy.
4. **Experiment:** visualize behavior, vary inputs, and probe edge cases.
5. **Verify:** compare selected results with trusted references such as scikit-learn where appropriate.

A from-scratch implementation is a learning exercise—not automatically a correct or efficient one. Comparisons are tests to design and interpret, not proof of universal correctness.

## Curriculum

| Section | Topics | Notebooks |
|---|---|---|
| 00 · Foundations | Linear algebra, calculus, probability, MLE/MAP | [Open](algorithms/notebooks/00_foundations) |
| 01 · Regression | Normal equation, gradient descent, polynomial regression, Ridge/Lasso/Elastic Net | [Open](algorithms/notebooks/01_regression) |
| 02 · Classification | Perceptron, logistic and softmax regression, SVM | [Open](algorithms/notebooks/02_classification) |
| 03 · Instance-based & Bayesian | K-nearest neighbors, Gaussian and Multinomial Naive Bayes | [Open](algorithms/notebooks/03_instance_bayes) |
| 04 · Trees & ensembles | Decision trees, random forests, AdaBoost, gradient boosting | [Open](algorithms/notebooks/04_trees_ensembles) |
| 05 · Unsupervised learning | K-means, hierarchical clustering, DBSCAN, PCA, SVD, GMM, EM | [Open](algorithms/notebooks/05_unsupervised) |
| 06 · Neural networks | Computational graphs, backpropagation, MLP, optimization methods | [Open](algorithms/notebooks/06_neural_networks) |

**Scope:** Topics listed describe the notebook curriculum. They do not imply every method is available as a polished, reusable estimator in the Python package.

## Repository structure

~~~text
ML/
├── algorithms/
│   └── notebooks/
│       ├── 00_foundations/
│       ├── 01_regression/
│       ├── 02_classification/
│       ├── 03_instance_bayes/
│       ├── 04_trees_ensembles/
│       ├── 05_unsupervised/
│       └── 06_neural_networks/
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
└── README.md
~~~

Generated artifacts, Python bytecode, and notebook caches are omitted from this overview.

## Getting started

### Requirements

- Python **3.9+**, as declared in project metadata.
- Conda (Miniconda, Miniforge, or Anaconda) or Python venv.
- Git and internet access for dependency installation.

CI currently uses Python 3.11. For a closer match to CI, use 3.11 locally; other versions should be validated.

### 1. Clone

~~~bash
git clone https://github.com/hdwc-151/ML.git
cd ML
~~~

### 2. Create an environment

**Conda (recommended):**

~~~bash
conda create -n ml-from-scratch python=3.11 -y
conda activate ml-from-scratch
~~~

**Alternative: venv**

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

The project metadata declares NumPy, Matplotlib, and scikit-learn. The requirements file also includes Jupyter Book. Dependencies are not fully pinned, so this is not a bit-for-bit environment lock.

### 4. Run notebooks

~~~bash
jupyter notebook
~~~

Open notebooks from **algorithms/notebooks/** in the Jupyter browser.

To use JupyterLab instead:

~~~bash
python -m pip install jupyterlab
jupyter lab
~~~

### 5. Inspect the utility package

~~~python
import utils

print(utils.__all__)
~~~

The shared utilities expose selected activation functions, loss functions, metrics, distance calculations, and preprocessing helpers. Consult [utils/__init__.py](utils/__init__.py) and individual modules for exact APIs.

## Reproducibility and validation

When running or extending notebooks:

- Run cells in order in a fresh kernel.
- Record package versions, random seeds, and data sources where relevant.
- Split data before fitting preprocessing; fit transforms on training data only.
- Check shapes, numerical stability, edge cases, and convergence.
- Compare against an independent implementation with aligned assumptions and sensible tolerances.
- Do not commit large datasets, model checkpoints, credentials, or local environment files.

**Known maturity gap:** The repository does not yet provide a comprehensive automated test suite or fully pinned environment lockfile. Do not assume algorithm correctness or notebook reproducibility solely because package installation succeeds.

## Development

1. Create a focused branch.
2. Keep changes scoped and explain the motivation.
3. Run affected notebooks from a clean kernel.
4. Validate changed utility behavior.
5. Summarize mathematical and behavioral implications in your pull request.

Suggested smoke checks:

~~~bash
python -m pip check
python -c "import utils; print('utils import OK')"
~~~

These checks are not substitutes for unit tests or notebook execution.

## Deployment

The repository includes [the GitHub Actions workflow](.github/workflows/deploy.yml), which builds Jupyter Book and publishes HTML to GitHub Pages on pushes to main.

Before relying on the published site, verify that all chapter paths exist, the Jupyter Book version supports the configuration, the workflow succeeds, and the deployed site reflects the intended commit.

> **Deployment blocker identified:** The current table of contents references **notebooks/** paths, but the notebook files currently live under **algorithms/notebooks/**. Align the TOC or intentionally reorganize the notebooks, then run a clean book build before treating deployment as healthy.

## References

- Christopher M. Bishop, *Pattern Recognition and Machine Learning*.
- Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning*.
- Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning*.
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) and [API reference](https://scikit-learn.org/stable/modules/classes.html).
- [NumPy documentation](https://numpy.org/doc/).

When a derivation or result relies on a source, cite the relevant chapter, edition, or documentation page.

## License

**No license file is currently present.** Until a license is added, reuse, redistribution, and contribution terms are not explicitly granted. Add an appropriate LICENSE before describing this project as openly reusable software.

---

Maintained by [hdwc-151](https://github.com/hdwc-151).
