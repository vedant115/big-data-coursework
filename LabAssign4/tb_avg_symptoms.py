from mrjob.job import MRJob
import csv

class AvgSymptomsPerPatient(MRJob):

    def mapper(self, _, line):
        row = list(csv.reader([line]))[0]
        if row[0] == "no":
            return

        symptoms = row[6:]  # Symptoms columns
        symptom_count = sum(int(s) for s in symptoms)  # Count symptoms per patient
        yield "TotalSymptoms", symptom_count
        yield "TotalPatients", 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    AvgSymptomsPerPatient.run()
