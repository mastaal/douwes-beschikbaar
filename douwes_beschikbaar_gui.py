#!/usr/bin/python3

"""
douwes_beschikbaar_gui.py:
    A TKinter GUI for douwes-beschikbaar.py

    Copyright 2017 Martijn Staal

    This file is part of douwes-beschikbaar.

    douwes-beschikbaar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    douwes-beschikbaar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with douwes-beschikbaar.  If not, see <http://www.gnu.org/licenses/>.
"""

import douwes_beschikbaar as douwes
from tkinter import *
book_file = "uitverkochte_titels.csv"

class DouwesGUI:

    def __init__(self, master):
        """A tkinter GUI for douwes_beschikbaar.py"""
        douwes.init_dict(book_file)
        frame = Frame(master)
        frame.pack()

        bottom_frame = Frame(master)
        bottom_frame.pack(side=BOTTOM)

        self.label_isbn = Label(frame, text="Vul een ISBN in:")
        self.label_isbn.pack(side=LEFT)

        self.entry_isbn = Entry(frame)
        self.entry_isbn.pack(side=LEFT)

        self.button_isbn_search = Button(frame, text="Zoeken", command=self.search_isbn)
        self.button_isbn_search.pack(side=LEFT)

        self.label_result_text = StringVar()
        self.label_result = Label(bottom_frame, textvariable=self.label_result_text)
        self.label_result.pack()

    def search_isbn(self):
        isbn = self.entry_isbn.get()
        available = douwes.check_available(isbn)
        if available:
            self.label_result_text.set("Deze titel is momenteel leverbaar.")
        else:
            self.label_result_text.set("Deze titel is momenteel niet leverbaar.")

root = Tk()
root.wm_title("douwes-beschikbaar")
root.geometry("400x50+0+0")
app = DouwesGUI(root)
root.mainloop()
