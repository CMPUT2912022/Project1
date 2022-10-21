import tkinter as tk

class UserVC(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_view()

    def create_view(self):
        session_button = tk.Button(self, text='Session Manager', command=self.session_action)
        session_button.grid(column=1, row=1)

        song_search_button = tk.Button(self, text='Search Songs', command=self.song_search_action)
        song_search_button.grid(column=2, row=1)

        artist_search_button = tk.Button(self, text='Search Artists', command=self.artist_search_action)
        artist_search_button.grid(column=3, row=1)
        
        logout_button = tk.Button(self, text='Logout', command=self.logout_action)
        logout_button.grid(column=4, row=1)

        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def session_action(self):
        pass

    def song_search_action(self):
        pass

    def artist_search_action(self):
        pass

    def logout_action(self):
        self.grid_forget()
