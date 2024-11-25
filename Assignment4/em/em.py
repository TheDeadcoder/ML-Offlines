import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import factorial  
from scipy.stats import poisson      

markdown_content = "# Dataset details:\n"
data = np.loadtxt('em_data_online_1.txt')


if not np.all(np.equal(np.mod(data, 1), 0)):
    raise ValueError("Data contains non-integer values. Factorial is undefined for non-integers.")


mean_data = np.mean(data)
var_data = np.var(data)
markdown_content += f"Mean of data: {mean_data}\n"
markdown_content += f"Variance of data: {var_data}\n\n"

plt.hist(data, bins=range(int(max(data)) + 2), edgecolor='black', alpha=0.7, align='left')  
plt.title('Histogram of Number of Children in Families')
plt.xlabel('Number of Children')
plt.ylabel('Frequency')
plt.savefig('data_histogram.png')
plt.close()


np.random.seed(0)
lambda1 = np.random.uniform(0, mean_data)
lambda2 = np.random.uniform(mean_data, max(data))
pi = 0.5  

markdown_content += "# EM Algorithm Iteration Details\n\n"
markdown_content += "| Iteration | Lambda1 | Lambda2 | Pi | Log-Likelihood |\n"
markdown_content += "|-----------|---------|---------|----|----------------|\n"

# Convergence criteria
tol = 1e-6
max_iter = 1000
log_likelihood_old = -np.inf

for iteration in range(max_iter):
    poisson_lambda1 = poisson.pmf(data, lambda1)
    poisson_lambda2 = poisson.pmf(data, lambda2)

    # Computing weights (posterior probabilities)
    gamma = pi * poisson_lambda1 / (pi * poisson_lambda1 + (1 - pi) * poisson_lambda2)

    # M-step: Updating parameters
    lambda1_new = np.sum(gamma * data) / np.sum(gamma)
    lambda2_new = np.sum((1 - gamma) * data) / np.sum(1 - gamma)
    pi_new = np.mean(gamma)

    # Compute log-likelihood
    epsilon = 1e-10
    log_likelihood_new = np.sum(np.log(pi * poisson_lambda1 + (1 - pi) * poisson_lambda2 + epsilon))

    markdown_content += f"| {iteration + 1} | {lambda1_new:.3f} | {lambda2_new:.3f} | {pi_new:.3f} | {log_likelihood_new:.3f} |\n"

    # Checking for convergence
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


print("\nEstimated Parameters:")
print(f"Mean number of children in families with family planning advice (lambda1): {lambda1}")
print(f"Mean number of children in families without family planning advice (lambda2): {lambda2}")
print(f"Proportion of families with family planning advice (pi): {pi}")
print(f"Proportion of families without family planning advice: {1 - pi}")

markdown_content += "\n# Estimated Parameters\n\n"
markdown_content += "| Parameter | Value |\n"
markdown_content += "|-----------|-------|\n"
markdown_content += f"| Mean number of children in families with family planning advice (lambda1) | {lambda1:.3f} |\n"
markdown_content += f"| Mean number of children in families without family planning advice (lambda2) | {lambda2:.3f} |\n"
markdown_content += f"| Proportion of families with family planning advice (pi) | {pi:.3f} |\n"
markdown_content += f"| Proportion of families without family planning advice | {1 - pi:.3f} |\n"

file_path = "em_algorithm_iterations_online.md"
with open(file_path, "w") as md_file:
    md_file.write(markdown_content)


