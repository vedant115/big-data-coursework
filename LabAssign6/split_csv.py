import csv
import os
import random

# Set random seed for reproducibility
random.seed(42)

input_csv = "diabetes.csv"    # Your original CSV file
train_csv = "diabetes_train.csv"
test_csv = "diabetes_test.csv"

train_ratio = 0.7  # 70% training, 30% testing

with open(input_csv, "r", newline="") as f:
    reader = list(csv.reader(f))
    header = reader[0]
    data = reader[1:]
    
# Shuffle the data
random.shuffle(data)

n_train = int(len(data) * train_ratio)
train_data = data[:n_train]
test_data = data[n_train:]

with open(train_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(train_data)

with open(test_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(test_data)

print(f"Created {train_csv} with {len(train_data)} records and {test_csv} with {len(test_data)} records.")
