import tkinter as tk

from Interface.userViewController import *
from Interface.memberChoiceVC import *
from Interface.artistVC import *
from Interface.createAccountController import *


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

        # label or
        desc1_label = tk.Label(self, text= "or", font=(24))
        desc1_label.grid(column=0, row=4,columnspan=2)
        
        # label 1
        desc1_label = tk.Label(self, text= "UID:", font=(24))
        desc1_label.grid(column=0, row=0)
        
        # member id entry
        mid_entry = tk.Entry(self, width=25, textvariable=self.mid)
        mid_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
        mid_entry.focus()

        # label 2
        desc2_label = tk.Label(self, text= "Password:",font=(24))
        desc2_label.grid(column=0, row=1)
        
        # password entry
        pwd_entry = tk.Entry(self, width=25, textvariable=self.pwd, show='*')
        pwd_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        # login button
        next_button = tk.Button(self, text='Login', command=self.login_action)
        next_button.grid(column=0, row=3,columnspan=2)

        # create account button
        next_button = tk.Button(self, text='Create Account', command=self.create_account)
        next_button.grid(column=0, row=5,columnspan=2)
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=6, pady=4)

        
        # ERROR label  
        self.error_label = tk.Label(self, text= "The information you've entered is incorrect.", fg="red")
        self.error_label.grid(column=0, row=2, columnspan=2)
        self.error_label.config(text = "")
        



    def wipe_frame(self):
        for child in self.winfo_children(): 
            if child.winfo_class() == "Entry":
                child.delete(0, "end")
        
        
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
        login_success_user = self.app.testUserCredentials(mid, pwd)
        login_success_artist = self.app.testArtistCredentials(mid, pwd)
        
        
        print("Is User:", isUser, "\nIs Artist:", isArtist)
        
        if isUser and isArtist:
            login_success_user = self.app.testUserCredentials(mid, pwd)
            login_success_artist = self.app.testArtistCredentials(mid, pwd)

            if login_success_user and login_success_artist: 
                # Give member the choice on who to login as.
                self.error_label.config(text = "")
                self.wipe_frame()
                MemberChoiceVC(self.handle_member_choice, self.app, self.parent)
            elif login_success_user:
                self.error_label.config(text = "")
                self.wipe_frame()
                uvc = UserVC(self.app, self.parent)
            elif login_success_artist:
                self.error_label.config(text = "")
                self.wipe_frame()
                avc = ArtistVC(self.app, self.parent)
            else:
                # error label
                self.error_label.config(text = "The information you've entered is incorrect.")
            
        elif self.isUser:
            login_success = self.app.userLogin(mid, pwd)
            if login_success:
                self.error_label.config(text = "")
                self.wipe_frame()
                uvc = UserVC(self.app, self.parent)
            else:
                # error label
                self.error_label.config(text = "The information you've entered is incorrect.")

        elif self.isArtist:
            login_success = self.app.artistLogin(mid, pwd)
            if login_success:
                self.error_label.config(text = "")
                self.wipe_frame()
                avc = ArtistVC(self.app, self.parent)
            else:
                # error label
                self.error_label.config(text = "The information you've entered is incorrect.")
        else:
            # error label
            self.error_label.config(text = "The information you've entered is incorrect.")


    def create_account(self):
        cavc = CreateAccountVC(self.app, self.parent)

    
    def handle_member_choice(self, user: bool):
        '''
        Callback for getting choice on whether member should login as user or artist.
        If user = True, will get password for user; if False, will get password for artist.
        '''
        mid = self.mid.get()
        if user:
            self.app.userLogin(mid, pwd)
            UserVC(self.app, self.parent)

        else:
            self.app.artistLogin(mid, pwd)
            ArtistVC(self.app, self.parent)

