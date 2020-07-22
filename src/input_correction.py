import string
from data.init_data import data_for_search, get_sentences_data


def character_replacement(substr, num_sentences):
    num_suitables = 0
    suitable_completions = []
    for i in range(0,len(substr),-1):
        for char in string.printable:

            corrction_str = substr[:i] + char + substr[i + 1:]
            place = data_for_search.get(corrction_str, None)
            
            if place:
                index_begin = place["begin"]
                index_end = place["end"]
                
                index_end = index_begin + num_sentences if num_suitables > num_sentences else index_end                
                num_suitables += index_end - index_begin

                nonlocal suitable_completions
                suitable_completions = get_sentences_data()[index_begin:index_end]
            if num_suitables > num_sentences:
                break

        if num_suitables > num_sentences:
                break

   

