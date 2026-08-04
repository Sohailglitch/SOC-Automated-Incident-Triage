# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:15:43 2024

@author: Lenovo
"""

import pandas as pd
import random

# Define possible rule description values
possible_rule_descriptions = [
    "Log file rotated.",
    "Listened ports status (netstat) changed (new port opened or closed).",
    "File modified.",
    "Network traffic anomaly detected.",
    "Unauthorized access attempt detected."
]

# Define possible analyst values
possible_analysts = ['Analyst_1', 'Analyst_2', 'Analyst_3', 'Analyst_4', 'Analyst_5']

# Generate random data for the dataset
data = {
    'Rule Description': [random.choice(possible_rule_descriptions) for _ in range(1000)],
    'Level': [random.randint(1, 5) for _ in range(1000)],  # Assuming levels are integers between 1 and 5
    'Analyst': [random.choice(possible_analysts) for _ in range(1000)]  # Randomly assign analysts
}

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'generated_dataset.csv'
df.to_csv(csv_file_path, index=False)

print(f"Generated dataset saved at: {csv_file_path}")
