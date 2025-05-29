import csv
import os

def convert_csv_to_docs(input_csv, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(input_csv, "r", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            # Create a richer representation to help tokenization.
            # For each field, we prefix the field name to the value.
            tokens = []
            for field in reader.fieldnames:
                tokens.append(f"{field}:{row[field]}")
            content = " ".join(tokens)
            # Use the Outcome field as the label for the filename.
            label = row["Outcome"]
            filename = os.path.join(output_dir, f"{label}_{i:04d}.txt")
            with open(filename, "w") as out:
                out.write(content)

# Convert training CSV to documents
convert_csv_to_docs("diabetes_train.csv", "diabetes_docs_train")
# Convert testing CSV to documents
convert_csv_to_docs("diabetes_test.csv", "diabetes_docs_test")

print("Conversion to documents complete.")
