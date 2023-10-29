from database import food_list
from tkinter import *

# sorting the dictionary by keys
sorted_food_list = dict(sorted(food_list.items()))

# creating the root window and config
root = Tk() # main window
root.title('Cups2grams')
root.minsize(310,410)
root.maxsize(600,820)
root.geometry("310x410+700+150")


# GUI elements
frame = Frame()
text = Label(root, text="Cups to grams converter",font=(30), 
             anchor='n',padx=5, pady=5)
text2 = Label(root, text='1. Select the ingredient')
ingredient_choser = Listbox(frame, selectmode=SINGLE, width=24)
scrollbar = Scrollbar(frame)
text3 = Label(root, text='2. Input number of Cups',pady=3)
input_value = Text(root, width=5, height=1, pady=3)
convert_value = Button(root, text='Convert', command= lambda: input_check())
output_text = Text(root, width=20, height=3, wrap=WORD)


# ingredient selector for the list box
for a in sorted_food_list:
    ingredient_choser.insert(END, a)


def input_check():
    """check user"""
    output_text.delete(1.0,END) # clear the text box
    selection = ingredient_choser.curselection() # select from list box
    user_input = input_value.get(1.0, "end-1c")
    if not selection and not user_input:
        output_text.insert(END, 'You need to select ingredient and input cup value.')
    elif not selection:
        output_text.insert(END, 'You need to select ingredient.')
    elif not user_input:
        output_text.insert(END, 'You need to input cup value.')
    elif not user_input.replace(".", "", 1).isdigit():
        output_text.insert(END, 'You can only enter numbers. Please enter number.')
    else:
        converter(ingredient_choser.get(selection), user_input)


def converter(ingredient, cups):
    """Conversion of cups to grams"""
    output_text.delete(1.0,END) # clear the text box
    gram_value = float(cups) * float(sorted_food_list[ingredient])    
    output_text.insert(END ,str(cups) + ' cups of ' + ingredient + ' is ' +
                            str(gram_value)+'g')


# scrollbar for the list box
scrollbar.config(command = ingredient_choser.yview) 
ingredient_choser.config(yscrollcommand = scrollbar.set)


# arrangement of the GUI
text.pack()
text2.pack()
frame.pack()
ingredient_choser.pack(side="left", fill="y")
scrollbar.pack(side="right", fill="y")
text3.pack()
input_value.pack()
convert_value.pack(anchor='center')
output_text.pack()


# run tkinter
root.mainloop()