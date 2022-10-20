from typing import List
from Application.members import *
from Application.dataObjects import *
import Application.members, sqlite3


class Application:
    member: Member = None

    
    # public
    def __init__(self):
        self.__init_database("data.db")
        return

    def userLogin(self, uid: str, pwd: str) -> User:
        pass
    def artistLogin(self, aid: str, pwd: str) -> Artist:
        pass
    def getSongDetails(self, sid: int) -> Song:
        pass
    def listenToSong(self, sid: int) -> None:
        pass
    def addSongToPlaylist(self, song: Song) -> None:
        pass
    def searchSong(self, search: str) -> List[Song]:
        pass
    def getPlaylistDetails(self, pid: int) -> Playlist:
        pass
    def searchPlaylist(self, pid: int) -> List[Song]:
        pass
    def getArtistDetails(self, aid: str) -> Artist:
        pass
    def addSong(self, title: str, duration: int) -> None:
        pass
    def searchArtists(self, search: str) -> List[Artist]:
        pass


    # private
    def __init_database(self, dbName):
        with open("Application/init_tables.sql", 'r') as fo:
            conn = sqlite3.connect(dbName)
            csr = conn.cursor()
            try:
                csr.executescript(fo.read())
                conn.commit()
            except sqlite3.Error as e:
                print("\nError while initializing database: \n", e)

            finally:
                conn.close()
        return

