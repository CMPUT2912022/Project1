--    users(uid, name, pwd)
--    songs(id, title, duration)
--    sessions(uid, sno, start, end)
--    listen(uid, sno, sid, cnt)
--    playlists(pid, title, uid)
--    plinclude(pid, sid, sorder)
--    artists(aid, name, nationality, pwd)
--    perform(aid, sid)


INSERT INTO users (uid, name, pwd) VALUES
(1, "Jack", "pwd1"),
(2, "Noah", "easypwd"),
(3, "Nolan", "easierpwd"),
(4, "Seth", "pwd2"),
(5, "Andrew", "passwd");


INSERT INTO songs (sid, title, duration) VALUES
(0, "Luckenbach, Texas", 202),
(1, "Act Naturally", 141),
(2, "My Friends Are Gonna Be Strangers", 148),
(3, "My Heroes Have Always Been Cowboys", 183),
(4, "Every Bad Habit", 204),
(5, "A Country Boy Can Survive", 255),
(6, "Sicko Mode", 312);


INSERT INTO artists (aid, name, nationality, pwd) VALUES
(1, "Waylon Jennings", "American", "2212"),
(2, "Buck Owens", "American", "14tw"),
(3, "Merle Haggard", "American", "sfgagfsab"),
(4, "The Strangers", "American", "gbhbhasbvhs"),
(5, "Willie Nelson", "American", "gkvuabfhwdisgky"),
(6, "Mickey Lamantia", "American", "823haf"),
(7, "Hank Williams, Jr.", "american", "ndsjjdsjks"),
(8, "Travis Scott", "American", "1111");


INSERT INTO perform (aid, sid) VALUES
(1,0),
(2,1),
(3,2),
(4,2),
(5,3),
(6,4),
(7,5),
(8,6);


INSERT INTO playlists (pid, title, uid) VALUES
(1, "Country for the Boys", 2),
(2, "Certified Bangers", 5);


INSERT INTO plinclude (pid, sid, sorder) VALUES
(1,1,1),
(1,2,2),
(1,3,3),
(1,4,4),
(1,5,5),
(1,6,6),
(1,7,7),
(2,8,8);

