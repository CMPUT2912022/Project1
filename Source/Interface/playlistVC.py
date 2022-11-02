import tkinter as tk
from tkinter import ttk
from Application.application import *
from Application.dataObjects import *
from math import *

class playlistVC(tk.Frame):
    def __init__(self, app, parent=None, itemID=0):
        self.app = app
        self.parent = parent
        self.itemID = itemID

        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        self.search = tk.StringVar()
        self.searchView = None

        self.create_view()

    def create_view(self):
        self.searchView = ttk.Treeview(self, columns=('id', 'Title', 'Duration'))
        self.searchView.heading('id', text='ID')
        self.searchView.heading('Title', text='Title')
        self.searchView.heading('Duration', text='Duration')
        self.searchView['show'] = 'headings'  # Remove empty first column
        self.searchView.grid(column=0, row=0, columnspan=5)

        self.fill_table()
        
        self.searchView.bind("<<TreeviewSelect>>", self.openSelectedItem)

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def openSelectedItem(self, a):
        selectedItem = self.searchView.selection()[0]
        itemID = self.searchView.item(selectedItem)['values'][0]
        svc = songVC(self.app, self.parent, itemID)
        self.destroy()



    def clear_all(self):
       for item in self.searchView.get_children():
          self.searchView.delete(item)

          
    def fill_table(self):
        self.clear_all()
        #CODE FOR FILLING THE TABLE WITH EVERY SONG IN THE PLAYLIST
        #WITH THE PLAYLIST ID OF SELF.ITEMID
        #format should be as below

        
        #data = self.app.searchSongAndPlaylists()
        #for i in range(current_page, current_page + self.limit):
            #if i >= len(data):
            #    break
            #d = data[i]
            #md = d[1]  # MusicData
            #self.searchView.insert("",'end',iid=i, values=(md.ID, md.title, md.duration))
