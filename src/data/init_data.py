sorce_files = {1: "init_data.py"}

sentences_data = [{"sentence": "Hello", "src": 1}, {"sentence": "Hi", "src": 1}, {"sentence": "Hic", "src": 1},{"sentence": "ic", "src": 1}]

data = {}


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
    init_data()
    print(f'{sentences_data} \n')
    print(f'{data} \n')

