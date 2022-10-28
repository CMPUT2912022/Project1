# Project1
Enterprise Database

## Running
```bash
# From .
cd Source
python3 main.py
```

## UI
![UI_Flowchart](https://github.com/CMPUT2912022/Project1/blob/main/Documentation/UI_Flowchart.svg)


## UML
![UML](https://github.com/CMPUT2912022/Project1/blob/main/Documentation/UML.svg)


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
    - Many-to-many relationship
- playlists(*pid*, title, *uid*)
  - PK: pid
- plinclude(*pid*, *sid*, sorder)
  - PK: pid, sid
  - FK: pid, sid
  - NOTES:
    - Many-to-many relationship
- artists(*aid*, name, nationality, pwd)
  - PK: aid
- perform(*aid*, *sid*)
  - PK: aid, sid
  - FK: aid, sid
  - NOTES:
    - Many-to-many relationship

## Design patterns
- Application logic should be seperate from the interface logic (have a class solely for managing the application logic).
- Each view should be in a seperate function/class
