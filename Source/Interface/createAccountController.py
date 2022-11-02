import tkinter as tk

from Interface.userViewController import *
from Interface.memberChoiceVC import *
from Interface.artistVC import *


class CreateAccountVC(tk.Frame):
    mid = None  # member id

    def __init__(self, app, parent=None, root = None):
        self.app = app
        self.parent = parent
        self.mid = tk.StringVar()
        self.pwd = tk.StringVar()
        self.name = tk.StringVar()
        
        
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.create_view()

    def create_view(self):
        
        # label 1
        desc1_label = tk.Label(self, text= "UID:", font=(24))
        desc1_label.grid(column=0, row=0)
        
        
        # member id entry
        mid_entry = tk.Entry(self, width=25, textvariable=self.mid)
        mid_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
        mid_entry.focus()

        # label 2
        desc3_label = tk.Label(self, text= "Name:",font=(24))
        desc3_label.grid(column=0, row=1)
        
        # Name entry
        name_entry = tk.Entry(self, width=25, textvariable=self.name)
        name_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        # label 3
        desc2_label = tk.Label(self, text= "Password:",font=(24))
        desc2_label.grid(column=0, row=2)
        
        # password entry
        pwd_entry = tk.Entry(self, width=25, textvariable=self.pwd, show='*')
        pwd_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))


        # create account button
        next_button = tk.Button(self, text='Create Account', command=self.create_action)
        next_button.grid(column=0, row=4,columnspan=2)

        # create account button
        next_button = tk.Button(self, text='Back', command=self.back)
        next_button.grid(column=1, row=5, sticky=(tk.E))
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=6, pady=4)

        
        # ERROR label  
        self.error_label = tk.Label(self, text= "Invalid UID! Please chose a different one.", fg="red")
        self.error_label.grid(column=0, row=3, columnspan=2)
        self.error_label.config(text = "")
        



    def wipe_frame(self):
        for child in self.winfo_children(): 
            if child.winfo_class() == "Entry":
                child.delete(0, "end")
                
    def back(self):
        self.destroy()

    def create_action(self):
        mid = self.mid.get()
        name = self.name.get()
        pwd = self.pwd.get()
        #IF THE UID GIVEN EXISTS ALREADY AS A USER OR AS AN ARTIST WE REJECT AND ASK FOR A DIFFERENT ONE
        isUser = self.app.memberIsUser(mid)
        isArtist = self.app.memberIsArtist(mid)


        if isUser or isArtist:
            self.error_label.config(text="Invalid UID! Please chose a different one.")
        else:
            #HERE WE PUT CODE TO ENTER THE NEW INFO IN TO OUR DATABASE.
            if self.app.registerUser(mid, name, pwd):
                self.error_label.config(text="")
                self.wipe_frame()
                uvc = UserVC(self.app, self.parent, root)
                self.destroy()  # Goes back to login view (relevant only if a user logs out)
            else:
                # Failed to register user
                self.error_label.config(text="Failed to register user.")





































        

   

 
