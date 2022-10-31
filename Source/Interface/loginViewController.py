import tkinter as tk

from Interface.userViewController import *
from Interface.memberChoiceVC import *
from Interface.artistVC import *


class LoginVC(tk.Frame):
    mid = None  # member id

    def __init__(self, app, parent=None):
        self.app = app
        self.parent = parent
        self.mid = tk.StringVar()
        self.pwd = tk.StringVar()
        self.isArtist = False
        self.isUser = False
        
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        # label 1
        desc1_label = tk.Label(self, text= "UID")
        desc1_label.grid(column=0, row=0)
        
        # member id entry
        mid_entry = tk.Entry(self, width=15, textvariable=self.mid)
        mid_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
        mid_entry.focus()

        # label 2
        desc2_label = tk.Label(self, text= "password")
        desc2_label.grid(column=0, row=1)
        
        # password entry
        pwd_entry = tk.Entry(self, width=15, textvariable=self.pwd, show='*')
        pwd_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        # login button
        next_button = tk.Button(self, text='Login', command=self.login_action)
        next_button.grid(column=0, row=2,columnspan=2)
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=6, pady=4)



    def login_action(self):
        mid = self.mid.get()
        pwd = self.pwd.get()
        
        # 1. Check if member is a user or artist
        isUser = self.app.memberIsUser(mid)
        isArtist = self.app.memberIsArtist(mid)

        if mid == "test":
            isUser = True
            isArtist = True
        
        self.isUser = isUser
        self.isArtist = isArtist
        
        
        print("Is User:", isUser, "\nIs Artist:", isArtist)
        
        #REMEMBER TO REMOVE THE TRUES THAT ARE HERE FOR TESTING
        if isUser and isArtist:
            # Give member the choice on who to login as.
            MemberChoiceVC(self.handle_member_choice, self.app, self.parent)
            
        elif self.isUser:
            login_success = self.app.userLogin(mid, pwd)
            login_success = True
            if login_success:
                uvc = UserVC(self.app, self.parent)

        elif self.isArtist:
            login_success = self.app.artistLogin(mid, pwd)
            login_success = True
            if login_success:
                avc = ArtistVC(self.app, self.parent)
            else:
                print("Artist failed to log in")

        else: 
            assert False
            
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

