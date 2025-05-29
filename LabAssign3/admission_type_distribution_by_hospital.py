from mrjob.job import MRJob
from mrjob.step import MRStep

class AdmissionTypeDistributionByHospital(MRJob):

    def mapper(self, _, line):
        """Mapper: Extract hospital name and admission type, skip header row."""
        # Skip the header row by checking if the first line matches the header format
        if line.startswith("Name,Age,Gender,Blood Type,Medical Condition,Date of Admission,Doctor,Hospital,Insurance Provider,Billing Amount,Room Number,Admission Type,Discharge Date,Medication,Test Results"):
            return
        
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns (assuming 15 columns)
        if len(columns) > 14:  # Ensure the row has at least 15 columns
            try:
                # Extract hospital name and admission type
                hospital = columns[7]  # Hospital is at index 7 (8th column)
                admission_type = columns[11]  # Admission Type is at index 11 (12th column)
                
                # Emit the hospital and admission type as a tuple
                yield hospital, admission_type
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., missing hospital or admission type)
                pass

    def reducer(self, hospital, admission_types):
        """Reducer: Count the number of each admission type for each hospital."""
        # Initialize a dictionary to count each admission type
        admission_count = {'Urgent': 0, 'Emergency': 0, 'Elective': 0}
        
        # Count the admission types
        for admission_type in admission_types:
            if admission_type in admission_count:
                admission_count[admission_type] += 1
        
        # Emit the hospital and the count of each admission type
        for admission_type, count in admission_count.items():
            yield hospital, (admission_type, count)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    AdmissionTypeDistributionByHospital.run()
