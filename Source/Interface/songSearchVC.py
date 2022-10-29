import tkinter as tk
from tkinter import ttk

class SongSearchVC(tk.Frame):
    def __init__(self, app, parent=None):
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        searchView = ttk.Treeview(self, columns=('id', 'Title', 'Duration'))
        searchView.grid(column=0, row=0, columnspan=3)

        search = tk.StringVar()  # member id
        search_entry = tk.Entry(self, width=15, textvariable=search)
        search_entry.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.E))
        
        search_button = tk.Button(self, text='Search', command=self.search_action)
        search_button.grid(column=2, row=1)

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def search_action(self):
        pass

    def logout_action(self):
        self.grid_forget()
