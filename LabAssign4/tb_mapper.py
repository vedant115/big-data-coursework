#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(',')
    
    # Assuming columns: PatientID, Age, Gender, Symptom1, Symptom2, Symptom3...
    if len(fields) < 4:
        continue  # Skip malformed lines

    patient_id = fields[1]
    symptoms = fields[6:]  # Extracting symptoms
    
    for symptom in symptoms:
        if symptom.strip():
            print(f"{symptom.strip()}\t1")  # Emit symptom and count
