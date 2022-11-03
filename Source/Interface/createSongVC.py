import tkinter as tk


class CreateSongVC(tk.Frame):
    mid = None  # member id

    def __init__(self, app, parent=None, root = None):
        self.app = app
        self.parent = parent
        self.mid = tk.StringVar()
        self.length = tk.StringVar()
        self.artists = tk.StringVar()
        
        
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.create_view()

    def create_view(self):
        
        # label 1
        desc1_label = tk.Label(self, text= "Song name:", font=(24))
        desc1_label.grid(column=0, row=0)
        
        
        # song name
        mid_entry = tk.Entry(self, width=25, textvariable=self.mid)
        mid_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
        mid_entry.focus()

        # label 2
        desc3_label = tk.Label(self, text= "Song length:",font=(24))
        desc3_label.grid(column=0, row=1)
        
        # song length
        name_entry = tk.Entry(self, width=25, textvariable=self.length)
        name_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        # label 3
        desc2_label = tk.Label(self, text= "Supporting artist ID:",font=(24))
        desc2_label.grid(column=0, row=2)
        
        # supporting artists
        pwd_entry = tk.Entry(self, width=25, textvariable=self.artists, show='*')
        pwd_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))


        # create account button
        next_button = tk.Button(self, text='Submit', command=self.create_action)
        next_button.grid(column=0, row=4,columnspan=2)

        # create account button
        next_button = tk.Button(self, text='Back', command=self.back)
        next_button.grid(column=1, row=4, sticky=(tk.E))
        
        for child in self.winfo_children(): 
            child.grid_configure(padx=6, pady=4)

        
        # ERROR label  
        self.error_label = tk.Label(self, text= "Song already exists! C'mon, I'm sure you can think of something new.", fg="red")
        self.error_label.grid(column=0, row=3, columnspan=2)
        self.error_label.config(text = "")
        



    def wipe_frame(self):
        for child in self.winfo_children(): 
            if child.winfo_class() == "Entry":
                child.delete(0, "end")
                
    def back(self):
        self.destroy()

    def create_action(self):
        #HERE GOES CODE TO CHECK IF THE USERS INPUT SONG NAME AND SONG LENGTH ALREADY EXIST
        #IF THEY DO WE CHANGE THE ERROR LABEL BACK TO WHAT IT IS ABOVE
        #IF THE SONG IS NEW AND DOESNT MATCH ANYTHING WE ALREADY HAVE IT IS ADDED
        #WITH THE INFORMATION PROVIDED AND THE WINDOW DESTROY WITH SELF.DESTROY() TO GO BACK
        #TO THE MAIN ARTIST vc
        #CODE SHOULD BE SIMILAR TO THE ONE USED IN THE ACCOUNTCREATIONCONTROLLER.PY

        s = self.app.addSong(self.mid, self.length, self.artists)
        if s != None:
            self.error_label.config(text="Song created successfully", fg="green")

        else:
            self.error_label.config(text="Song already exists! C'mon, I'm sure you can think of something new.", fg="red")





































        

   

 
