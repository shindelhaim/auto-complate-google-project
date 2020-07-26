from completion import get_best_k_completions
from data.init_data import init_meta_data, get_source_files, ignore_punctuation_and_spaces
from tkinter import Tk, Menu, END, Entry, Button, Listbox, Scrollbar, Text, Frame


init_meta_data()


root = Tk() 
root.title('Auto Complete') 

menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')


def get(): 
    input = entry.get()
    input = ignore_punctuation_and_spaces(input)
    mylist.delete(0,END)

    autoCompleteData_list = get_best_k_completions(input)
    mylist.insert(END, '\n\n')
    mylist.insert(END, f'    Here are {len(autoCompleteData_list)} suggestions:')
    mylist.insert(END, '\n\n')
    
    for i in range(len(autoCompleteData_list)):
        mylist.insert(END, f'    {i + 1}. {autoCompleteData_list[i].completed_sentence},') 
        mylist.insert(END, f'        (src: {get_source_files()[autoCompleteData_list[i].source_text]}, offset: {autoCompleteData_list[i].offset}, score: {autoCompleteData_list[i].score})')
        mylist.insert(END, '\n\n')


entry = Entry(width=87, bd=4, font="David")
button_search = Button(root, text='Search', width=8, bd=2, command=get)
entry.grid(row=0, column=0) 
button_search.grid(row=0, column=1)
mylist = Listbox(root, width=87, height=20, bd=3,  font="David") 
mylist.grid(row=1, column=0)
root.mainloop()
