from database import food_list
from tkinter import *
from tkinter import ttk
# import sys

# creating the root window and config
root = Tk() # main window
root.title('Cups2grams')
root.minsize(310,410)
root.maxsize(600,820)
root.geometry("310x410+700+150")


# GUI elements
text = Label(root, text="Cups to grams converter",font=(30), 
             anchor='n',padx=5, pady=5)
text2 = Label(root, text='1. Select the ingredient')
ingredient_choser = Listbox(root, selectmode=SINGLE, width=24)
text3 = Label(root, text='2. Input number of Cups',pady=3)
input_value = Text(root, width=5, height=1, pady=3)
convert_value = Button(root, text='Convert', command= lambda: converter(1)
                       ) 
output_text = Text(root, width=24, height=3)


# ingredient selector for the list box
for a in food_list:
    ingredient_choser.insert(END, a)


def converter(cups):
    """Conversion of cups to grams"""
    ingredient = ingredient_choser.get(ingredient_choser.curselection()) # get selected item from list box 
    cups = input_value.get(1.0, "end-1c") # get inputed value of cups
    gram_value = float(cups) * float(food_list[ingredient])
    print(gram_value)


# arrangement of the GUI
text.pack()
text2.pack()
ingredient_choser.pack()
text3.pack()
input_value.pack()
convert_value.pack(anchor='center')
output_text.pack()

root.mainloop()


# need to create input for cups value
# need to print out the conversion