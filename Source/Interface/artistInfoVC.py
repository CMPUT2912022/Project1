import tkinter as tk
from tkinter import ttk
from Application.application import *
from Application.dataObjects import *
from math import *
from Interface.songVC import *

class artistInfoVC(tk.Frame):
    def __init__(self, app, parent=None, root=None, artistName=0):
        self.app = app
        self.parent = parent
        self.artistName = artistName
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
        self.searchView = ttk.Treeview(self, columns=('id', 'Title', 'Duration'))
        self.searchView.heading('id', text='ID')
        self.searchView.heading('Title', text='Title')
        self.searchView.heading('Duration', text='Duration')
        self.searchView['show'] = 'headings'  # Remove empty first column
        self.searchView.grid(column=0, row=0, columnspan=5)

        self.fill_table()
        
        self.searchView.bind("<<TreeviewSelect>>", self.openSelectedItem)
        
        back_button = tk.Button(self, text='Back', command=self.back_action)
        back_button.grid(column=0, row=1, sticky=(tk.W, tk.E))
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def openSelectedItem(self, a):
        selectedItem = self.searchView.selection()[0]
        itemID = self.searchView.item(selectedItem)['values'][0]
        svc = songVC(self.app, self.parent, self.root, itemID)
        self.destroy()



    def clear_all(self):
       for item in self.searchView.get_children():
          self.searchView.delete(item)

    def back_action(self):
        self.destroy()
   
    def fill_table(self):
        self.clear_all()
        #data = [(1,Song(1, "Luckenbach Texas", 69))]
        #CODE FOR FILLING THE TABLE WITH EVERY SONG THAT THE ARTIST HAS
        #WITH THE THE ARTIST NAME OF SELF.ARTISTNAME
        #format should be as below

        artistDetails= self.app.getArtistDetails(self.artistName)
        
        data = artistDetails.songs
        self.max_index = trunc(len(data)/self.limit)
        if len(data)%self.limit == 0:
            self.max_index -=1;
        current_page = self.current_index*self.limit
        for i in range(current_page, current_page + self.limit):
            if i >= len(data):
                break
            s = data[i]
            self.searchView.insert("",'end',iid=i, values=(s.ID, s.title, s.duration))

