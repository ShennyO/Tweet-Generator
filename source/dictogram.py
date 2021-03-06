#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random
import pdb

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        # self.markov_dictionary = {}
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
        self.words = word_list
        # self.set_markov()
        # self.total_counts = {}
        # self.generate_sentence()

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        if word not in self:
            self[word] = count
            self.tokens +=count
            self.types +=1
        else:
            self[word] +=count
            self.tokens +=count

    # def set_markov(self):
    #     for index, word in enumerate(self.words):
    #         if word not in self.markov_dictionary:
    #             selected_index = index
    #             next_word = self.words[selected_index + 1]
    #             self.markov_dictionary[word] = {next_word: 1}
    #         else:
    #             selected_index = index
    #             if index < len(self.words) -1:
    #                 next_word = self.words[selected_index + 1]
    #                 if next_word not in self.markov_dictionary[word]:
    #                     self.markov_dictionary[word][next_word] =1
    #                 else:
    #                     self.markov_dictionary[word][next_word]+=1
    #     print(self.markov_dictionary)

    # def generate_sentence(self):
    #     sentence = []
    #     random_index = random.randint(0, len(self.words) -1)
    #     selected_word = self.words[random_index]
    #
    #     n = 0
    #     while (n < 10):
    #         sentence.append(selected_word)
    #         next_word_choices = self.markov_dictionary[selected_word]
    #         random_num = random.randint(0, len(self.words) -1)
    #         selected_word = random.choice(next_word_choices)
    #         n+=1
    #     joined_sentence = ' '.join(sentence)
    #     print("sentence: %s" % joined_sentence)



    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word not in self:
            return 0
        else:
            return self[word]


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    print('dictionary: {}'.format(histogram.markov_dictionary))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
