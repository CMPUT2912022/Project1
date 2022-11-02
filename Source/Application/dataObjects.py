
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


class ArtistStats:
    top_songs = []
    top_playlists = []

    def __init__(self, top_songs, top_playlists):
        self.top_songs = top_songs
        self.top_playlists = top_playlists
