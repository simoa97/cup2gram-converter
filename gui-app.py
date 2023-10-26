from database import food_list
from tkinter import *

sorted_food_list = dict(sorted(food_list.items())) # sorting for the list

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
convert_value = Button(root, text='Convert', command= lambda: converter(1))
output_text = Text(root, width=20, height=3, wrap=WORD)


# ingredient selector for the list box
for a in sorted_food_list:
    ingredient_choser.insert(END, a)


def converter(cups):
    """Conversion of cups to grams"""
    output_text.delete(1.0,END) # clear the text box
    ingredient = ingredient_choser.get(ingredient_choser.curselection()) # get selected item from list box 
    cups = input_value.get(1.0, "end-1c") # get inputed value of cups
    gram_value = float(cups) * float(sorted_food_list[ingredient])
    output_text.insert(END ,str(cups) + ' cups of ' + ingredient + ' is ' +
                        str(gram_value)+'g')


# arrangement of the GUI
text.pack()
text2.pack()
ingredient_choser.pack()
text3.pack()
input_value.pack()
convert_value.pack(anchor='center')
output_text.pack()

root.mainloop()
