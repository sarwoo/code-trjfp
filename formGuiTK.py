from tkinter import *
from tkinter import ttk
from datetime import date
import tkinter



def add_click():
    print(f'{date_entry.get()}')
    print(f'{weight_entry.get()}')
    print(f'{product_category_entry.get()}')
    print(f'{product_temperature_entry.get()}')
    print(f'{product_type_entry.get()}')
    print(f'{source_company_entry.get()}')

def cancel_click():
    window.destroy()

def temperature_options():
    return [
        'Ambient',
        'Chilled',
        'Frozen'
    ]

window = Tk()
window.title("Interception")
window.config(padx=50, pady=50)

#Labels
date_label = Label(text="Date:")
date_label.grid(row=0, column=0, sticky=E)

weight_label = Label(text="Weight Kg:")
weight_label.grid(row=1, column=0, sticky=E)

product_category_label = Label(text="Product category:")
product_category_label.grid(row=2, column=0, sticky=E)

product_temperature_label = Label(text="Product temperature:")
product_temperature_label.grid(row=3, column=0, sticky=E)

product_type_label = Label(text="Product type:")
product_type_label.grid(row=4, column=0, sticky=E)

source_company_label = Label(text="Source company:")
source_company_label.grid(row=5, column=0, sticky=E)


#Entries
date_entry = Entry(width=20)
date_entry.grid(row=0, column=1)
date_entry.insert(0, date.today())

weight_entry = Entry(width=20)
weight_entry.grid(row=1, column=1)
weight_entry.focus()

product_category_entry = Entry(width=20)
product_category_entry.grid(row=2, column=1)

style = ttk.Style()
style.configure("BW.TCombobox", foreground="black", background="white", highlightbackground='white')
temperature = tkinter.StringVar()
product_temperature_entry = ttk.Combobox(width=20, style="BW.TCombobox", textvariable=temperature)
product_temperature_entry['values'] = temperature_options()
product_temperature_entry.current(0)
product_temperature_entry.grid(row=3, column=1)

product_type_entry = Entry(width=20)
product_type_entry.grid(row=4, column=1)

source_company_entry = Entry(width=20)
source_company_entry.grid(row=5, column=1)

# Buttons
add_intercept_button = Button(text="Add intercept", width=20)
add_intercept_button.grid(row=6, column=1)
add_intercept_button.config(command=add_click)

cancel_intercept_button = Button(text="Back", width=14, command=cancel_click)
cancel_intercept_button.grid(row=6, column=0, sticky=E)

window.mainloop()
