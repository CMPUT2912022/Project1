from typing import List
from Application.members import *
from Application.dataObjects import *
import Application.members, sqlite3

import datetime  # [US.01.01]

class Application:
    member: Member = None
    
    conn = None
    

    def __init__(self, db="data.db"):
        self.__init_database(db)
        self.conn = sqlite3.connect(db)
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

    def getSongDetails(self, sid: int) -> SongDetails:
        csr = self.conn.cursor()
        query1 = """
        SELECT title, duration
        FROM songs
        WHERE sid = {s_sid};
        """.format(s_sid=sid)

        query2 = """
        SELECT a.aid, a.name 
        FROM artists a
        JOIN perform p ON p.aid = a.aid
        WHERE p.sid = {s_sid};
        """.format(s_sid=sid)
       
        query3 = """
        SELECT p.title FROM playlists p
        JOIN plinclude pi ON p.pid = pi.pid
        WHERE pi.sid = {sid}
        GROUP BY p.pid
        """.format(sid=sid)

        result1=csr.execute(query1).fetchone()
        result2=csr.execute(query2).fetchall()
        result3=csr.execute(query3).fetchall()

        title = result1[0]
        duration = result1[1]
        
        artists = []
        for row in result2:
            artists.append(Artist(row[0],row[1]))

        playlist_names = []
        for row in result3:
            playlist_names.append(row[0])

        return SongDetails(sid, title, duration, artists, playlist_names)

	
    def listenToSong(self, sid: int) -> None:
        pass

    def addSongToPlaylist(self, pid: int, song: Song) -> None:
        csr=self.conn.cursor()
        csr.execute("""
        INSERT INTO plinclude (sid)
        VALUES (?)""", (sid,))
        self.conn.commit()


    def searchSongAndPlaylists(self, terms: List[str]) -> List[MusicData]:
        data = []
        if terms == None or len(terms)==0:
            return data
        csr = self.conn.cursor()
        # Song Query
        where_clause = " OR title ".join(["LIKE '%' || ? || '%'" for k in terms])
        hit_clause = " + ".join(["(title LIKE '%' || ? || '%')" for k in terms])
        query = """
            SELECT sid, title, duration, {hit_clause}
            FROM songs
            WHERE title {where_clause}
            ORDER BY {hit_clause} DESC;
            """.format(where_clause = where_clause, hit_clause = hit_clause)
        results = csr.execute(query, terms + terms + terms).fetchall()

        for row in results:
            data.append((row[3], Song(row[0], row[1], row[2])))

        # Playlist query
        where_clause = " OR p.title ".join(["LIKE '%' || ? || '%'" for k in terms])
        hit_clause = " + ".join(["(p.title LIKE '%' || ? || '%')" for k in terms])
        query = """
            SELECT p.pid, p.title, SUM(s.duration), {hit_clause}
            FROM playlists p
            JOIN plinclude pi ON p.pid = pi.pid
            JOIN songs s ON s.sid = pi.sid
            WHERE p.title {where_clause}
            GROUP BY p.pid
            ORDER BY {hit_clause} DESC;
            """.format(where_clause = where_clause, hit_clause = hit_clause)
        results = csr.execute(query, terms+terms+terms ).fetchall()

        for row in results:
            data.append((row[3], Playlist(row[0], row[1], row[2])))

        # Sort data (not sorted since playlists added)
        data = sorted(data, key=lambda x: x[0], reverse=True)
        return data


    def getPlaylistDetails(self, pid: int) -> PlaylistDetails:
        csr = self.conn.cursor()
        p_details = csr.execute("SELECT pid, title FROM playlists WHERE pid = ?", (pid,)).fetchone()

        s_query = csr.execute("""
        SELECT s.sid, s.title, s.duration FROM songs s 
        JOIN plinclude pi ON pi.sid = s.sid
        WHERE pi.pid = ?;
                              """, (pid,)).fetchall()
        songs = []  # [Song]
        for row in s_query:
            songs.append(Song(row[0], row[1], row[2]))
        return PlaylistDetails(pid, p_details[1], songs)




    def searchPlaylist(self, pid: int) -> List[Song]:
        pass

    def getArtistDetails(self, aid: str) -> Artist:
        pass

    def addSong(self, title: str, duration: int, artists: List[str]) -> Song:
        '''
        addSong function lets artists add new songs to db. 
        returns None if song is already in db otherwise returns Song
        ''' 
        csr = self.conn.cursor()
        max_sid = csr.execute("SELECT MAX(sid) FROM songs").fetchone()[0]
        query = csr.execute(""" 
        SELECT * 
        FROM songs s 
        WHERE 
        s.title = ?
        AND 
        s.duration = ?;
        """, (title,duration))
        
        if query == None: 
            csr.execute(""" 
            INSERT INTO songs  
            VALUES (?,?,?);
            """, (max_sid+1, title, duration))        
            
            for i in artists: 
                csr.execute(""" 
                INSERT INTO perform (aid) 
                VALUES (?,?);
                """, (artists[i], max_sid+1))

            return Song(max_sid+1, title, duration)
        else:
            return None 
        



    def getArtistStats(self, aid: str) -> ArtistStats:  # [US.06.02]
        '''
        returns stats on a particular artist
        '''
        csr = self.conn.cursor() 

        # Top three listeners (users) by playtime
        top_users_query = csr.execute("""SELECT u.uid, u.name, SUM(l.cnt) FROM users u
            JOIN listen l ON u.uid = l.uid
            JOIN perform p ON l.sid = p.sid
            WHERE p.aid = ?
            GROUP BY p.aid
            SORT BY sum(l.cnt)
            LIMIT 3;
            """, (aid,))


        # Top 3 playlists that include the largest number of their songs
        top_playlists_query = csr.execute("""SELECT p.pid, p.title, SUM(), COUNT(pinc.sid) FROM playlists p
            JOIN plinclude pinc ON p.pid = pinc.pid
            JOIN perform perf ON p.sid = perf.sid
            WHERE a.aid = ?
            GROUP BY p.pid, a.aid
            SORT BY COUNT(pinc.sid)
            LIMIT 3;""", (aid,))


        users = [User(q[1], q[2]) for q in top_users_query.fetchall()]
        playlists = [Playlist(q[1], q[2]) for q in top_users_query.fetchall()]
        return ArtistStats(users, playlists)
        


    def addSong(self, title: str, duration: int) -> None:
        pass

    def searchArtists(self, terms: List[str]) -> List[Artist]:
        data=[]
        csr=self.conn.cursor()

        where_clause = " OR name ".join(["LIKE '%' || ? || '%'" for i in terms])
        query = """
            SELECT a.name, a.nationality, COUNT(p.sid)
            FROM artists a, perform p
            WHERE a.name {where_clause};
            """.format(where_clause = where_clause)
            
        results = csr.execute(query, tuple(terms)).fetchall()

        for row in results:
            data.append((1, Artists(row[0],row[1],row[2])))


    def __init_database(self, dbName):
        #with open("Application/init_tables.sql", 'r') as fo:
        with open("Application/prj-tables.sql", 'r') as fo:
            conn = sqlite3.connect(dbName)
            csr = conn.cursor()
            try:
                query = csr.execute("SELECT 1 FROM sqlite_master WHERE type='table';").fetchone()
                if query == None:
                    csr.executescript(fo.read())
                    conn.commit()
            except sqlite3.Error as e:
                print("\nError while initializing database: \n", e)

            finally:
                conn.close()
        return

