import tkinter as tk
from tkinter import ttk
from Application.application import *
from Application.dataObjects import *
from math import *

class songVC(tk.Frame):
    def __init__(self, app, parent=None, root = None, itemID = 0):
        self.app = app
        self.parent = parent
        self.itemID = itemID
        root.geometry('320x180')

        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))


        self.create_view()

    def create_view(self):
    
        desc1_label = tk.Label(self, text= f"Song ID: {self.itemID}", font=(24))
        desc1_label.grid(column=0, row=0, columnspan=4)

        search_button = tk.Button(self, text='Play', command=self.listen_action)
        search_button.grid(column=0, row=1)

        up_button = tk.Button(self, text='Info', command=self.info_action)
        up_button.grid(column=1, row=1)
        
        down_button = tk.Button(self, text='Add to playlist', command=self.playlist_action)
        down_button.grid(column=2, row=1)
        
        back_button = tk.Button(self, text='Back', command=self.back_action)
        back_button.grid(column=3, row=1)

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)



    def listen_action(self):
        #CODE FOR LISTENING SESSIONS GOES HERE
        #IF A LISTENING SESSIONS EXISTS FOR THIS USER THEN ADD THIS SONG TO IT
        #IF NOT CREATE A NEW ONE
        pass
    def info_action(self):
        pass


    def playlist_action(self):
        pass


    def back_action(self):
        self.destroy()
