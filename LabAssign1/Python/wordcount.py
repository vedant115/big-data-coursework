#!/usr/bin/env python3
import sys

def mapper():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print("{}\t1".format(word))

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
                print("{}\t{}".format(current_word, current_count))
            current_word = word
            current_count = count

    if current_word:
        print("{}\t{}".format(current_word, current_count))

if __name__ == "__main__":
    if sys.argv[1] == "mapper":
        mapper()
    elif sys.argv[1] == "reducer":
        reducer()
