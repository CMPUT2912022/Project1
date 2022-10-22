import tkinter as tk

from Interface.userViewController import *

class LoginVC(tk.Frame):
    mid = None  # member id
    pwd = None

    def __init__(self, app, parent=None):
        self.app = app
        self.parent = parent
        self.mid = tk.StringVar()
        self.pwd = tk.StringVar()

        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        mid_entry = tk.Entry(self, width=15, textvariable=self.mid)
        mid_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        mid_entry.focus()

        # password entry
        #pwd_entry = tk.Entry(self, width=15, textvariable=self.pwd, show='*')
        #pwd_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        #pwd_entry.focus()

        # login button
        next_button = tk.Button(self, text='Next', command=self.next_action)
        next_button.grid(column=2, row=3)
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def next_action(self):
        # 1. Check if member is a user or artist

        # 2. Check if login successful
        login_success = self.app.userLogin(self.mid.get(), self.pwd.get())


        # 3. Route accordingly
        if login_success:
            uvc = UserVC(self.app, self.parent)
            #uvc.grid()
            #self.grid_forget()
        else:
            # Raise error
            pass

