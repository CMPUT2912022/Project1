import tkinter as tk

from Interface.createSongVC import *
from Interface.artistTOPVC import *

class ArtistVC(tk.Frame):
    def __init__(self, app, parent=None, root = None):
        self.app = app
        self.parent = parent
        self.root = root
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        create_song_button = tk.Button(self, text='Create Song', command=self.create_song_action)
        create_song_button.grid(column=0, row=1, sticky=(tk.W, tk.E))

        stats_button = tk.Button(self, text='Artist Stats', command=self.artist_stats_action)
        stats_button.grid(column=1, row=1, sticky=(tk.W, tk.E))

        logout_button = tk.Button(self, text='Logout', command=self.logout_action)
        logout_button.grid(column=2, row=1, sticky=(tk.W, tk.E))

        exit_button = tk.Button(self, text='Exit', command=self.exitpg)
        exit_button.grid(column=3, row=1, sticky=(tk.W, tk.E))

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def create_song_action(self):
        csvc = CreateSongVC(self.app, self.parent, self.root)

    def artist_stats_action(self):
        asvc = artistStatsVC(self.app, self.parent, self.root)

    def logout_action(self):
        #self.grid_forget()
        self.destroy()
        
    def exitpg(self):
        exit(0)
