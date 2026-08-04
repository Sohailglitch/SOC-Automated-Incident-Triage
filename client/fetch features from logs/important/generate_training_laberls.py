import csv
import random

# Load the existing CSV file
csv_file_path = 'output.csv'
new_csv_file_path = 'output_with_analyst.csv'

# Define the list of analysts
analysts = ['Analyst_1', 'Analyst_2', 'Analyst_3', 'Analyst_4', 'Analyst_5']

# Read data from the existing CSV file and add the Analyst column
with open(csv_file_path, mode='r') as read_file, open(new_csv_file_path, mode='w', newline='') as write_file:
    reader = csv.reader(read_file)
    writer = csv.writer(write_file)
    
    # Read and write the header row with the Analyst column added
    header = next(reader)
    header.append('Analyst')
    writer.writerow(header)

    # Write data rows with a random analyst assigned
    for row in reader:
        analyst_assigned = random.choice(analysts)
        row.append(analyst_assigned)
        writer.writerow(row)

print(f"CSV file with Analyst column saved at: {new_csv_file_path}")

