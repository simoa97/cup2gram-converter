from database import food_list
from tkinter import *
from tkinter import ttk
import sys

root = Tk() # main window
root.title('Cups2grams')
root.minsize(310,410)
root.maxsize(600,820)
root.geometry("310x410+700+150")


# GUI elements
text = Label(root, text="Cups to grams converter",font=(30), 
             anchor='n',padx=5, pady=5)
text2 = Label(root, text='Select the ingredient')
ingredient_choser = Listbox(root, selectmode=SINGLE, width=24)
convert_value = Button(root, text='Convert', command= lambda: converter(1)
                       ) # prints out only first selection :-( 
output_text = Text(root, width=24, height=3)


# ingredient selector for the list box
for a in food_list:
    ingredient_choser.insert(END, a)

#ingredient = food_list[x]


def converter(cups):
    """Conversion of cups to grams"""
    ingredient = ingredient_choser.get(ingredient_choser.curselection())
    gram_value = float(cups) * float(food_list[ingredient])
    print(gram_value)


# arrangement of the GUI
text.pack()
text2.pack()
ingredient_choser.pack()
convert_value.pack(anchor='center')
output_text.pack()

root.mainloop()