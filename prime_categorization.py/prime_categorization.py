import pandas as pd

# Load the data
data = pd.read_csv("ocd_dataset/filtered_reaction_times.csv")

# Define categorization rules based on prime type
def categorize_prime(prime):
    if prime.startswith('OCD'):
        return 'OCD-related'
    elif prime.startswith('Neutral'):
        return 'Neutral'
    else:
        return 'Other'

# Apply categorization function
data['prime_category'] = data['prime'].apply(categorize_prime)

# Save the categorized data
data.to_csv("ocd_dataset/categorized_primes.csv", index=False)

print("Prime categorization complete. Categories saved to 'categorized_primes.csv'.")
