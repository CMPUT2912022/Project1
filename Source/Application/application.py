from typing import List
import members

class Application:
    member: Member = None


    def userLogin(uid: str, pwd: str) -> User:
        pass
    def artistLogin(aid: str, pwd: str) -> Artist:
        pass
    def getSongDetails(sid: int) -> Song:
        pass
    def listenToSong(sid: int) -> None:
        pass
    def addSongToPlaylist(song: Song) -> None:
        pass
    def searchSong(search: str) -> List[Song]:
        pass
    def getPlaylistDetails(pid: int) -> Playlist:
        pass
    def searchPlaylist(pid: int) -> List[Song]:
        pass
    def getArtistDetails(aid: str) -> Artist:
        pass
    def addSong(title: str, duration: int) -> None:
        pass
    def searchArtists(search: str) -> List[Artist]:
        pass
