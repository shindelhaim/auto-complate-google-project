from data.init_data import data_for_search, get_sentences_data
from input_correction import get_completions_with_correction


def get_list_completions(input):
    indexes = data_for_search.get(input, None)
    suitable_completions = []

    if indexes:
        match_indexes = indexes[:5] if len(indexes) > 5 else indexes
        list_sentences_data = get_sentences_data()

        for i in match_indexes:
            suitable_completions += list_sentences_data[i]
            suitable_completions[i]["score"] = len(list_sentences_data[i]["sentence"]) * 2

    if len(suitable_completions) < 5:
        suitable_completions += get_completions_with_correction(input, 5 - len(suitable_completions))

    for item in suitable_completions:
        item["offset"] = item["sentence"].index(input)

    return suitable_completions


# if __name__ == "__main__":
#     print(f'{get_list_completions("* enum")} \n')
#     print(f'{get_list_completions("Hel")} \n')
