# Question: Demonstrate Gibbs Sampling, build a probabilistic model, and generate posterior samples.
"""Gibbs sampler for Bayesian linear regression with a Normal-Inverse-Gamma prior."""
import numpy as np
from scipy.stats import invgamma
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler

def gibbs(X, y, iterations=5000, burn=1000, seed=42):
    rng = np.random.default_rng(seed)
    n, p = X.shape
    tau2, a0, b0 = 100.0, 2.0, 2.0
    beta = np.zeros(p); sigma2 = 1.0
    samples = np.empty((iterations, p))
    for i in range(iterations):
        cov = np.linalg.inv(X.T @ X / sigma2 + np.eye(p) / tau2)
        mean = cov @ (X.T @ y / sigma2)
        beta = rng.multivariate_normal(mean, cov)
        residual = y - X @ beta
        shape = a0 + n / 2
        scale = b0 + 0.5 * residual @ residual + 0.5 * beta @ beta / tau2
        sigma2 = invgamma.rvs(a=shape, scale=scale, random_state=rng)
        samples[i] = beta
    return samples[burn:]

def main():
    data = load_diabetes()
    X = StandardScaler().fit_transform(data.data)
    X = np.column_stack((np.ones(len(X)), X))
    y = data.target.astype(float)
    posterior = gibbs(X, y)
    print("Posterior samples:", len(posterior))
    print("Posterior coefficient means:", np.round(posterior.mean(axis=0), 2))
    print("95% credible interval for BMI coefficient:", np.round(np.percentile(posterior[:, 4], [2.5, 97.5]), 2))

if __name__ == "__main__": main()
