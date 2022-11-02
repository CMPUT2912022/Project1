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


    def registerUser(self, uid: str, name: str, pwd: str) -> bool:
        '''
        Registers a user, also logs them in. Can be assumed self.member will be set
        after successfully calling this function.
        Returns bool indicating whether registration was successful.
        '''
        if self.memberIsUser(uid) or self.memberIsArtist(uid) or uid == "" or name == "" or pwd == "":
            return False
        else:
            csr = self.conn.cursor() 
            query = csr.execute("INSERT INTO users VALUES (?, ?, ?);", (uid, name, pwd))
            self.conn.commit()
            self.member = User(uid, name)
            return True
        

    def testUserCredentials(self, uid: str, pwd: str):  # [US.01.06]
        '''
        For testing a user's login credentials (without actually logging them in)
        returns None if failed, otherwise returns User
        '''
        csr = self.conn.cursor() 
        query = csr.execute("SELECT uid, name, pwd FROM users WHERE uid = ?", (uid,)).fetchone()
        success = None
        if query != None and query[2] == pwd:
            # Password matches
            success = User(uid, query[1])
        return success


    def userLogin(self, uid: str, pwd: str) -> bool:  # [US.01.06]
        '''
        For logging in a user (not an artist)!
        '''
        if self.member != None:
            # Log current member out
            self.logout()
        credentialTest = self.testUserCredentials(uid, pwd)
        success = False
        if credentialTest != None:
            # Password matches
            self.member = credentialTest
            success = True
        return success
    

    def testArtistCredentials(self, aid: str, pwd: str):  # [US.01.06]
        '''
        For testing an artist's login credentials (without actually logging them in)
        returns None if failed, otherwise returns Artist 
        '''
        csr = self.conn.cursor() 
        query = csr.execute("SELECT aid, name, pwd FROM artists WHERE aid = ?", (aid,)).fetchone()
        success = None
        if query != None and query[2] == pwd:
            # Password matches
            success = Artist(aid, query[1])  # TODO: Get nationality too
        return success


    def artistLogin(self, aid: str, pwd: str) -> bool:
        '''
        For logging in an artist.
        '''
        if self.member != None:
            self.logout()
        credentialTest = self.testArtistCredentials(aid, pwd)
        success = False
        if credentialTest != None:
            # Password matches
            self.member = credentialTest
            success = True
        return success


    def logout(self):
        '''
        Handles logging out members (artist and user)
        '''
        if isinstance(self.member, User):
            # Handle user logout
            self.endSession()
            self.member = None
        elif isinstance(self.member, Artist):
            # Handle artist logout
            self.member = None
        return


    def startSession(self):  # [US.01.01]
        # Restrictions: Member must be logged in, and only one session can be open at a time.
        self.endSession()  # Close all sessions that were previously open.

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
            self.conn.commit()
        return

    def getSongDetails(self, sid: int) -> Song:
        pass
    def listenToSong(self, sid: int) -> None:
        pass

    def addSongToPlaylist(self, pid: int, song: Song) -> None:
        csr=self.conn.cursor()
        csr.execute("""
        INSERT INTO plinclude (sid)
        VALUES (sid)""")


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

        #Playlist Query
        csr.execute("""
        SELECT p1.pid, p1.title, SUM(p3.duration)
        FROM playlists p1, plinclude p2, songs p3
        WHERE 
        title LIKE %?
        AND 
        p1.pid = p2.pid
        AND 
        p2.sid = p3.sid;
            """, (user_input,))
        self.conn.commit()
        return data
	
	





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

