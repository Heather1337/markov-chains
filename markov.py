"""Generate Markov text from text files."""


import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path)
    opened_file_text_string = opened_file.read()

    return opened_file_text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text_list = text_string.split()
    for i in range(0, len(text_list) + 1):
        if i <= (len(text_list) - 4):
            word1_word2_tuple = (text_list[i], text_list[i + 1])
            word3 = text_list[i + 2]
            if not word1_word2_tuple in chains:
                chains[word1_word2_tuple] = [word3]
            else:
                chains[word1_word2_tuple].append(word3)
        if i == (len(text_list) - 1):
            word1_word2_tuple = (text_list[i - 2], text_list[i - 1])
            word3 = text_list[i]
            if word1_word2_tuple in chains:
                chains[word1_word2_tuple].append(word3)
            else:
                chains[word1_word2_tuple] = [word3]
        

    return chains


def make_text(chains):
    """Return text from chains."""

    chains_keys = list(chains.keys())
    current_key = random.choice(chains_keys)
    chosen_word = None 
    words = [current_key[0], current_key[1]]

    while(current_key in chains):
        chosen_word = chains[current_key][random.randint(0, len(chains[current_key]) - 1)]
        words.append(chosen_word)
        current_key = (current_key[1], chosen_word)
        print(current_key)
    

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
