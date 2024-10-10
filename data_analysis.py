import pandas as pd

# Load the data
data = pd.read_csv("ocd_dataset/reaction_times.csv")

# Filter RT values (e.g., exclude RTs < 300 ms and > 2000 ms)
filtered_data = data[(data['key_resp.rt'] > 0.3) & (data['key_resp.rt'] < 2.0)]

# Save filtered data
filtered_data.to_csv("ocd_dataset/filtered_reaction_times.csv", index=False)

print(f"Filtered {len(data) - len(filtered_data)} outliers based on reaction time.")