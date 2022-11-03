import tkinter as tk
from tkinter import ttk
from Application.application import *
from Application.dataObjects import *
from math import *

class artistStatsVC(tk.Frame):
    def __init__(self, app, parent=None, root=None):
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
        #top 3 users
        
        desc1_label = tk.Label(self, text= "TOP 3 USERS", font=(24))
        desc1_label.grid(column=0, row=0, columnspan=2)
        
        self.searchView = ttk.Treeview(self, columns=('ID', 'Name'))
        self.searchView.heading('ID', text='ID')
        self.searchView.heading('Name', text='Name')
        self.searchView['show'] = 'headings'  # Remove empty first column
        self.searchView.grid(column=0, row=1, columnspan=2)

       
        #TOP 3 PLAYLISTS

        desc2_label = tk.Label(self, text= "TOP 3 PLAYLISTS", font=(24))
        desc2_label.grid(column=2, row=0, columnspan=2)
        
        self.searchView1 = ttk.Treeview(self, columns=('ID', 'Title'))
        self.searchView1.heading('ID', text='ID')
        self.searchView1.heading('Title', text='Title')
        self.searchView1['show'] = 'headings'  # Remove empty first column
        self.searchView1.grid(column=2, row=1, columnspan=2)
        
        self.fill_table()

        back_button = tk.Button(self, text='Back', command=self.back_action)
        back_button.grid(column=0, row=2,columnspan=4, sticky=(tk.W, tk.E))
        
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

    def back_action(self):
        self.destroy()
   
    def fill_table(self):
        self.clear_all()
        #CODE FOR FILLING BOTH TABLES WITH THE TOP 3 USERS AND THE TOP 3 PLAYLISTS
        a_stats = self.app.getArtistStats(self.app.member.mid)
        for s in a_stats.top_songs:
            self.searchView.insert("",'end',iid=i, values=(s.ID, s.title, s.duration))

        for p in a_stats.top_playlists:
            self.searchView1.insert("",'end',iid=i, values=(p.ID, p.title, p.duration))
