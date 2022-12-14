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

class ArtistDetails: 
    aid = None
    name = ""
    songs=[]
    def __init__(self, aid, name, songs):
        self.aid = aid
        self.name = name
        self.songs = songs

class SongDetails:
    sid = None
    title = ""
    duration = None
    artists = []  # [Artist]
    playlist_names = []  # [string]
    def __init__(self, sid, title, duration, artists, playlist_names):
        self.sid = sid
        self.title = title
        self.duration = duration
        self.artists = artists
        self.playlist_names = playlist_names


class PlaylistDetails:
    pid = None
    title = ""
    songs = []
    def __init__(self, pid, title, songs):
        self.pid = pid
        self.title = title
        self.songs = songs
