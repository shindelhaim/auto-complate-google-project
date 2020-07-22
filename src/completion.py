from data.init_data import data_for_search, get_sentences_data





def get_list_completions(input):
    place = data_for_search.get(input, None)

    if place is None:
        return []

    index_begin = place["begin"]
    index_end = place["end"]

    index_end = index_begin + 5 if index_end - index_begin > 5 else index_end

    suitable_completions = get_sentences_data()[index_begin:index_end]

    for item in suitable_completions:
        item["score"] = len(item["sentence"]) * 2

    return suitable_completions


# if __name__ == "__main__":
#     print(f'{get_list_completions("H")} \n')
#     print(f'{get_list_completions("Hel")} \n')

