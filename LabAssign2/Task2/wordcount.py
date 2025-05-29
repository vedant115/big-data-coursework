import sys
from collections import defaultdict

# Mapper: reads input from stdin
def mapper():
    for line in sys.stdin:
        # Split each line into words and output each word with a count of 1
        for word in line.strip().split():
            print(f"{word}\t1")

# Reducer: reads input from stdin (sorted key-value pairs)
def reducer():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        word, count = line.strip().split("\t")
        count = int(count)

        if word == current_word:
            current_count += count
        else:
            if current_word:
                print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = count

    # Output the last word if necessary
    if current_word:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    mapper()  # Call mapper or reducer based on the script logic

