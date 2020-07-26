from data.init_data import data_for_search, get_sentences_data
from input_correction import get_completions_with_correction
from auto_complete_data import AutoCompleteData


def get_list_completions(input):
    location_sub = data_for_search.get(input, None)
    suitable_completions = []

    if location_sub:
        match_indexes = location_sub[:5] if len(location_sub) > 5 else location_sub
        list_sentences_data = get_sentences_data()

        for i in match_indexes:
            sentence_dict = list_sentences_data[i]
            sentence_dict["score"] = len(input) * 2
            suitable_completions += [sentence_dict]
            

    if len(suitable_completions) < 5:
        suitable_completions += get_completions_with_correction(input, 5 - len(suitable_completions))

        # remove duplicate sentences in suitable_completions
        new_suitable_list = []

        for item in suitable_completions:
            if {"sentence": item["sentence"], "src": item["src"], "line": item["line"]} not in list(map(lambda d: {"sentence": d["sentence"], "src": d["src"], "line": d["line"]}, new_suitable_list)):
                new_suitable_list += [item]
        
        return new_suitable_list

    return suitable_completions


def get_best_k_completions(input):
    suitable_completions_list = get_list_completions(input)
    autoCompleteData_list = []

    for item in suitable_completions_list:
        autoCompleteData_list += [AutoCompleteData(item)]

    return autoCompleteData_list
   

# if __name__ == "__main__":
#     print(f'{get_list_completions("* enum")} \n')
#     print(f'{get_list_completions("Hel")} \n')