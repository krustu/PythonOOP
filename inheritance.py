
class Tier1:
    def __init__(self, name):
        self.name = name

class King(Tier1):
    pass
King = King("Rysbek")
print(King.name)