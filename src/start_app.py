from completion import get_best_k_completions
from data.init_data import ignore_punctuation_and_spaces, get_source_files
from auto_complete_data import AutoCompleteData



def start_application():
    print("The system is ready:")

    while(True):
        user_input = input("Enter your text: \n")
        new_input = ""

        while(new_input != '#' and user_input != '#'):
            user_input += new_input
            autoCompleteData_list = get_best_k_completions(ignore_punctuation_and_spaces(user_input))
            print(f'Here are {len(autoCompleteData_list)} suggestions: \n')

            for i in range(len(autoCompleteData_list)):
                print(f'{i + 1}. {autoCompleteData_list[i].completed_sentence},') 
                print(f'(src: {get_source_files()[autoCompleteData_list[i].source_text]}, offset: {autoCompleteData_list[i].offset}, score: {autoCompleteData_list[i].score}) \n')

            print(user_input, end='')
            new_input =  input()