from data.init_data import data_for_search, get_sentences_data


def get_list_completions(input):
    place = data_for_search.get(input, None)

    if place is None:
        return []

    index_begin = place["begin"]
    index_end = place["end"]

    index_end = index_begin + 5 if index_end - index_begin > 5 else index_end

    return get_sentences_data()[index_begin:index_end]


# if __name__ == "__main__":
#     print(f'{get_list_completions("H")} \n')
#     print(f'{get_list_completions("Hel")} \n')

