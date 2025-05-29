from mrjob.job import MRJob
from mrjob.step import MRStep

class AgeGroupBillingAnalysis(MRJob):

    def age_group(self, age):
        """Classify patients into age groups."""
        if age <= 18:
            return "0-18"
        elif 19 <= age <= 35:
            return "19-35"
        elif 36 <= age <= 50:
            return "36-50"
        else:
            return "51+"

    def mapper(self, _, line):
        """Mapper: Extract age group and billing amount."""
        # Skip the header row by checking if the first line matches the header format
        if line.startswith("Name,Age,Gender,Blood Type,Medical Condition,Date of Admission,Doctor,Hospital,Insurance Provider,Billing Amount,Room Number,Admission Type,Discharge Date,Medication,Test Results"):
            return
        
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns (assuming 15 columns)
        if len(columns) > 9:  # Ensure the row has at least 10 columns (Age and Billing Amount are present in column 1 and 9)
            try:
                # Extract age (column index 1) and billing amount (column index 9)
                age = int(columns[1])
                billing_amount = float(columns[9])
                
                # Classify the patient into an age group
                age_group = self.age_group(age)
                
                # Emit the age group and billing amount
                yield age_group, (billing_amount, 1)
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., non-integer age, missing billing amount)
                pass

    def reducer(self, age_group, values):
        """Reducer: Calculate the average billing amount for each age group."""
        total_billing = 0
        total_count = 0
        
        # Sum up the billing amounts and counts for each age group
        for billing_amount, count in values:
            total_billing += billing_amount
            total_count += count
        
        # Calculate the average billing amount
        if total_count > 0:
            average_billing = total_billing / total_count
            yield age_group, average_billing

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    AgeGroupBillingAnalysis.run()

