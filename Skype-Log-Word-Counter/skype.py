import re

import utility


config = {}
execfile('config.conf', config)

pattern = re.compile("\[[0-3][0-9]\.[01][0-9]\.[0-9]{1,4}\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\]\s.+")
previous_message = ""
previous_sender = ""

words = {}

with open(config["input"]) as f:
    for line in f:
        if pattern.match(line):
            without_date = line.split('] ', 1)[1].strip()
            if ': ' in without_date:
                sender = without_date.split(': ', 1)[0].strip()
                message = without_date.split(': ', 1)[1].strip()
                if config["verbose"]:
                    print 'Sender: ' + sender
                    print 'Message: ' + message
                previous_sender = sender
                previous_message = message
                word_list = utility.get_word_list(message)
                for word in word_list:
                    if word not in words:
                        words[word] = 1
                    else:
                        words[word] += 1

sorted_words = utility.sort_dictionary(words)
print sorted_words

if config["csv_output"]:
    utility.to_csv(sorted_words)