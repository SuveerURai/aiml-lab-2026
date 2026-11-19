# Question: Demonstrate Gibbs Sampling and generate samples from a posterior distribution.
# Transcribed from the manual; indentation restored for Python readability.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from scipy.stats import invgamma

# 1. Load dataset
data = load_diabetes()
X = StandardScaler().fit_transform(data.data)
y = data.target

# Add intercept
X = np.c_[np.ones(len(X)), X]
n, p = X.shape

# 2. Prior parameters
tau2 = 100
a0, b0 = 2, 2

# 3. Initialize
N, burn = 5000, 1000
beta = np.zeros(p)
sigma2 = 1
samples = np.zeros((N, p))

# 4. Gibbs Sampling
for i in range(N):
    # beta | sigma2, y
    V = np.linalg.inv(X.T @ X / sigma2 + np.eye(p) / tau2)
    m = V @ (X.T @ y / sigma2)
    beta = np.random.multivariate_normal(m, V)

    # sigma2 | beta, y
    error = y - X @ beta
    a = a0 + n / 2
    b = b0 + 0.5 * np.sum(error ** 2) + 0.5 * np.sum(beta ** 2) / tau2
    sigma2 = invgamma.rvs(a=a, scale=b)
    samples[i] = beta

# 5. Remove burn-in
posterior = samples[burn:]

# 6. Validation
print("Dataset samples :", n)
print("Total iterations :", N)
print("Burn-in samples :", burn)
print("Posterior samples:", len(posterior))
print("\nPosterior Mean of Coefficients:")
print(np.round(posterior.mean(axis=0), 3))
print("\n95% Credible Interval:")
for j in range(p):
    print(j, np.round(np.percentile(posterior[:, j], [2.5, 97.5]), 3))

# 7. Trace plot
plt.plot(samples[:, 1])
plt.axvline(burn, linestyle="--", label="Burn-in")
plt.xlabel("Iteration")
plt.ylabel("Coefficient")
plt.title("Gibbs Sampling Trace Plot")
plt.legend()
plt.show()

# 8. Posterior distribution
plt.hist(posterior[:, 3], bins=30, density=True)
plt.xlabel("BMI Coefficient")
plt.ylabel("Density")
plt.title("Posterior Distribution of BMI Coefficient")
plt.show()
