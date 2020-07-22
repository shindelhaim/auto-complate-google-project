from completion import get_best_k_completions

def start_application():
    print("The system is ready:")

    while(True):
        user_input = input("Enter your text: \n")
        new_input = ""

        while(new_input != '#' and user_input != '#'):
            user_input += new_input
            print(f'Here are suggestions: \n')
            get_best_k_completions(user_input)
            
            print(user_input, end='')
            new_input =  input()