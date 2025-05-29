from mrjob.job import MRJob
from mrjob.step import MRStep

class MostCommonConditionByAgeGroup(MRJob):

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
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns
        if len(columns) > 4:  # Ensure the row has at least 5 columns (Name, Age, Gender, Blood Type, Medical Condition)
            try:
                # Extract age and medical condition
                age = int(columns[1])
                medical_condition = columns[4]
                
                # Classify the patient into an age group
                age_group = self.age_group(age)
                
                # Emit the age group and medical condition as a tuple
                yield (age_group, medical_condition), 1
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., non-integer age or missing columns)
                pass

    def reducer(self, key, counts):
        # Sum the counts for each (age group, medical condition) pair
        total_count = sum(counts)
        
        # Emit the (age group, medical condition) tuple and total count
        yield key[0], (key[1], total_count)  # Emit age group and the condition with its total count

    def reducer_find_max(self, age_group, condition_count_pairs):
        # Convert the condition_count_pairs to a list
        condition_count_pairs = list(condition_count_pairs)
        
        try:
            # Ensure condition_count_pairs is not empty
            if not condition_count_pairs:
                print(f"Warning: No data for age group {age_group}")
                return
            
            # Find the medical condition with the highest count in this age group
            max_condition, max_count = max(condition_count_pairs, key=lambda x: x[1])
            
            # Emit the age group and the most common medical condition with its count
            yield age_group, (max_condition, max_count)
        except Exception as e:
            print(f"Error in reducer_find_max: {e}")
            raise

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_find_max)
        ]

if __name__ == '__main__':
    MostCommonConditionByAgeGroup.run()

