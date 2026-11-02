# Machine Learning — Index

## Learning sequence

| ID | Topic | Core concepts | Main references | Existing notebooks |
|---|---|---|---|---|
| ML-01 | Problem formulation | supervised/unsupervised, features, targets, loss, generalization | ISLR Ch.1–2; ESL Ch.1–2 | [All algorithm notebooks](../../../algorithms/notebooks) |
| ML-02 | Linear regression | least squares, normal equation, residuals | MML Ch.9; ISLR Ch.3; ESL Ch.3 | [Regression](../../../algorithms/notebooks/01_regression) |
| ML-03 | Optimization and regularization | GD, learning rate, Ridge, Lasso, Elastic Net | MML Ch.7; ISLR Ch.6; ESL Ch.5 | [GD](../../../algorithms/notebooks/01_regression/02_linear_regression_gradient_descent.ipynb), [Regularization](../../../algorithms/notebooks/01_regression/04_ridge_lasso_elasticnet.ipynb) |
| ML-04 | Classification | perceptron, logistic, softmax, margins | ISLR Ch.4; ESL Ch.4; PRML Ch.4 | [Classification](../../../algorithms/notebooks/02_classification) |
| ML-05 | Instance / probabilistic methods | KNN, Bayes rule, Naive Bayes | PRML Ch.2; ISLR Ch.4 | [Instance/Bayes](../../../algorithms/notebooks/03_instance_bayes) |
| ML-06 | Trees and ensembles | impurity, bagging, random forest, boosting | ISLR Ch.8; ESL Ch.9–10, 15–16 | [Trees/ensembles](../../../algorithms/notebooks/04_trees_ensembles) |
| ML-07 | Unsupervised learning | clustering, PCA, GMM, EM | ISLR Ch.12; ESL Ch.14; PRML Ch.9 | [Unsupervised](../../../algorithms/notebooks/05_unsupervised) |
| ML-08 | Model evaluation | train/validation/test, cross-validation, metrics, calibration | ISLR Ch.5; ESL Ch.7–8 | Dedicated notebook not yet present |

## Implementation standard

Each algorithm notebook should eventually include:
1. Problem statement and assumptions.
2. Notation and tensor/array shapes.
3. Mathematical derivation.
4. NumPy implementation with clear function contracts.
5. Synthetic or public dataset experiment.
6. Numerical/edge-case tests.
7. Reference implementation comparison.
8. Limitations and further reading.

## Critical gap

Model evaluation and data leakage prevention deserve a dedicated section. Do not interpret high training accuracy as evidence of generalization.
