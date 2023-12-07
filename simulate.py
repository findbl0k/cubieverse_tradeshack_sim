import pandas as pd
import random

# Function to simulate resource drops for a given cubie
def simulate_drops(resources, quantities, market_values, iterations=1000000):
    drop_count = {resource: 0 for resource in resources}
    for _ in range(iterations):
        if random.random() < 0.02:  # 2% chance of a drop
            chosen_resource = random.choice(resources)
            drop_count[chosen_resource] += quantities[resources.index(chosen_resource)] / 2  # Half of the resource quantity

    simulated_value = sum(drop_count[resource] * market_values[resource] for resource in resources) / iterations
    return simulated_value

#  Function to calculate expected value for a given cubie
def calculate_expected_value(row, market_values):
    resources = [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])]
    quantities = [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])]
    total_value = sum(quantities[i]/2 * market_values[resources[i]] for i in range(len(resources)))
    num_resources = len(resources)
    return 0.02 * total_value / num_resources if num_resources > 0 else 0

# Load CSV data
cubies_df = pd.read_csv('cubies.csv')
resources_df = pd.read_csv('resources.csv')

# Convert resource prices to a dictionary
market_values = {row['x1']: row['v1'] for _, row in resources_df.iterrows()}

cubies_df['expected_value'] = cubies_df.apply(lambda row: calculate_expected_value(row, market_values), axis=1)

# Process each cubie and calculate simulated and expected values
cubies_df['simulated_value100'] = cubies_df.apply(
    lambda row: simulate_drops(
        [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])],
        [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])],
        market_values, 100
    ),
    axis=1
)

# Process each cubie and calculate simulated and expected values
cubies_df['simulated_value500'] = cubies_df.apply(
    lambda row: simulate_drops(
        [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])],
        [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])],
        market_values, 500
    ),
    axis=1
)

# Process each cubie and calculate simulated and expected values
cubies_df['simulated_value1000'] = cubies_df.apply(
    lambda row: simulate_drops(
        [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])],
        [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])],
        market_values, 1000
    ),
    axis=1
)

# Process each cubie and calculate simulated and expected values
cubies_df['simulated_value5000'] = cubies_df.apply(
    lambda row: simulate_drops(
        [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])],
        [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])],
        market_values, 5000
    ),
    axis=1
)

# Process each cubie and calculate simulated and expected values
cubies_df['simulated_value10000'] = cubies_df.apply(
    lambda row: simulate_drops(
        [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])],
        [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])],
        market_values, 10000
    ),
    axis=1
)

# Process each cubie and calculate simulated and expected values
cubies_df['simulated_value100000'] = cubies_df.apply(
    lambda row: simulate_drops(
        [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])],
        [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])],
        market_values, 100000
    ),
    axis=1
)

# Process each cubie and calculate simulated and expected values
cubies_df['simulated_value10000000'] = cubies_df.apply(
    lambda row: simulate_drops(
        [row[f'r{i}'] for i in range(1, 4) if pd.notna(row[f'r{i}'])],
        [row[f'n{i}'] for i in range(1, 4) if pd.notna(row[f'n{i}'])],
        market_values, 10000000
    ),
    axis=1
)

# Sort the cubies by simulated value in descending order
sorted_cubies_df = cubies_df.sort_values('expected_value', ascending=False)

# Drop unnecessary columns
final_df = sorted_cubies_df.drop(['n1', 'r1', 'n2', 'r2', 'n3', 'r3'], axis=1)

# Print sorted values
print(final_df[['cubie','expected_value', 'simulated_value100', 'simulated_value500', 'simulated_value1000', 'simulated_value5000', 'simulated_value10000', 'simulated_value100000', 'simulated_value10000000']])

# Save the filtered data to a new CSV file
final_df.to_csv('cubie_TS_drop_values.csv', index=False)