import tkinter as tk
from tkinter import ttk
from Application.application import *
from Application.dataObjects import *

class SongSearchVC(tk.Frame):
    def __init__(self, app, parent=None):
        self.app = app
        self.parent = parent

        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.search = tk.StringVar()
        self.searchView = None

        self.create_view()

    def create_view(self):
        self.searchView = ttk.Treeview(self, columns=('id', 'Title', 'Duration', 'Type'))
        self.searchView.heading('id', text='id')
        self.searchView.heading('Title', text='Title')
        self.searchView.heading('Duration', text='Duration')
        self.searchView.heading('Type', text='Type')
        self.searchView['show'] = 'headings'  # Remove empty first column
        self.searchView.grid(column=0, row=0, columnspan=3)

        search_entry = tk.Entry(self, width=15, textvariable=self.search)
        search_entry.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.E))
        
        search_button = tk.Button(self, text='Search', command=self.search_action)
        search_button.grid(column=2, row=1)

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def search_action(self):
        #terms = [t.strip() for t in self.search.get().split(',')]  # Old search pattern, splitting on commas
        terms = self.search.get().split()

        print(terms)

        #data = [(1,Song(4, "Luckenbach Texas", 69)), (2, Song(88, "Allah's Plan", 420)), (3, Playlist(4, "My Cool Playlist", 69420))]  # Test data

        data = self.app.searchSongAndPlaylists(terms)
        for i in range(len(data)):
            d = data[i]
            md = d[1]  # MusicData
            self.searchView.insert("",'end',iid=i, values=(md.ID, md.title, md.duration, md.__class__.__name__))
        print(data)

    def logout_action(self):
        self.grid_forget()
