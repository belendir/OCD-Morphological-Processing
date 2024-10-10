import pandas as pd
from scipy import stats

# Load OCD and healthy datasets
ocd_data = pd.read_csv("ocd_dataset/categorized_primes.csv")
healthy_data = pd.read_csv("healthy_dataset/categorized_primes.csv")

# Compute average RTs
ocd_avg_rt = ocd_data['key_resp.rt'].mean()
healthy_avg_rt = healthy_data['key_resp.rt'].mean()

# Perform a t-test to compare the RTs
t_stat, p_value = stats.ttest_ind(ocd_data['key_resp.rt'], healthy_data['key_resp.rt'])

# Print results
print(f"OCD group average RT: {ocd_avg_rt:.3f} seconds")
print(f"Healthy group average RT: {healthy_avg_rt:.3f} seconds")
print(f"T-statistic: {t_stat:.3f}, P-value: {p_value:.3f}")

if p_value < 0.05:
    print("The difference in reaction times between OCD and healthy participants is statistically significant.")
else:
    print("No significant difference in reaction times between OCD and healthy participants.")
