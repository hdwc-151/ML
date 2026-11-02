# Deep Learning — Index

## Learning sequence

| ID | Topic | Core concepts | Main reference | Repository status |
|---|---|---|---|---|
| DL-01 | Neural network foundations | neuron, activation, layers, forward pass | Goodfellow Ch.6; PRML Ch.5 | [MLP notebook](../../../algorithms/notebooks/06_neural_networks/02_multi_layer_perceptron.ipynb) |
| DL-02 | Computational graphs and autodiff | chain rule, graph, reverse-mode differentiation | Goodfellow Ch.6; MML Ch.5 | [Backprop notebook](../../../algorithms/notebooks/06_neural_networks/01_computational_graph_backprop.ipynb) |
| DL-03 | Optimization | SGD, momentum, adaptive optimizers | Goodfellow Ch.8 | [Optimizer notebook](../../../algorithms/notebooks/06_neural_networks/03_optimizers_momentum_adam.ipynb) |
| DL-04 | Generalization | regularization, initialization, early stopping | Goodfellow Ch.7, 11 | Partial: regularization notebook is classical ML |
| DL-05 | Convolutional networks | convolution, pooling, receptive field | Goodfellow Ch.9 | Not yet implemented |
| DL-06 | Sequence models | RNN, LSTM, recursive nets | Goodfellow Ch.10 | Not yet implemented |
| DL-07 | Representation learning | autoencoders, latent representations | Goodfellow Ch.14–15 | Not yet implemented |
| DL-08 | Generative models | latent-variable models, likelihood, sampling | Goodfellow Ch.16–20 | Not yet implemented |

## Recommended prerequisites

Complete MATH-01 through MATH-06 and ML-02 through ML-04 first. Then study computational graphs and MLPs before CNNs, sequence models or generative models.

## Scope warning

This repository currently provides introductory neural-network notebooks. It does not yet implement a complete deep-learning framework, CNN pipeline, transformer, or generative model.
