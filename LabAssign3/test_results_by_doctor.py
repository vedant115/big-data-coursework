from mrjob.job import MRJob
from mrjob.step import MRStep

class TestResultsByDoctor(MRJob):

    def mapper(self, _, line):
        """Mapper: Extract doctor name and test result, skip header row."""
        # Skip the header row by checking if the first line matches the header format
        if line.startswith("Name,Age,Gender,Blood Type,Medical Condition,Date of Admission,Doctor,Hospital,Insurance Provider,Billing Amount,Room Number,Admission Type,Discharge Date,Medication,Test Results"):
            return
        
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns (assuming 15 columns)
        if len(columns) > 14:  # Ensure the row has at least 15 columns
            try:
                # Extract doctor name and test result
                doctor = columns[6]  # Doctor's name is at index 6 (7th column)
                test_result = columns[14]  # Test Result is at index 14 (15th column)
                
                # Emit the doctor and test result as a tuple
                yield doctor, test_result
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., missing doctor or test result)
                pass

    def reducer(self, doctor, test_results):
        """Reducer: Count the occurrences of each test result type for each doctor."""
        # Initialize counters for each test result type
        result_count = {'Normal': 0, 'Abnormal': 0, 'Inconclusive': 0}
        total_count = 0
        
        # Count the occurrences of each test result
        for test_result in test_results:
            if test_result in result_count:
                result_count[test_result] += 1
                total_count += 1
        
        # Calculate the percentage for each test result type
        if total_count > 0:
            normal_percentage = (result_count['Normal'] / total_count) * 100
            abnormal_percentage = (result_count['Abnormal'] / total_count) * 100
            inconclusive_percentage = (result_count['Inconclusive'] / total_count) * 100
        else:
            normal_percentage = abnormal_percentage = inconclusive_percentage = 0
        
        # Emit the doctor name and the percentage of each test result
        yield doctor, (normal_percentage, abnormal_percentage, inconclusive_percentage)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    TestResultsByDoctor.run()
