# Mathematics for Machine Learning — Index

This index groups the mathematical prerequisites needed by the algorithms in this repository. It is a learning sequence, not a claim that all topics are already implemented.

## Suggested order

| ID | Topic | Required ideas | Main reference | Existing notebook |
|---|---|---|---|---|
| MATH-01 | Linear algebra | vectors, matrices, rank, basis, linear maps | MML Ch.2; DL Ch.2 | [Foundations 01](../../../algorithms/notebooks/00_foundations/01_linear_algebra_calculus.ipynb) |
| MATH-02 | Analytic geometry | norms, dot product, orthogonality, projection | MML Ch.3 | [Foundations 01](../../../algorithms/notebooks/00_foundations/01_linear_algebra_calculus.ipynb) |
| MATH-03 | Matrix decomposition | eigenvalues, eigenspaces, SVD, low rank | MML Ch.4; ESL Ch.14 | [PCA/SVD](../../../algorithms/notebooks/05_unsupervised/03_pca_svd_dimensionality_reduction.ipynb) |
| MATH-04 | Differential calculus | derivatives, partial derivatives, gradient, Jacobian, chain rule | MML Ch.5; DL Ch.4 | [Foundations 01](../../../algorithms/notebooks/00_foundations/01_linear_algebra_calculus.ipynb) |
| MATH-05 | Probability and statistics | random variables, conditional probability, expectation, variance, covariance | MML Ch.6; PRML Ch.2; DL Ch.3 | [Foundations 02](../../../algorithms/notebooks/00_foundations/02_probability_mle_map.ipynb) |
| MATH-06 | Optimization | objective, convexity, gradient descent, constraints | MML Ch.7; DL Ch.8 | [Gradient descent](../../../algorithms/notebooks/01_regression/02_linear_regression_gradient_descent.ipynb) |
| MATH-07 | Information theory | entropy, cross-entropy, KL divergence, mutual information | DL Ch.3; PRML Ch.1–2 | [Logistic regression](../../../algorithms/notebooks/02_classification/02_logistic_regression.ipynb) |
| MATH-08 | Numerical computation | floating point, conditioning, stability, vectorization | DL Ch.4 | Not yet available |

## Competency gate

Before implementing gradient-based models, the learner should be able to:
- derive a scalar derivative and partial derivative;
- distinguish gradient shape from parameter shape;
- apply the chain rule to a computational graph;
- explain dot product, matrix multiplication and broadcasting;
- derive expectation and variance for a simple distribution;
- explain why numerical stability matters (e.g. log-sum-exp).

## Reference sequence

1. MML Chapters 2–7 for structured mathematical foundations.
2. DL Chapters 2–4 for numerical computation and ML-specific mathematical tools.
3. PRML Chapter 2 for probabilistic modeling depth.
