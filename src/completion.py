from data.init_data import data_for_search, get_sentences_data, get_source_files
from input_correction import get_completions_with_correction
from auto_complete_data import AutoCompleteData


def get_list_completions(input):
    indexes = data_for_search.get(input, None)
    suitable_completions = []

    if indexes:
        match_indexes = indexes[:5] if len(indexes) > 5 else indexes
        list_sentences_data = get_sentences_data()

        for i in match_indexes:
            sentence_dict = list_sentences_data[i]
            sentence_dict["score"] = len(list_sentences_data[i]["sentence"]) * 2
            sentence_dict["offset"] = (sentence_dict["sentence"]).index(input)
            suitable_completions += [sentence_dict]
            

    if len(suitable_completions) < 5:
        suitable_completions += get_completions_with_correction(input, 5 - len(suitable_completions))


    return suitable_completions


def get_best_k_completions(input):
    suitable_completions_list = get_list_completions(input)
    autoCompleteData_list = []

    for item in suitable_completions_list:
        autoCompleteData_list += [AutoCompleteData(item)]
    
    for i in range(len(autoCompleteData_list)):
        print(f'{i + 1}. {autoCompleteData_list[i].completed_sentence}, ({get_source_files()[autoCompleteData_list[i].source_text]}) \n')


# if __name__ == "__main__":
#     print(f'{get_list_completions("* enum")} \n')
#     print(f'{get_list_completions("Hel")} \n')
