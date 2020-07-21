sorce_files = {1: "src/data/contents.txt"}

sentences_data = []

data = {}



def remove_space_of_begin(sentence):
    while(sentence and sentence[0] == ' '): 
        sentence = sentence[1:]
    
    return sentence


def get_dict_of_sentences(sentence, id_src):
    sentence = remove_space_of_begin(sentence)
    return [{"sentence": sentence, "src": id_src}]


def read_from_files():
    sentences_data_no_sorted = []
    
    for id, name in sorce_files.items():

        with open(name) as file:
            sentences = file.read().split("\n")

        for sentence in sentences:
            sentences_data_no_sorted += get_dict_of_sentences(sentence, id)

    global sentences_data
    sentences_data = sorted(sentences_data_no_sorted, key=lambda k: k["sentence"])


def get_sub_sentences(sentence):
    return [sentence[0:i] for i in range(1, len(sentence) + 1)]


def init_data():
    for index, item in enumerate(sentences_data):
        sub_sentences = get_sub_sentences(item["sentence"])
    
        for sub in sub_sentences:
            if sub in data:
                data[sub]["end"] += 1
            else:
                data[sub] = {"begin": index, "end": index + 1}


if __name__ == "__main__":
    read_from_files()
    init_data()
    print(f'{sentences_data} \n')
    print(f'{data} \n')

