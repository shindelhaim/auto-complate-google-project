import string


source_files = {1: "data/contents.txt"}

sentences_data = []

data_for_search = {}



def get_source_files():
    return source_files


def get_sentences_data():
    return sentences_data


def remove_space_of_begin(sentence):
    while(sentence and sentence[0] == ' '): 
        sentence = sentence[1:]
    
    return sentence


def get_dict_of_sentences(sentence, id_src, num_line):
    sentence = remove_space_of_begin(sentence)
    return {"sentence": sentence, "src": id_src, "line": num_line}


def read_from_files():  
    for id, name in source_files.items():
        global sentences_data

        with open(name) as file:
            sentences = file.read().split("\n")

        for num_line, sentence in enumerate(sentences):
            dict_sentence = get_dict_of_sentences(sentence, id, num_line)

            if dict_sentence["sentence"] != "":
                sentences_data += [dict_sentence]


def get_sub_sentences(sentence):
    return [sentence[i:j] for i in range(0, len(sentence) + 1) for j in range(i + 1, len(sentence) + 1)]


def init_data_for_search():
    for index, item in enumerate(sentences_data):
        sub_sentences = get_sub_sentences(item["sentence"])
    
        for sub in sub_sentences:
            if sub in data_for_search:
                data_for_search[sub].add(index)
            else:
                data_for_search[sub] = {index}
    
    #sort indexes for every sub
    for sub in data_for_search.keys():
        data_for_search[sub] = list(data_for_search[sub])
        data_for_search[sub] = sorted(data_for_search[sub], 
            key=lambda k: sentences_data[k]["sentence"][(sentences_data[k]["sentence"]).index(sub):])


def init_meta_data():
    read_from_files()
    init_data_for_search()


if __name__ == "__main__":
    init_meta_data()
    # print(f'{sentences_data} \n')
    print(f'{data_for_search["C server"]} \n')

    for i in data_for_search["C server"]:
        print(f'{sentences_data[i]} \n')