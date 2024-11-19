import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import factorial  # Import factorial from scipy.special
from scipy.stats import poisson      # Optional: Import poisson for PMF

# Read data from the file
data = np.loadtxt('em_data.txt')

# Ensure data contains integer values
if not np.all(np.equal(np.mod(data, 1), 0)):
    raise ValueError("Data contains non-integer values. Factorial is undefined for non-integers.")

# Exploratory Data Analysis (EDA)
# Compute basic statistics
mean_data = np.mean(data)
var_data = np.var(data)
print(f"Mean of data: {mean_data}")
print(f"Variance of data: {var_data}")

# Plot histogram of the data
plt.hist(data, bins=range(int(max(data)) + 2), edgecolor='black', alpha=0.7, align='left')  # Adjust bins for better alignment
plt.title('Histogram of Number of Children in Families')
plt.xlabel('Number of Children')
plt.ylabel('Frequency')
plt.savefig('data_histogram.png')
plt.close()

# EM Algorithm for Poisson Mixture Model
# Initialize parameters
np.random.seed(0)
lambda1 = np.random.uniform(0, mean_data)
lambda2 = np.random.uniform(mean_data, max(data))
pi = 0.5  # Mixing proportion for families with family planning

# Convergence criteria
tol = 1e-6
max_iter = 1000
log_likelihood_old = -np.inf

for iteration in range(max_iter):
    # E-step: Compute responsibilities
    # Probability of data given lambda1 and lambda2 using scipy's poisson.pmf
    # This avoids manually computing factorials
    poisson_lambda1 = poisson.pmf(data, lambda1)
    poisson_lambda2 = poisson.pmf(data, lambda2)

    # Compute weights (posterior probabilities)
    gamma = pi * poisson_lambda1 / (pi * poisson_lambda1 + (1 - pi) * poisson_lambda2)

    # M-step: Update parameters
    lambda1_new = np.sum(gamma * data) / np.sum(gamma)
    lambda2_new = np.sum((1 - gamma) * data) / np.sum(1 - gamma)
    pi_new = np.mean(gamma)

    # Compute log-likelihood
    # To prevent log(0), add a small epsilon
    epsilon = 1e-10
    log_likelihood_new = np.sum(np.log(pi * poisson_lambda1 + (1 - pi) * poisson_lambda2 + epsilon))

    # Check convergence
    if abs(log_likelihood_new - log_likelihood_old) < tol:
        print(f"Converged at iteration {iteration + 1}")
        break

    # Update parameters for next iteration
    lambda1 = lambda1_new
    lambda2 = lambda2_new
    pi = pi_new
    log_likelihood_old = log_likelihood_new

    if (iteration + 1) % 10 == 0 or iteration == 0:
        print(f"Iteration {iteration + 1}:")
        print(f"    lambda1 = {lambda1}")
        print(f"    lambda2 = {lambda2}")
        print(f"    pi = {pi}")
        print(f"    Log-Likelihood = {log_likelihood_new}")

else:
    print("Reached maximum iterations without convergence.")

# Final estimated parameters
print("\nEstimated Parameters:")
print(f"Mean number of children in families with family planning advice (lambda1): {lambda1}")
print(f"Mean number of children in families without family planning advice (lambda2): {lambda2}")
print(f"Proportion of families with family planning advice (pi): {pi}")
print(f"Proportion of families without family planning advice: {1 - pi}")
