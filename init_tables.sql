--users(uid, name, pwd)
CREAT TABLE users (
    uid     CHAR(25)    NOT NULL UNIQUE,
    name    CHAR(25),
    pwd     CHAR(25)    NOT NULL,
    PRIMARY KEY (uid)
);

--songs(sid, title, duration)
CREATE TABLE songs (
    sid INT,
    title TEXT,
    duration INT,
    PRIMARY KEY (sid)
);

--sessions(uid, sno, start, end)
CREATE TABLE sessions (
    uid CHAR(25),
    sno INT,
    start INT,
    end INT
    PRIMARY KEY (uid, sno),
    FOREIGN KEY (uid)
);

--listen(uid, sno, sid, cnt)
CREATE TABLE listen (
    uid CHAR(25),
    sno INT,
    sid INT,
    cnt INT,
    PRIMARY KEY (uid, sno, sid),
    FOREIGN KEY (uid, sno, sid)
);

--playlists(pid, title, uid)
CREATE TABLE playlists (
    pid INT,
    title TEXT,
    uid CHAR(25),
    PRIMARY KEY (pid, uid),
    FOREIGN KEY (uid)
);

--plinclude(pid, sid, sorder)
CREATE TABLE plinclude (
    pid INT,
    sid INT,
    sorder INT,
    PRIMARY KEY (pid, sid, sorder),
    FOREIGN KEY (pid, sid)
);

--artists(aid, name, nationality, pwd)
CREATE TABLE artists (
    aid CHAR(25),
    name TEXT,
    nationality TEXT,
    pwd TEXT,
    PRIMARY KEY (aid)
);

--perform(aid, sid)
CREATE TABLE perform (
    aid CHAR(25),
    sid INT,
    PRIMARY KEY (aid, sid),
    FOREIGN KEY (aid, sid)
);

