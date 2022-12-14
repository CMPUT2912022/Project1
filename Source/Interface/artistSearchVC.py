import tkinter as tk
from tkinter import ttk
from Application.application import *
from Application.dataObjects import *
from math import *
from Interface.playlistVC import *
from Interface.artistInfoVC import *
from Interface.songVC import *

class ArtistSearchVC(tk.Frame):
    def __init__(self, app, parent=None, root = None):
        self.app = app
        self.parent = parent
        self.root = root
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.current_index = 0
        self.max_index = 0
        self.limit = 5

        self.search = tk.StringVar()
        self.searchView = None

        self.create_view()

    def create_view(self):
        self.searchView = ttk.Treeview(self, columns=('aid', 'Name', 'Nationality', 'Number of Songs'))
        self.searchView.heading('aid', text='aid')
        self.searchView.heading('Name', text='Name')
        self.searchView.heading('Nationality', text='Nationality')
        self.searchView.heading('Number of Songs', text='Number of Songs')
        self.searchView['show'] = 'headings'  # Remove empty first column

        self.searchView.grid(column=0, row=0, columnspan=5)

        self.searchView.bind("<<TreeviewSelect>>", self.openSelectedItem)

        search_entry = tk.Entry(self, width=5, textvariable=self.search)
        search_entry.grid(column=0, row=1, sticky=(tk.W, tk.E))
        search_entry.focus()

        search_button = tk.Button(self, text='Search', command=self.search_action)
        search_button.grid(column=1, row=1)

        up_button = tk.Button(self, text='Next', command=self.next_action)
        up_button.grid(column=3, row=1)
        
        down_button = tk.Button(self, text='Previous', command=self.previous_action)
        down_button.grid(column=2, row=1)
        
        back_button = tk.Button(self, text='Back', command=self.back_action)
        back_button.grid(column=4, row=1)

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)


    #PREVIOUS AND NEXT JUST HANDLE MOVING THE PAGE BACK AND FORTH
    #THIS IS DONE USING THE SELF.CURRENT_INDEX AND MAKING SURE ONLY
    #5 ITEMS ARE DISPLAYED AT A TIME, BY MOVING THE INDEX WE
    #CHANGE WHICH 5 WE SEE
    def previous_action(self):
        if self.current_index != 0:
            self.current_index -=1
            self.clear_all()
            self.search_action()

    def next_action(self):
        if self.current_index != self.max_index:
            self.current_index +=1
            self.clear_all()
            self.search_action()
    
    def back_action(self):
        self.destroy()

    #WHEN A PLAYLIST OR SONG IS SELECTED WE NEED TO OPEN A NEW WINDOW
    #DEPENDING ON THE TYPE. A PLAYLIST WINDOW DISPLAYS ALL OF ITS SONGS
    #AND IF SOMETHING IS PRESSED IN IT IT DISPLAYS A SONG WINDOW
    #IF A SONG IS PRESSED THEN A SONG WINDOWS DISPLAYS THE 3 OPTIONS
    #LISTEN IN REQUIRMENTS
    def openSelectedItem(self, a):
        selectedItem = self.searchView.selection()[0]
        artistName = self.searchView.item(selectedItem)['values'][0]
        aivc = artistInfoVC(self.app, self.parent,self.root, artistName)



        
    def clear_all(self):
       for item in self.searchView.get_children():
          self.searchView.delete(item)
    def search_action(self):
        self.clear_all()
        #terms = [t.strip() for t in self.search.get().split(',')]  # Old search pattern, splitting on commas
        terms = self.search.get().split()

        print(terms)
        data = self.app.searchArtists(terms)

        self.max_index = trunc(len(data)/self.limit)
        if len(data)%self.limit == 0:
            self.max_index -=1;
        current_page = self.current_index*self.limit
        for i in range(current_page, current_page + self.limit):
            if i >= len(data):
                break
            a = data[i][1]  # Artist
            t_songs = data[i][2]

            self.searchView.insert("",'end',iid=i, values=(a.mid, a.name, a.nationality, t_songs))
        print(data)


