import random
import sys
import time

def generate_random_sentence(number_of_words):
    with open('76-0.txt', 'r') as f:
        first_time = time.time()
        second_time = time.time()
        reading_time = second_time - first_time
        all_words_array = f.read().split()
        output = []
        sentence_array = []
        count_of_words = len(all_words_array)
        for index in range(int(number_of_words)):
            rand_num = random.randint(0, count_of_words)
            sentence_array.append(all_words_array[rand_num])

        sentence = ' '.join(sentence_array)
        third_time = time.time()
        fxn_time = time.time() - first_time



        return (sentence)







if __name__ == '__main__':
    inputted = sys.argv[1:]
    word_count = int(inputted[0])
    sentence = generate_random_sentence()
    print(sentence)
