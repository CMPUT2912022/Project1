import tkinter as tk
from Interface.userViewController import *


class PasswordVC(tk.Frame):
    mid = None  # member id
    pwd = None

    def __init__(self, mid, isArtist: bool, isUser: bool, app, parent=None):
        self.mid = mid
        assert type(mid) == str, "Member ID is not of stype String"

        self.isArtist = isArtist
        self.isUser = isUser
        assert isArtist != isUser, "PasswordVC should only be called for logging in a specific account, not an artist & a user."
        self.app = app

        self.parent = parent
        self.pwd = tk.StringVar()

        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        #user_button = tk.Button(self, text='Next', command=self.next_action)
        #artist_button.grid(column=2, row=3)

        # password entry
        pwd_entry = tk.Entry(self, width=15, textvariable=self.pwd, show='*')
        pwd_entry.grid(column=0, row=0, columnspan=3, sticky=(tk.W, tk.E))
        pwd_entry.focus()

        # login button
        next_button = tk.Button(self, text='Login', command=self.login_action)
        next_button.grid(column=3, row=1)
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)


    def login_action(self):
        mid = self.mid
        pwd = self.pwd.get()


        if self.isUser:
            login_success = self.app.userLogin(mid, pwd)
            if login_success:
                uvc = UserVC(self.app, self.parent)

        elif self.isArtist:
            login_success = self.app.artistLogin(mid, pwd)
            # TODO: Complete artist view and transfer

        else: 
            assert False


