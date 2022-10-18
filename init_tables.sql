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

--playlists(pid, title, uid)

--plinclude(pid, sid, sorder)

--artists(aid, name, nationality, pwd)

--perform(aid, sid)

