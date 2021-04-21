import re
import os

def format_text(string):
    formatedArray = re.findall('[a-zA-Z]+', string)
    return (" ".join(formatedArray))

def dictionary_reverse():
    datasets = os.listdir('dataset')
    all_words = ""
    for filename in datasets:
        with open(f"dataset/{filename}", "r") as dataset_file:
            all_words += format_text(dataset_file.read().replace("\n", ""))

    dictionary = {word:idx for idx, word in enumerate(list(set(all_words.split(" "))))} # na variavel dictionary contém o “match” de cada palavra contida nos documentos com um identificador único “word_id”, conforme figura 2.
    reverse_index = []
    count = 0
    for word_id in dictionary:
        word_file_list = []
        for filename in datasets:
            with open(f"dataset/{filename}", "r") as dataset_file:
                data = format_text(dataset_file.read().replace("\n", ""))

            if data.find(word_id):
                word_file_list.append(filename)
        tuple_word = (dictionary[word_id], sorted(word_file_list))
        reverse_index.append(tuple_word)
        count += 1
        print(tuple_word)
        if count == 30:
            break

    return reverse_index.sort()
    
dictionary_reverse()