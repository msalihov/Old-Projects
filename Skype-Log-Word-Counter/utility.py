import re
import operator
import string


config = {}
execfile('config.conf', config)
deli = config["csv_delimeter"]


def strip_characters(word):
    bad_chars = '()?[]{},./!#@\\&^$%*~`-+=_"\';:|><'
    exp = re.compile("[%s]" % bad_chars)
    word = str(word).lower()
    word = word.translate(string.maketrans("", ""), bad_chars)
    return word


def get_word_list(all_words):
    word_list = all_words.split(' ')
    index = 0
    for word in word_list:
        word_list[index] = strip_characters(word)
        index += 1
    return word_list


def sort_dictionary(dictionary):
    dict_return = sorted(dictionary.items(), key=operator.itemgetter(1))
    dict_return.reverse()
    return dict_return


def to_csv(input_list):
    index = 0
    with open(config["csv_file"], 'w') as fp:
        for item in input_list:
            index += 1
            fp.write('"' + str(item[0]) + '"' + deli + str(item[1]) + deli + str(index) + '\n')