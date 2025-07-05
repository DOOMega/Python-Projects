class Location():

    def __init__(self, name, description):

        self.name = name
        self.Description = description
        self.Connection = {}

class Map():

    def __init__(self):

        self.Locations = {}
        self.Current_location = None
        


game_map = Map()
Forest = Location("Forest", "A dense forest.")
Cave = Location("Cave", "A dark cave with stalactites.")
Lair = Location("Lair", "A mysterious and dangerous dungeon.")

Forest.Connection = {"Forest": Forest}
Cave.Connection = {"Cave": Cave}
Lair.Connection = {"Lair": Lair}

game_map.Locations = {"Forest": Forest, "Cave": Cave, "Lair": Lair}
game_map.Current_location = Forest
