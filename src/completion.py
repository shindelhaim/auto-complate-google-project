sentence1 = "Hello"
sentence2 = "Hi"

sorce = {1: "completion.py"}

sentences_sort = [{"sentence": "Hello", "src": 1}, {"sentence": "Hi", "src": 1}]

data = {
    "H": {
        "begin": 0,
        "end": 2
    },

    "He": {
        "begin": 0,
        "end": 1
    }, 

    "Hel": {
        "begin": 0,
        "end": 1
    }, 

    "Hell": {
        "begin": 0,
        "end": 1
    }, 

    "Hello": {
        "begin": 0,
        "end": 1
    }, 

    "Hi": {
        "begin": 1,
        "end": 2
    }
}


def get_list_completions(input):
    place = data.get(input, None)

    if place is None:
        return []

    index_begin = place["begin"]
    index_end = place["end"]

    index_end = index_begin + 5 if index_end - index_begin > 5 else index_end

    return sentences_sort[index_begin:index_end]


if __name__ == "__main__":
    print(f'{get_list_completions("H")} \n')
    print(f'{get_list_completions("Hel")} \n')

