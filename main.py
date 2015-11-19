import random

# Return a list of the next "words" from a file. The resulting list's size is determined by the order argument.
def get_words(order = 3):
    buffer = []
    with open("corpus.txt", "r") as f:
        for line in f:
            lines = line.split()
            buffer.extend(lines)
            while(len(buffer) > order):
                yield buffer[0:order]
                buffer.pop(0)

def populate_table():
    # Populate a dictionary with key/value pairs of words and their respective frequencies.
    markov_table = {}
    for x in get_words(3):
        key = tuple(x[:-1])
        if markov_table.get(key):
            # We've seen this n-gram before, so append the following word to the associated list in the hash.
            markov_table[key].append(x[-1])
        else:
            # This is a new n-gram.
            markov_table[key] = [x[-1]]

def markov():
    markov_table = populate_table()
