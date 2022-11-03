--    users(uid, name, pwd)
--    songs(id, title, duration)
--    sessions(uid, sno, start, end)
--    listen(uid, sno, sid, cnt)
--    playlists(pid, title, uid)
--    plinclude(pid, sid, sorder)
--    artists(aid, name, nationality, pwd)
--    perform(aid, sid)


INSERT INTO users (uid, name, pwd) VALUES
("JCK", "Jack", "pwd1"),
("NOAH", "Noah", "easypwd"),
("NOL", "Nolan", "easierpwd"),
("SETH", "Seth", "pwd2"),
("ADRW", "Andrew", "passwd"),
("chm", "Connor", "pwd");


INSERT INTO songs (sid, title, duration) VALUES
(0, "Luckenbach, Texas", 202),
(1, "Act Naturally", 141),
(2, "My Friends Are Gonna Be Strangers", 148),
(3, "My Heroes Have Always Been Cowboys", 183),
(4, "Every Bad Habit", 204),
(5, "A Country Boy Can Survive", 255),
(6, "Sicko Mode", 312);


INSERT INTO artists (aid, name, nationality, pwd) VALUES
("WAY", "Waylon Jennings", "American", "2212"),
("BUCK", "Buck Owens", "American", "14tw"),
("MERL", "Merle Haggard", "American", "sfgagfsab"),
("STRA", "The Strangers", "American", "gbhbhasbvhs"),
("WILY", "Willie Nelson", "American", "gkvuabfhwdisgky"),
("MICK", "Mickey Lamantia", "American", "823haf"),
("HANK", "Hank Williams, Jr.", "american", "ndsjjdsjks"),
("TRVS", "Travis Scott", "American", "1111"),
("chm", "Connor", "Canadian", "pwd");


INSERT INTO perform (aid, sid) VALUES
("WAY",0),
("BUCK",1),
("MERL",2),
("STRA",2),
("WILY",3),
("MICK",4),
("HANK",5),
("TRVS",6);


INSERT INTO playlists (pid, title, uid) VALUES
(1, "Country for the Boys", 2),
(2, "Certified Bangers", 5);


INSERT INTO plinclude (pid, sid, sorder) VALUES
(1,0,0),
(1,1,1),
(1,2,2),
(1,3,3),
(1,4,4),
(1,5,5),
(2,6,1);

