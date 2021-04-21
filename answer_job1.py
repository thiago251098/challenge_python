import re
import os

def format_text(string):
    formatedArray = re.findall('[a-zA-Z]+', string)
    return (" ".join(formatedArray))

def dictionary_word_id():
    datasets = os.listdir('dataset')
    all_words = ""
    for filename in datasets:
        with open(f"dataset/{filename}", "r") as dataset_file:
            all_words += format_text(dataset_file.read().replace("\n", ""))
    dictionary = [(word,idx) for idx, word in enumerate(list(set(all_words.split(" "))))]
    for word in dictionary:
        print(word)

dictionary_word_id()
