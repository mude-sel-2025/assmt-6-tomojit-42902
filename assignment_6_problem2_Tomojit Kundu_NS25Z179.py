import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def confidence_interval(N_samples=100, sample_size=30, true_mean=67, true_std=10, confidence=0.95):
    """
    Demonstrates confidence intervals for the mean.
    Parameters:
    - N_samples: Number of independent samples
    - sample_size: Number of observations per sample
    - true_mean: True population mean
    - true_std: True population standard deviation
    - confidence: Confidence level (default 0.95)
    """
    
    # Z value for the two-tailed confidence interval
    alpha = 1 - confidence
    z = norm.ppf(1 - alpha/2)   # e.g. ~1.96 for 95%
    
    # Store the lower and upper bounds of each CI
    ci_lowers = []
    ci_uppers = []
    
    # Track intervals that do NOT contain the true mean
    misses = 0
    
    # Generate samples and compute CIs
    for i in range(N_samples):
        sample = np.random.normal(loc=true_mean, scale=true_std, size=sample_size)

        # Sample mean and standard error (σ known)
        sample_mean = np.mean(sample)
        sample_se = true_std / np.sqrt(sample_size)
        
        # CI bounds
        lower = sample_mean - z * sample_se
        upper = sample_mean + z * sample_se

        # append to CI lists        
        ci_lowers.append(lower)
        ci_uppers.append(upper)
        
        # Check if the true mean is inside the CI
        if  (lower <= true_mean <= upper):
            misses += 1
    
    # Plot the CIs
    plt.figure(figsize=(8, 6))
    for i, (low, up) in enumerate(zip(ci_lowers, ci_uppers)):
        # Red if CI misses the true mean, blue otherwise
        color = 'red' if not (low <= true_mean <= up) else 'blue'

        plt.plot([low, up], [i, i], color=color, lw=2)
        plt.plot([np.mean([low, up])], [i], 'o', color=color)  # mark sample mean
    
    plt.axvline(true_mean, color='magenta', linestyle='-', label='True Mean', lw=3)
    plt.xlabel("Value")
    plt.ylabel("Sample #")
    plt.title(f"{confidence*100:.0f}% Confidence Intervals for Sample Means\nMissed intervals: {misses}/{N_samples}")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Print results
    print(f"Out of {N_samples} intervals, {misses} did NOT contain the true mean.")
    print(f"This is roughly {misses/N_samples*100:.2f}%, close to the expected {alpha*100:.2f}% for a {confidence*100:.0f}% CI.")

# ================================
# Run main if this script is executed
# ================================
if __name__ == "__main__":
    confidence_interval()
    plt.show()  # do not comment this out
