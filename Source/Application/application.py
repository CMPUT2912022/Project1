from typing import List
from Application.members import *
from Application.dataObjects import *
import Application.members, sqlite3

import datetime  # [US.01.01]

class Application:
    member: Member = None
    
    dbName = "data.db"
    conn = None
    

    def __init__(self):
        self.__init_database("data.db")
        self.conn = sqlite3.connect(self.dbName)
        return


    def memberIsUser(self, mid: str) -> bool:
        csr = self.conn.cursor()
        query = csr.execute("SELECT * FROM users WHERE uid = ?", (mid,)).fetchone()
        return True if query != None else False


    def memberIsArtist(self, mid: str) -> bool:
        csr = self.conn.cursor()
        query = csr.execute("SELECT * FROM artists WHERE aid = ?", (mid,)).fetchone()
        return True if query != None else False


    def userLogin(self, uid: str, pwd: str) -> bool:  # [US.01.06]
        '''
        For logging in a user (not an artist)!
        '''
        if self.member != None:
            # Log current member out
            # End all of member's sessions
            # TODO
            pass
        csr = self.conn.cursor() 
        query = csr.execute("SELECT uid, name, pwd FROM users WHERE uid = ?", (uid,)).fetchone()
        success = False
        if query != None and query[2] == pwd:
            # Password matches
            self.member = User(uid, query[1])
            success = True
        return success


    def artistLogin(self, aid: str, pwd: str) -> Artist:
        '''
        For logging in an artist.
        '''
        if self.member != None:
            # Log current member out
            # End all of member's sessions
            # TODO
            pass
        csr = self.conn.cursor() 
        query = csr.execute("SELECT aid, name, pwd FROM artists WHERE aid = ?", (aid,)).fetchone()
        success = False
        if query != None and query[2] == pwd:
            # Password matches
            self.member = Artist(aid, query[1])
            success = True
        return success


    def startSession(self):  # [US.01.01]
        # Restrictions: Member must be logged in.
        if self.member != None:
            csr = self.conn.cursor()
            max_sno = csr.execute("SELECT MAX(sno) FROM sessions").fetchone()[0]
            sno = max_sno + 1 if max_sno != None else 0
            csr.execute("INSERT INTO sessions (uid, sno, start, end) VALUES (?,?,?,NULL)", (self.member.mid, sno, datetime.datetime.now()))
            self.conn.commit()
        return
            

    def endSession(self):
        # Restrictions: Member must be logged in.
        if self.member != None:
            csr = self.conn.cursor()
            csr.execute("""
            UPDATE sessions
            SET end = ?
            WHERE 
            uid = ? AND end IS NULL;
                        """, (datetime.datetime.now(), self.member.mid))
            #IN (SELECT s1.sno FROM sessions s1 WHERE s1.end = Null and s1.uid = ?)
            self.conn.commit()
        return

    def getSongDetails(self, sid: int) -> Song:
        pass
    def listenToSong(self, sid: int) -> None:
        pass
    def addSongToPlaylist(self, song: Song) -> None:
        pass


    def searchSongAndPlaylists(self, terms: List[str]) -> List[MusicData]:
        data : List[MusicData]
        csr = self.conn.cursor()
        user_input=raw_input("Enter a song:") 
        #Song Query
        csr.execute(""" 
        SELECT * 
        FROM songs 
        WHERE 
        title LIKE %?;
        """, (user_input,))
        return data 
#
#    #Playlist Query
#    csr.execute("""
#    SELECT p1.pid, p1.title, SUM(p3.duration)
#    FROM playlists p1, plinclude p2, songs p3
#    WHERE 
#    title LIKE %?
#    AND 
#    p1.pid = p2.pid
#    AND 
#    p2.sid = p3.sid
#        """, (user_input,))
#    return data
#    self.conn.commit()
#    return data
#	
	





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

