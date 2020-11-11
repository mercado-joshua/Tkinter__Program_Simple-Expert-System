#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd,simpledialog as sd

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""

    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.init_config()
        self.init_vars()
        self.init_widgets()

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def init_vars(self):
        self.world = {}

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.withdraw()
        self.resizable(False, False)
        self.title('Ask the Expert - Capital Cities of the World')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        self._read_from_file()

        while True:
            query_country = sd.askstring('Country', 'Type the name of a country:')
            query_country = query_country.capitalize()

            if query_country in self.world:
                result = self.world[query_country]
                mb.showinfo('Answer', f'The capital city of {query_country} is {result}!')

            else:
                new_city = sd.askstring('Teach me',
                    f'I don\'t know! What is the capital city of {query_country}?')

                self.world[query_country] = new_city
                self._write_to_file(query_country, new_city)

    # INSTANCE ---------------------------------
    def _read_from_file(self):
        with open(self.filename) as file:
            for line in file:
                line = line.rstrip('\n')
                country, city = line.split('/')
                self.world[country] = city

    def _write_to_file(self, country_name, city_name):
        with open(self.filename, 'a') as file:
            file.write(f'\n{country_name}/{city_name}')


#===========================
# Start GUI
#===========================

def main():
    app = App('capital_data.txt')
    app.mainloop()

if __name__ == '__main__':
    main()