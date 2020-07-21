sorce_files = {1: "data/contents.txt"}

sentences_data = []

data_for_search = {}


def get_sentences_data():
    return sentences_data


def remove_space_of_begin(sentence):
    while(sentence and sentence[0] == ' '): 
        sentence = sentence[1:]
    
    return sentence


def get_dict_of_sentences(sentence, id_src):
    sentence = remove_space_of_begin(sentence)
    return {"sentence": sentence, "src": id_src}


def read_from_files():
    sentences_data_no_sorted = []
    
    for id, name in sorce_files.items():

        with open(name) as file:
            sentences = file.read().split("\n")

        for sentence in sentences:
            dict_sentence = get_dict_of_sentences(sentence, id)

            if(dict_sentence["sentence"] != "" and dict_sentence not in sentences_data_no_sorted):
                sentences_data_no_sorted += [dict_sentence]


    global sentences_data
    sentences_data = sorted(sentences_data_no_sorted, key=lambda k: k["sentence"])


def get_sub_sentences(sentence):
    return [sentence[0:i] for i in range(1, len(sentence) + 1)]


def init_data_for_search():
    for index, item in enumerate(sentences_data):
        sub_sentences = get_sub_sentences(item["sentence"])
    
        for sub in sub_sentences:
            if sub in data_for_search:
                data_for_search[sub]["end"] += 1
            else:
                data_for_search[sub] = {"begin": index, "end": index + 1}

def init_meta_data():
    read_from_files()
    init_data_for_search()


# if __name__ == "__main__":
#     read_from_files()
#     init_data_for_search()
#     print(f'{sentences_data} \n')
#     print(f'{data_for_search} \n')

