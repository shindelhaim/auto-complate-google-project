import string
from data.init_data import data_for_search, get_sentences_data


def character_replacement(substr, num_sentences):
    num_suitables = 0
    suitable_completions = []
    

    for i in range(0,len(substr))[::-1]:

        for char in string.printable:
            
            corrction_str = substr[:i] + char + substr[i + 1:]
            match_indexes = data_for_search.get(corrction_str, None)
            
            if match_indexes:
                
                match_indexes = match_indexes[:num_sentences] if len(match_indexes) > num_sentences else match_indexes
                list_sentences_data = get_sentences_data()

                for j in match_indexes:
                    sentence_dict = list_sentences_data[j]
                    sentence_dict["score"] = len(list_sentences_data[j]["sentence"]) * 2

                    if(i < 4):
                        sentence_dict["score"] -=  5 - i
                    else:
                        sentence_dict["score"] -= 1

                    
                    sentence_dict["offset"] = (sentence_dict["sentence"]).index(corrction_str)
                    suitable_completions += [sentence_dict]

                num_suitables = len(suitable_completions)
                num_sentences -= num_suitables
            
            if num_sentences == 0:
                return suitable_completions
    
    return suitable_completions


def deleting_character(substr, num_sentences):
    return []

def adding_character(substr, num_sentences):
    return []

def get_completions_with_correction(substr, num_sentences):
    correction_list = []
    correction_list += character_replacement(substr, num_sentences)
    correction_list += deleting_character(substr, num_sentences)
    correction_list += adding_character(substr, num_sentences)

    correction_list = sorted(correction_list, key=lambda k: k["score"], reverse=True)
    len_correction_list = len(correction_list)
    index_end = 5 if len_correction_list > 5 else len_correction_list
    
    return correction_list[:index_end]
