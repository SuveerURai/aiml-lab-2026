# Question: Build an ANN using backpropagation and test it with an appropriate dataset.
"""Train a one-hidden-layer neural network from scratch with NumPy."""
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-np.clip(x, -40, 40)))

def main():
    X = np.array([[2,9],[1,5],[3,6]], dtype=float)
    y = np.array([[.92],[.86],[.89]])
    X /= X.max(axis=0)
    rng = np.random.default_rng(7)
    w1 = rng.uniform(-1, 1, (2, 3)); b1 = np.zeros((1, 3))
    w2 = rng.uniform(-1, 1, (3, 1)); b2 = np.zeros((1, 1))
    rate = 0.6
    for _ in range(10000):
        hidden = sigmoid(X @ w1 + b1); output = sigmoid(hidden @ w2 + b2)
        delta_out = (y - output) * output * (1-output)
        delta_hidden = (delta_out @ w2.T) * hidden * (1-hidden)
        w2 += rate * hidden.T @ delta_out; b2 += rate * delta_out.sum(axis=0, keepdims=True)
        w1 += rate * X.T @ delta_hidden; b1 += rate * delta_hidden.sum(axis=0, keepdims=True)
    print("Actual outputs:\n", y)
    print("Predicted outputs:\n", sigmoid(sigmoid(X @ w1 + b1) @ w2 + b2))

if __name__ == "__main__": main()
