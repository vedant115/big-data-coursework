from mrjob.job import MRJob
from mrjob.step import MRStep

class MostFrequentlyUsedRooms(MRJob):

    def mapper(self, _, line):
        """Mapper: Extract room number and emit it."""
        # Skip the header row by checking if the first line matches the header format
        if line.startswith("Name,Age,Gender,Blood Type,Medical Condition,Date of Admission,Doctor,Hospital,Insurance Provider,Billing Amount,Room Number,Admission Type,Discharge Date,Medication,Test Results"):
            return
        
        # Split the line into columns
        columns = line.split(',')
        
        # Check if there are enough columns (assuming 15 columns)
        if len(columns) > 10:  # Ensure the row has at least 11 columns (Room Number is at index 10)
            try:
                # Extract room number (column index 10)
                room_number = columns[11]  # Room Number is at index 10 (11th column)
                
                # Emit the room number as the key
                yield room_number, 1
            except (ValueError, IndexError):
                # Skip rows with invalid data (e.g., missing room number)
                pass

    def reducer(self, room_number, counts):
        """Reducer: Count the occurrences of each room number."""
        # Sum up all counts for this room
        total_usage = sum(counts)
        
        # Emit the room number and its total usage count
        yield room_number, total_usage

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MostFrequentlyUsedRooms.run()
