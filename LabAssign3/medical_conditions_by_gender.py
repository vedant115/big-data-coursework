from mrjob.job import MRJob
from mrjob.step import MRStep

class MedicalConditionsByGender(MRJob):

    def mapper(self, _, line):
        """Mapper: Extract gender and medical condition, skip header row."""
        # Skip the header row by checking if the first line matches the header format
        if line.startswith("Name,Age,Gender,Blood Type,Medical Condition,Date of Admission,Doctor,Hospital,Insurance Provider,Billing Amount,Room Number,Admission Type,Discharge Date,Medication,Test Results"):
            return
        
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns (assuming 15 columns)
        if len(columns) > 14:  # Ensure the row has at least 15 columns
            try:
                # Extract gender and medical condition
                gender = columns[2]  # Gender is at index 2 (3rd column)
                medical_condition = columns[4]  # Medical Condition is at index 4 (5th column)
                
                # Emit the gender and medical condition as a tuple
                yield gender, medical_condition
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., missing gender or medical condition)
                pass

    def reducer(self, gender, medical_conditions):
        """Reducer: Count the occurrences of each medical condition by gender."""
        # Initialize a dictionary to count each medical condition
        condition_count = {}
        
        # Count the occurrences of each medical condition
        for medical_condition in medical_conditions:
            if medical_condition in condition_count:
                condition_count[medical_condition] += 1
            else:
                condition_count[medical_condition] = 1
        
        # Emit the gender and the count of each medical condition
        for medical_condition, count in condition_count.items():
            yield (gender, medical_condition), count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MedicalConditionsByGender.run()
