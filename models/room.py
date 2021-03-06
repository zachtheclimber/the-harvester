from models.npc import NPC


class Room():
    def __init__(self, name=None, description=None):
        self._name = name
        self._description = description
        self._occupants = []
        self.linked_rooms = {}

    def get_name(self):
        return self._name

    def set_name(self, room_name):
        self._name = room_name

    def get_description(self):
        return self._description

    def set_description(self, room_description):
        self._description = room_description

    def set_occupant(self, occupant: NPC):
        self._occupants.append(occupant)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(f"You are in the {self._name}.")
        print(f"You see: {self._description}")
        self.print_occupants()
        self.print_doors()

    def describe(self):
        print(self.get_description())

    def print_occupants(self):
        for occupant in self._occupants:
            occupant.describe()

    def print_doors(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room} is {direction}.")
