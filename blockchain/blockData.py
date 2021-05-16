
# block data will be dependent on how we design the game
class BlockData:
    def __init__(self, id, name):
        # `id` will depend on game (change later)
        # `name` will depend on game (change later)
        self.id = id
        self.name = name

    def getTuple(self):
        # tuple should consist of the data that will affect the hash
        tup = (self.id, self.name)
        return tup