import csv
from mrjob.job import MRJob
from mrjob.step import MRStep

class TotalBillingByHospital(MRJob):

    def mapper(self, _, line):
        # Use csv.reader to properly handle commas within quoted fields
        reader = csv.reader([line])
        for columns in reader:
            if len(columns) > 9:  # Check that there are enough columns
                hospital = columns[7]
                try:
                    billing_amount = float(columns[9])
                    yield hospital, billing_amount
                except ValueError:
                    pass  # Skip rows with invalid billing amounts

    def reducer(self, hospital, billing_amounts):
        total_billing = sum(billing_amounts)
        yield hospital, total_billing

if __name__ == '__main__':
    TotalBillingByHospital.run()

