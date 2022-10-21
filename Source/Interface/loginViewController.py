import tkinter as tk

from Interface.userViewController import *

class LoginVC(tk.Frame):
    def __init__(self, parent=None):
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        mid = tk.StringVar()  # member id
        mid_entry = tk.Entry(self, width=15, textvariable=mid)
        mid_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        mid_entry.focus()

        # password entry
        pwd = tk.StringVar()  # member id
        pwd_entry = tk.Entry(self, width=15, textvariable=pwd, show='*')
        pwd_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        pwd_entry.focus()

        # login button
        login_button = tk.Button(self, text='Login', command=self.login_action)
        login_button.grid(column=2, row=3)
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def login_action(self):
        # 1. Check if login successful

        # 2. Check if member is a user or artist

        # 3. Route accordingly
        uvc = UserVC(self.parent)
        #uvc.grid()
        pass
