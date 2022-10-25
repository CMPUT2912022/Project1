import tkinter as tk
from Interface.songSearchVC import *
from Interface.artistSearchVC import *

class SessionVC(tk.Frame):  # [US.01.01]
    def __init__(self, app, parent=None):
        self.app = app
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        start_button = tk.Button(self, text='Start Session', command=self.start_action)
        start_button.grid(column=0, row=0)

        end_button = tk.Button(self, text='End Session', command=self.end_action)
        end_button.grid(column=0, row=1)

        back_button = tk.Button(self, text='Back', command=self.back_action)
        back_button.grid(column=0, row=2)

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def start_action(self):
        self.app.startSession()

    def end_action(self):
        self.app.endSession()
        pass

    def back_action(self):
        self.grid_forget()
        #self.destroy()
        #self.update_view()
