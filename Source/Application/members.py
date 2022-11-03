

class Member:
    mid = ""
    name = ""
    
    def __init__(self, mid, name):
        self.mid = mid
        self.name = name
        return


class Artist(Member):
    nationality = ""
    def __init__(self, mid, name, nationality=None):
        super().__init__(mid, name)
        self.nationality = nationality
        return


class User(Member):
    def __init__(self, mid, name):
        super().__init__(mid, name)
        return
