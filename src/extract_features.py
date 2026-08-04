# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:41:40 2024

@author: Lenovo
"""

import re
import csv

# Load JSON data from file
file_path = "E:/CUTM SSU PROJECTS/AUTOMATED INCIDENT TRIAGE/client/fetch features from logs/wazuhalertsjson.txt"
with open(file_path, 'r') as file:
    content = file.read()

# Define regex patterns
timestamp_pattern = r'"timestamp":"(.*?)"'
rule_description_pattern = r'"description":"(.*?)"'
level_pattern = r'"level":(\d+)'

# Find all matches using regex
timestamps = re.findall(timestamp_pattern, content)
rule_descriptions = re.findall(rule_description_pattern, content)
levels = re.findall(level_pattern, content)

# Ensure all lists have the same length
data_length = min(len(rule_descriptions), len(levels))

# Define the CSV file path
csv_file_path = 'output.csv'

# Write data to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Rule Description', 'Level'])

    # Write data rows
    for i in range(data_length):
        # Concatenate elements into strings
        timestamp_str = timestamps[i] if i < len(timestamps) else ''
        rule_description_str = rule_descriptions[i] if i < len(rule_descriptions) else ''
        level_str = levels[i] if i < len(levels) else ''

        # Write concatenated strings to CSV for Timestamp, Rule Description, and Level columns only
        writer.writerow([rule_description_str, level_str])

print(f"CSV file saved at: {csv_file_path}")
