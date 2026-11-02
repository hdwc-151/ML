# PRML-001 — Pattern Recognition and Machine Learning

## Bibliographic record

| Field | Value |
|---|---|
| Title | *Pattern Recognition and Machine Learning* |
| Author | Christopher M. Bishop |
| Publisher | Springer |
| Year / edition | 2006; first edition |
| ISBN | 978-0-387-31073-2 |
| Official publisher page | https://link.springer.com/book/9780387310732 |
| Author/publisher-hosted resource | https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/ |
| Access | Microsoft Research page links to a full author/publisher-hosted PDF; Springer page provides bibliographic and supplementary information |
| Rights note | Free access to a hosted PDF is not a blanket redistribution license |

## Official chapter map

1. Introduction
2. Probability Distributions
3. Linear Models for Regression
4. Linear Models for Classification
5. Neural Networks
6. Kernel Methods
7. Sparse Kernel Machines
8. Graphical Models
9. Mixture Models and EM
10. Approximate Inference
11. Sampling Methods
12. Continuous Latent Variables
13. Sequential Data
14. Combining Models

Use the exact section titles from the book PDF when producing formal citations.

## Prerequisites

- Linear algebra: vectors, matrices, eigenvalues/eigenvectors.
- Multivariable calculus and chain rule.
- Probability: conditional probability, Bayes' rule, common distributions, expectation.
- Basic optimization.
- Python is useful for experiments but not a prerequisite for reading the mathematics.

## Topic mapping to repository

| Topic | PRML chapter | Existing notebook |
|---|---:|---|
| Probability distributions, Bayes rule | 2 | [02_probability_mle_map](../../../algorithms/notebooks/00_foundations/02_probability_mle_map.ipynb) |
| Linear regression | 3 | [01_linear_regression_normal_equation](../../../algorithms/notebooks/01_regression/01_linear_regression_normal_equation.ipynb) |
| Logistic / probabilistic classification | 4 | [02_logistic_regression](../../../algorithms/notebooks/02_classification/02_logistic_regression.ipynb) |
| Neural networks | 5 | [02_multi_layer_perceptron](../../../algorithms/notebooks/06_neural_networks/02_multi_layer_perceptron.ipynb) |
| Kernel methods and SVM | 6–7 | [04_support_vector_machines](../../../algorithms/notebooks/02_classification/04_support_vector_machines.ipynb) |
| Mixture models and EM | 9 | [04_gaussian_mixture_models_em](../../../algorithms/notebooks/05_unsupervised/04_gaussian_mixture_models_em.ipynb) |
| Latent variables / dimensionality reduction | 12 | [03_pca_svd_dimensionality_reduction](../../../algorithms/notebooks/05_unsupervised/03_pca_svd_dimensionality_reduction.ipynb) |

## Reading strategy

PRML is mathematically dense. Read Chapters 2–4 before neural networks or graphical models. Derive likelihoods and posterior distributions on paper; use repository notebooks to make assumptions and numerical behavior explicit.

## Official resources

- Microsoft Research book page: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
- Springer book page and supplementary material: https://link.springer.com/book/9780387310732
