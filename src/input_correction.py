import string
from data.init_data import data_for_search, get_sentences_data


def get_suitable_sentences_without_duplicates(i_letter, corrction_str, match_indexes, num_miss_sentences, suitable_completions, type_change):
    list_sentences_data = get_sentences_data()

    for j in match_indexes:
        if num_miss_sentences == 0:
            return suitable_completions
            
        sentence_dict = list_sentences_data[j]
        l = list(map(lambda d: {"sentence": d["sentence"], "src": d["src"], "line": d["line"]}, suitable_completions))

        if sentence_dict in l:
            continue

        if "replacement" == type_change:
            sentence_dict["score"] = len(corrction_str) * 2

            if(i_letter < 4):
                sentence_dict["score"] -=  5 - i_letter
            else:
                sentence_dict["score"] -= 1

        if "deleting" == type_change:
            sentence_dict["score"] = len(corrction_str) * 2 - 1

            if(i_letter < 4):
                sentence_dict["score"] -=  10 - 2 * i_letter
            else:
                sentence_dict["score"] -= 2

        if "adding" == type_change:
            sentence_dict["score"] = len(corrction_str) * 2 + 1

            if(i_letter < 4):
                sentence_dict["score"] -=  10 - 2 * i_letter
            else:
                sentence_dict["score"] -= 2

        suitable_completions += [sentence_dict]
        num_miss_sentences -= 1

    return suitable_completions
            

def character_replacement(substr, num_sentences):
    suitable_completions = []
    num_miss_sentences = num_sentences

    for i in range(0, len(substr))[::-1]:

        for char in 'abcdefghijklmnopqrstuvwxyz'.replace(substr[i],''):
            
            corrction_str = substr[:i] + char + substr[i + 1:] if i != len(substr) - 1 else substr[:i] + char
            match_indexes = data_for_search.get(corrction_str, None)
            
            if not match_indexes:
                continue

            suitable_completions = get_suitable_sentences_without_duplicates(i, corrction_str, match_indexes, num_miss_sentences, suitable_completions, "replacement")
            num_miss_sentences = num_sentences - len(suitable_completions)
            
            if num_miss_sentences == 0:
                return suitable_completions
    
    return suitable_completions


def deleting_character(substr, num_sentences):
    suitable_completions = []
    num_miss_sentences = num_sentences
    
    for i in range(0, len(substr) - 1)[::-1]:

        for char in 'abcdefghijklmnopqrstuvwxyz':
            
            corrction_str = substr[:i + 1] + char + substr[i + 1:]
            match_indexes = data_for_search.get(corrction_str, None)

            if not match_indexes:
                continue
            
            suitable_completions = get_suitable_sentences_without_duplicates(i, corrction_str, match_indexes, num_miss_sentences, suitable_completions, "deleting")
            num_miss_sentences = num_sentences - len(suitable_completions)
            
            if num_miss_sentences == 0:
                return suitable_completions
    
    return suitable_completions


def adding_character(substr, num_sentences):
    suitable_completions = []
    num_miss_sentences = num_sentences

    for i in range(0, len(substr))[::-1]:
        
        corrction_str = substr[:i] + substr[i + 1:] if i != len(substr) - 1 else substr[:i]
        match_indexes = data_for_search.get(corrction_str, None)
            
        if not match_indexes:   
            continue

        suitable_completions = get_suitable_sentences_without_duplicates(i, corrction_str, match_indexes, num_miss_sentences, suitable_completions, "adding")
        num_miss_sentences = num_sentences - len(suitable_completions)
            
        if num_miss_sentences == 0:
            return suitable_completions
    
    return suitable_completions


def get_completions_with_correction(substr, num_sentences):
    correction_list = []
    correction_list += character_replacement(substr, num_sentences)
    correction_list += deleting_character(substr, num_sentences)
    correction_list += adding_character(substr, num_sentences)

    correction_list = sorted(correction_list, key=lambda k: k["score"], reverse=True)

    # remove duplicate sentences in correction_list
    new_correction_list = []

    for item in correction_list:
        if {"sentence": item["sentence"], "src": item["src"], "line": item["line"]} not in list(map(lambda d: {"sentence": d["sentence"], "src": d["src"], "line": item["line"]}, new_correction_list)):
            new_correction_list += [item]
            
    len_correction_list = len(new_correction_list)
    index_end = num_sentences if len_correction_list > num_sentences else len_correction_list
    
    return new_correction_list[:index_end]
