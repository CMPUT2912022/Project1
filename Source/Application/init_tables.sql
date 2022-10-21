PRAGMA foreign_keys = ON;

--users(uid, name, pwd)
CREATE TABLE IF NOT EXISTS users (
    uid     CHAR(25)    NOT NULL UNIQUE,
    name    CHAR(25),
    pwd     CHAR(25)    NOT NULL,
    PRIMARY KEY (uid)
);

--songs(sid, title, duration)
CREATE TABLE IF NOT EXISTS songs (
    sid INT,
    title TEXT,
    duration INT,
    PRIMARY KEY (sid)
);

--sessions(uid, sno, start, end)
CREATE TABLE IF NOT EXISTS sessions (
    uid CHAR(25),
    sno INT,
    start INT,
    end INT,
    PRIMARY KEY (uid, sno),
    FOREIGN KEY (uid) REFERENCES users(uid)
);

--listen(uid, sno, sid, cnt)
CREATE TABLE IF NOT EXISTS listen (
    uid CHAR(25),
    sno INT,
    sid INT,
    cnt INT,
    PRIMARY KEY (uid, sno, sid),
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (sno) REFERENCES sessions(sno),
    FOREIGN KEY (sid) REFERENCES songs(sid)
);

--playlists(pid, title, uid)
CREATE TABLE IF NOT EXISTS playlists (
    pid INT,
    title TEXT,
    uid CHAR(25),
    PRIMARY KEY (pid),
    FOREIGN KEY (uid) REFERENCES users(uid)
);

--plinclude(pid, sid, sorder)
CREATE TABLE IF NOT EXISTS plinclude (
    pid INT,
    sid INT,
    sorder INT,
    PRIMARY KEY (pid, sid, sorder),
    FOREIGN KEY (pid) REFERENCES playlists(pid),
    FOREIGN KEY (sid) REFERENCES songs(sid)
);

--artists(aid, name, nationality, pwd)
CREATE TABLE IF NOT EXISTS artists (
    aid CHAR(25),
    name TEXT,
    nationality TEXT,
    pwd TEXT,
    PRIMARY KEY (aid)
);

--perform(aid, sid)
CREATE TABLE IF NOT EXISTS perform (
    aid CHAR(25),
    sid INT,
    PRIMARY KEY (aid, sid),
    FOREIGN KEY (aid) REFERENCES artists(aid),
    FOREIGN KEY (sid) REFERENCES songs(sid)
);

