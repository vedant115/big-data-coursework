from mrjob.job import MRJob
import csv

class SymptomGenderAnalysis(MRJob):
    
    def mapper(self, _, line):
        row = list(csv.reader([line]))[0]
        if row[0] == "no":  # Skip header
            return
        
        gender = row[3]  # Gender column
        symptoms = row[6:]  # Symptoms start from 6th column

        for i, symptom in enumerate(symptoms):
            if symptom == "1":  # Count only present symptoms
                yield (f"{gender}_{i}", 1)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    SymptomGenderAnalysis.run()
