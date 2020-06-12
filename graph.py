"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of rooms."""

    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        """
        Add a room to the graph.
        """
        # create a dict for the new room
        self.rooms[room.id] = {}
        # populate it with the room's exits per the map
        for r in room.get_exits():
            self.rooms[room.id][r] = '?'

    def add_hall(self, this_room, next_room, direction):
        """
        Add a non-directed edge to the graph.
        """
        reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        self.rooms[this_room.id][direction] = next_room.id
        self.rooms[next_room.id][reverse_direction[direction]] = this_room.id

    def get_neighbors(self, room):
        """
        Get all neighbors (edges) of a room.
        """
#        print("current room is: ", room)
        return self.rooms[room]

    def bfs(self, starting_room):
        """
        Return a list containing the shortest path from
        starting_room to other rooms in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_room])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last room from the PATH
            last_room = path[-1]
            # found an exit with a '?' as the value
            if last_room == "?":
                return path
            # If that vertex has not been visited...
            if last_room not in visited:
                # Mark it as visited...
                visited.add(last_room)
                # Then add A PATH TO its neighbors to the back of the queue
                for edge in self.get_neighbors(last_room).values():
                    # COPY THE PATH
                    path_copy = list(path)
                    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(edge)
                    q.enqueue(path_copy)
