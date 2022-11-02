import tkinter as tk
from Interface.userViewController import *


class MemberChoiceVC(tk.Frame):
    def __init__(self, handler, app, parent=None):
        self.app = app
        self.parent = parent
        self.handler = handler

        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        user_button = tk.Button(self, text='Login as User', command=self.user_action)
        user_button.grid(column=0, row=0)

        artist_button = tk.Button(self, text='Login as Artist', command=self.artist_action)
        artist_button.grid(column=1, row=0)
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)


    def user_action(self):
        self.handler(True)
        self.grid_forget()
        #self.destroy()

    def artist_action(self):
        self.handler(False)
        self.grid_forget()
        #self.destroy()
