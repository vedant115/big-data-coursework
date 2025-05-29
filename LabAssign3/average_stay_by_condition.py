from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime

class AverageStayByCondition(MRJob):

    def mapper(self, _, line):
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns
        if len(columns) < 13:
            return  # Skip rows with insufficient columns
        
        try:
            # Extract the medical condition, admission date, and discharge date
            medical_condition = columns[4]
            admission_date = datetime.strptime(columns[5], '%Y-%m-%d')
            discharge_date = datetime.strptime(columns[12], '%Y-%m-%d')
            
            # Calculate the length of stay
            length_of_stay = (discharge_date - admission_date).days
            
            # Emit the medical condition and length of stay
            yield medical_condition, length_of_stay
        except (ValueError, IndexError) as e:
            # Skip rows with invalid data (e.g., malformed dates or missing columns)
            pass

    def reducer(self, medical_condition, lengths_of_stay):
        # Convert the lengths of stay to a list
        lengths = list(lengths_of_stay)
        
        # Calculate the average length of stay
        if lengths:  # Ensure there are valid lengths to average
            average_stay = sum(lengths) / len(lengths)
            yield medical_condition, average_stay

if __name__ == '__main__':
    AverageStayByCondition.run()
