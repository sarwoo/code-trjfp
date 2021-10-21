import tkinter
from tkinter import ttk

from ttkbootstrap import Style


class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title('Simple data entry form')
        self.style = Style('sandstone')
        self.form = EntryForm(self)
        self.form.pack(fill='both', expand='yes')
    


class EntryForm(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(padding=(20, 10))
        self.columnconfigure(2, weight=1)

        # form variables
        self.date = tkinter.StringVar(value='', name='date')
        self.weight = tkinter.StringVar(value='', name='weight')
        self.temperature = tkinter.StringVar(value='', name='temperature')
        self.product = tkinter.StringVar(value='', name='product')
        self.source_type = tkinter.StringVar(value='', name='source_type')
        self.source = tkinter.StringVar(value='', name='source')

        # form headers
        ttk.Label(self, text='Please enter intercept data', width=40).grid(columnspan=3, pady=10)
        
        temperatures = ['Ambient', 'Chilled', 'Frozen']
        products = ['Bakery', 'Dairy', 'Drinks', 'Fresh Produce', 'Meat Fish Poultry Eggs', 'Other', 'Pre Prepared Meals']
        source_types = ['Donation', 'Paid']
        # create label/entry rows
        ttk.Label(self, text='date'.title()).grid(row=1, column=0, sticky='ew', pady=10, padx=(0, 10))
        ttk.Entry(self, textvariable='date').grid(row=1, column=1, columnspan=2, sticky='ew')
        ttk.Label(self, text='weight kg'.title()).grid(row=2, column=0, sticky='ew', pady=10, padx=(0, 10))
        ttk.Entry(self, textvariable='weight').grid(row=2, column=1, columnspan=2, sticky='ew')
        ttk.Label(self, text='temperature'.title()).grid(row=3, column=0, sticky='ew', pady=10, padx=(0, 10))
        cbTemp = ttk.Combobox(self, textvariable='temperature', values=temperatures, state="readonly")
        cbTemp.grid(row=3, column=1, columnspan=2, sticky='ew')
        cbTemp.current(0)
        ttk.Label(self, text='product'.title()).grid(row=4, column=0, sticky='ew', pady=10, padx=(0, 10))
        cbProd = ttk.Combobox(self, textvariable='product', values=products, state="readonly")
        cbProd.grid(row=4, column=1, columnspan=2, sticky='ew')
        cbProd.current(0)
        ttk.Label(self, text='source'.title()).grid(row=5, column=0, sticky='ew', pady=10, padx=(0, 10))
        ttk.Entry(self, textvariable='source').grid(row=5, column=1, columnspan=2, sticky='ew')
        ttk.Label(self, text='source type'.title()).grid(row=6, column=0, sticky='ew', pady=10, padx=(0, 10))
        cbType = ttk.Combobox(self, textvariable='source_type', values=source_types, state="readonly")
        cbType.grid(row=6, column=1, columnspan=2, sticky='ew')
        cbType.current(0)
        
        
        # submit button
        self.submit = ttk.Button(self, text='Submit', style='primary.TButton', command=self.print_form_data)
        self.submit.grid(row=8, column=1, sticky='ew', pady=10, padx=(0, 10))

        # cancel button
        self.cancel = ttk.Button(self, text='Cancel', style='primary.TButton', command=self.quit)
        self.cancel.grid(row=8, column=2, sticky='w')

    def print_form_data(self):
        print(self.date.get(), self.weight.get(), self.temperature.get(), self.product.get(), self.source_type.get(), self.source.get())

if __name__ == '__main__':
    Application().mainloop()