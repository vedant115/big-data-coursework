from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class TBSymptomCount(MRJob):
    
    def __init__(self, *args, **kwargs):
        super(TBSymptomCount, self).__init__(*args, **kwargs)
        self.symptom_headers = []

    def mapper_init(self):
        """ Called once per mapper instance to store headers """
        self.symptom_headers = []

    def mapper(self, _, line):
        reader = csv.reader([line])
        fields = next(reader)

        # If header row, store it for future use
        if not self.symptom_headers:
            self.symptom_headers = fields[6:]  # Symptoms start from column 6
            return  # Skip processing the header row

        symptoms = fields[6:]

        for i, symptom_value in enumerate(symptoms):
            symptom_name = self.symptom_headers[i].strip()  # Get symptom name
            if symptom_value.strip() == "1":
                yield symptom_name, 1

    def reducer(self, symptom, counts):
        yield symptom, sum(counts)

    def steps(self):
        return [MRStep(mapper_init=self.mapper_init, mapper=self.mapper, reducer=self.reducer)]

if __name__ == "__main__":
    TBSymptomCount.run()

