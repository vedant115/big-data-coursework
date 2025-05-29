from mrjob.job import MRJob
from mrjob.step import MRStep

class AverageBillingByInsuranceProvider(MRJob):

    def mapper(self, _, line):
        """Mapper: Extract insurance provider and billing amount, skip header row."""
        # Skip the header row by checking if the first line matches the header format
        if line.startswith("Name,Age,Gender,Blood Type,Medical Condition,Date of Admission,Doctor,Hospital,Insurance Provider,Billing Amount,Room Number,Admission Type,Discharge Date,Medication,Test Results"):
            return
        
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns (assuming 15 columns)
        if len(columns) > 14:  # Ensure the row has at least 15 columns
            try:
                # Extract the insurance provider and billing amount
                insurance_provider = columns[8]
                billing_amount = float(columns[9])  # Convert the billing amount to a float
                
                # Emit the insurance provider and billing amount as a tuple
                yield insurance_provider, (billing_amount, 1)  # (sum, count)
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., missing or non-numeric billing amount)
                pass

    def reducer(self, insurance_provider, values):
        """Reducer: Calculate the average billing amount for each insurance provider."""
        total_billing = 0
        count = 0
        
        # Sum up the billing amounts and count the number of records
        for billing_amount, record_count in values:
            total_billing += billing_amount
            count += record_count
        
        # Calculate the average billing amount
        if count > 0:
            average_billing = total_billing / count
            # Emit the insurance provider and its average billing amount
            yield insurance_provider, average_billing

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    AverageBillingByInsuranceProvider.run()
