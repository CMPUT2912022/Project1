import tkinter as tk

from Interface.userViewController import *
from Interface.memberChoiceVC import *
from Interface.passwordVC import *


class LoginVC(tk.Frame):
    mid = None  # member id

    def __init__(self, app, parent=None):
        self.app = app
        self.parent = parent
        self.mid = tk.StringVar()

        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        # member id entry
        mid_entry = tk.Entry(self, width=15, textvariable=self.mid)
        mid_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        mid_entry.focus()

        # next button
        next_button = tk.Button(self, text='Next', command=self.next_action)
        next_button.grid(column=2, row=3)
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)


    def next_action(self):
        mid = self.mid.get()

        # 1. Check if member is a user or artist
        isUser = self.app.memberIsUser(mid)
        isArtist = self.app.memberIsArtist(mid)
        print("Is User:", isUser, "\nIs Artist:", isArtist)

        if isUser and isArtist:
            # Give member the choice on who to login as.
            MemberChoiceVC(self.handle_member_choice, self.app, self.parent)

        elif isUser:
            PasswordVC(mid=mid, isArtist=False, isUser=True, app=self.app, parent=self.parent)

        elif isArtist:
            PasswordVC(mid=mid, isArtist=True, isUser=False, app=self.app, parent=self.parent)

    
    def handle_member_choice(self, user: bool):
        '''
        Callback for getting choice on whether member should login as user or artist.
        If user = True, will get password for user; if False, will get password for artist.
        '''
        mid = self.mid.get()
        if user:
            PasswordVC(mid=mid, isArtist=False, isUser=True, app=self.app, parent=self.parent)

        else:
            PasswordVC(mid=mid, isArtist=True, isUser=False, app=self.app, parent=self.parent)

