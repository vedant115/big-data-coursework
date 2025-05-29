from mrjob.job import MRJob
import csv
from itertools import combinations

class SymptomCorrelation(MRJob):

    def mapper(self, _, line):
        row = list(csv.reader([line]))[0]
        if row[0] == "no":
            return

        symptoms = row[6:]
        active_symptoms = [i for i, s in enumerate(symptoms) if s == "1"]

        # Generate symptom pairs
        for pair in combinations(active_symptoms, 2):
            yield pair, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    SymptomCorrelation.run()
