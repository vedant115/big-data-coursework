from mrjob.job import MRJob
import csv

class SymptomTrendByYear(MRJob):

    def mapper(self, _, line):
        row = list(csv.reader([line]))[0]
        if row[0] == "no":
            return

        year = row[4].split('/')[-1]  # Extract year from date
        symptoms = row[6:]
        symptom_count = sum(int(s) for s in symptoms)

        yield year, symptom_count  # Sum all symptoms for each year

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    SymptomTrendByYear.run()
