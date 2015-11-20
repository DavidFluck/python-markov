import argparse
import random

# Return a list of the next "words" from a file. The resulting list's size is determined by the order argument.
def get_words(filenames, order):
    buffer = []
    for file in filenames:
        with open(file, 'r') as f:
            for line in f:
                lines = line.split()
                buffer.extend(lines)
                while(len(buffer) > order):
                    yield buffer[0:order]
                    buffer.pop(0)

def populate_table(filenames, order):
    # Populate a dictionary with key/value pairs of words and the word that follows immediately after.
    markov_table = {}
    for x in get_words(filenames, order):
        key = tuple(x[:-1])
        if markov_table.get(key):
            # We've seen this n-gram before, so append the following word to the associated list in the hash.
            markov_table[key].append(x[-1])
        else:
            # This is a new n-gram.
            markov_table[key] = [x[-1]]

    return markov_table

def markov(filenames, order = 4):
    markov_table = populate_table(filenames, order)

    # Choose a random starting state and next word.
    random_state = random.choice(list(markov_table.keys()))
    initial_next_word = random.choice(markov_table[random_state])

    word_list = list(random_state) + [initial_next_word]
    print(' '.join(word_list), end=' ')

    for x in range(1,500):
        # Choose the next word.
        next_state = tuple(word_list[-(order - 1):])
        next_word = random.choice(markov_table[next_state])

        word_list = list(next_state) + [next_word]
        print("{} ".format(next_word), end='')

# Handle command-line parsing.
parser = argparse.ArgumentParser()
parser.add_argument('filenames', nargs='+')
args = parser.parse_args()

markov(args.filenames)
