from completion import get_list_completions

def start_application():
    print("The system is ready:")

    while(True):
        user_input = input("Enter your text: \n")
        new_input = ""

        while(new_input != '#' and user_input != '#'):
            user_input += new_input
            print(f'Here are 5 suggestions: \n{get_list_completions(user_input)} \n')
            print(user_input, end='')
            new_input =  input()