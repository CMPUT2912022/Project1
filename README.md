# Project1
Enterprise Database

## Tables
- users(*uid*, name, pwd)
  - PK: uid
- songs(*id*, title, duration)
  - PK: id
- sessions(*uid*, *sno*, start, end)
  - PK: uid, sno
  - FK: uid
- listen(*uid*, *sno*, *sid*, cnt)
  - PK: uid, sno, sid
  - FK: uid, sno, sid
  - NOTES:
    - Weak entity
- playlists(*pid*, title, *uid*)
  - PK: pid
- plinclude(*pid*, *sid*, sorder)
  - PK: pid, sid
  - FK: pid, sid
  - NOTES:
    - Weak entity
- artists(*aid*, name, nationality, pwd)
  - PK: aid
- perform(*aid*, *sid*)
  - PK: aid, sid
  - FK: aid, sid
  - NOTES:
    - Weak entity


