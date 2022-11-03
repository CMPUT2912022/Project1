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
        self.root = root
        self.mid = tk.StringVar()
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.create_view()

    def create_view(self):
    
        desc1_label = tk.Label(self, text= f"Song ID: {self.itemID}", font=(20))
        desc1_label.grid(column=0, row=0, columnspan=4, sticky=(tk.N, tk.W, tk.E, tk.S))
        #artist name
        desc2_label = tk.Label(self, text= "", font=(20))
        desc2_label.grid(column=0, row=1, columnspan=4, sticky=(tk.N, tk.W, tk.E, tk.S))
        #song title
        desc4_label = tk.Label(self, text= "", font=(20))
        desc4_label.grid(column=0, row=2, columnspan=4, sticky=(tk.N, tk.W, tk.E, tk.S))
        #song duration
        desc5_label = tk.Label(self, text= "", font=(20))
        desc5_label.grid(column=0, row=3, columnspan=4, sticky=(tk.N, tk.W, tk.E, tk.S))
        #list of playslists the song is in
        desc6_label = tk.Label(self, text= "", font=(20))
        desc6_label.grid(column=0, row=4, columnspan=4, sticky=(tk.N, tk.W, tk.E, tk.S))

        search_button = tk.Button(self, text='Play', command=self.listen_action)
        search_button.grid(column=0, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))

        up_button = tk.Button(self, text='Info', command=self.info_action)
        up_button.grid(column=1, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        down_button = tk.Button(self, text='Add to playlist', command=self.playlist_action)
        down_button.grid(column=2, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        back_button = tk.Button(self, text='Back', command=self.back_action)
        back_button.grid(column=3, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        mid_entry = tk.Entry(self, width=15, textvariable=self.mid)
        mid_entry.grid(column=2, row=6,sticky=(tk.N, tk.W, tk.E, tk.S))
        mid_entry.focus()

        for child in self.winfo_children(): 
            child.grid_configure(padx=10, pady=5)



    def listen_action(self):
        #CODE FOR LISTENING SESSIONS GOES HERE
        #IF A LISTENING SESSIONS EXISTS FOR THIS USER THEN ADD THIS SONG TO IT
        #IF NOT CREATE A NEW ONE
        pass
    def info_action(self):
        #CODE FOR GETTING A SONGS INFO GOES HERE, THEN IT JUST NEEDS TO BE ADDED TO THE LABELS

        sd = self.app.getSongDetails(self.itemID)  # Returns SongDetails(sid, title, duration, artists, playlist_names)
        #TODO
        print(sd)
        print(sd.sid, sd.title, sd.duration, sd.artists, sd.playlist_names)


    def playlist_action(self):
        #ADD SONG TO PLAYLIST, NAME OF PLAYLIST IS IN SELF.MID
        pass


    def back_action(self):
        self.destroy()
