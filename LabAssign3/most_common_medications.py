from mrjob.job import MRJob
from mrjob.step import MRStep

class MostCommonMedications(MRJob):

    def mapper(self, _, line):
        """Mapper: Extract medical condition and prescribed medication."""
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns (assuming 6 columns)
        if len(columns) > 5:  # Ensure the row has at least 6 columns (Name, Age, Gender, Blood Type, Medical Condition, Medication)
            try:
                # Extract the medical condition and medication prescribed
                medical_condition = columns[4]
                medication = columns[13]
                
                # Emit the (medical_condition, medication) pair with a count of 1
                yield (medical_condition, medication), 1
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., missing columns)
                pass

    def reducer(self, key, counts):
        """Reducer: Count the occurrences of each medication for each medical condition."""
        # Sum the counts for each (medical_condition, medication) pair
        total_count = sum(counts)
        
        # Emit the (medical_condition, medication) pair with the total count
        yield key[0], (key[1], total_count)  # Emit the medical condition and medication with the count

    def reducer_find_max(self, medical_condition, medication_count_pairs):
        """Reducer to find the most prescribed medication for each condition."""
        # Convert the medication_count_pairs to a list
        medication_count_pairs = list(medication_count_pairs)
        
        try:
            # Ensure medication_count_pairs is not empty
            if not medication_count_pairs:
                print(f"Warning: No medications for condition {medical_condition}")
                return
            
            # Find the medication with the highest count for this condition
            max_medication, max_count = max(medication_count_pairs, key=lambda x: x[1])
            
            # Emit the medical condition and the most prescribed medication with its count
            yield medical_condition, (max_medication, max_count)
        except Exception as e:
            print(f"Error in reducer_find_max: {e}")
            raise

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_find_max)
        ]

if __name__ == '__main__':
    MostCommonMedications.run()
