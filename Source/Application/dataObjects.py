
class MusicData:
    ID : int
    title : str
    duration : int

    def __init__(self, ID, title, duration):
        self.ID = ID
        self.title = title
        self.duration = duration
        return
    

class Song(MusicData):
    pass

class Playlist(MusicData):
    pass


