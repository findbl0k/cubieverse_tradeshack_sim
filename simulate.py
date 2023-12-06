import pandas as pd
import random

# Function to simulate resource drops for a given cubie
def simulate_drops(resources, quantities, market_values, iterations=10000000):
    drop_count = {resource: 0 for resource in resources}
    for _ in range(iterations):
        if random.random() < 0.02:  # 2% chance of a drop
            chosen_resource = random.choice(resources)
            drop_count[chosen_resource] += quantities[resources.index(chosen_resource)] / 2  # Half of the resource quantity

    expected_value = sum(drop_count[resource] * market_values[resource] for resource in resources) / iterations
    return expected_value

# Load CSV data
cubies_df = pd.read_csv('cubies.csv')
resources_df = pd.read_csv('resources.csv')

# Convert resource prices to a dictionary
market_values = {row['x1']: row['v1'] for _, row in resources_df.iterrows()}

# Process each cubie and calculate expected value
def process_cubie(row):
    resources = [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])]
    quantities = [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])]
    return simulate_drops(resources, quantities, market_values)

cubies_df['expected_value'] = cubies_df.apply(process_cubie, axis=1)

# Sort the cubies by expected value in descending order
sorted_cubies_df = cubies_df.sort_values('expected_value', ascending=False)

# Drop unnecessary columns
sorted_cubies_df = sorted_cubies_df.drop(['n1', 'r1', 'n2', 'r2', 'n3', 'r3'], axis=1)

# Print sorted expected values
print(sorted_cubies_df[['cubie', 'expected_value']])

# Determine and print the best cubie
best_cubie = sorted_cubies_df.iloc[0]['cubie']
print("Best Cubie:", best_cubie)

# Save the filtered data to a new CSV file
sorted_cubies_df.to_csv('cubie_TS_drop_values.csv', index=False)