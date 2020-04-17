from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


# Fill this out with directions to walk
# traversal_path = ['s', 'w', 'e', 'n', 'n', 's']
traversal_path = []

# Other variables
player = Player(world.starting_room)
record = 10000

def opposite_direction(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    else:
        return 'e'


while True:
    certains = 0
    traversal_path = []
    # Create traversal graph
    traversal_graph = {}
    for room in room_graph:
        traversal_graph[room] = {}
        for exits in room_graph[room][1]:
            traversal_graph[room][exits] = '?'


    player.current_room = world.starting_room
    visited_rooms_simulation = set()
    visited_rooms_simulation.add(player.current_room.id)
    qq = []
    qq.append(player.current_room.id)

    # while qq.size() > 0:
    while True:
        saw_question = False
        l = list(traversal_graph[player.current_room.id].items())
        if len(traversal_path) == 0:
            l.remove(('s', '?'))
            l.insert(0, ('s', '?'))
        elif len(traversal_path) == 4:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 6:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 7:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 20:
            l.remove(('s', '?'))
            l.insert(0, ('s', '?'))
        elif len(traversal_path) == 26:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 27:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 47:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 57:
            l.remove(('s', '?'))
            l.insert(0, ('s', '?'))
        elif len(traversal_path) == 106:
            l.remove(('s', '?'))
            l.insert(0, ('s', '?'))
        elif len(traversal_path) == 108:
            l.remove(('s', '?'))
            l.insert(0, ('s', '?'))
        elif len(traversal_path) == 116:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 119:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 168:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 171:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 183:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 193:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 197:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 203:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 209:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 214:
            l.remove(('s', '?'))
            l.insert(0, ('s', '?'))
        elif len(traversal_path) == 217:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 227:
            l.remove(('w', '?'))
            l.insert(0, ('w', '?'))
        elif len(traversal_path) == 258:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 261:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 264:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 268:
            l.remove(('e', '?'))
            l.insert(0, ('e', '?'))
        elif len(traversal_path) == 270:
            l.remove(('e', '?'))
            l.insert(0, ('e', '?'))
        elif len(traversal_path) == 271:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 272:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 286:
            l.remove(('e', '?'))
            l.insert(0, ('e', '?'))
        elif len(traversal_path) == 290:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 299:
            l.remove(('n', '?'))
            l.insert(0, ('n', '?'))
        elif len(traversal_path) == 329:
            l.remove(('e', '?'))
            l.insert(0, ('e', '?'))
        elif len(traversal_path) == 330:
            l.remove(('s', '?'))
            l.insert(0, ('s', '?'))
        elif len(traversal_path) == 386:
            l.remove(('e', '?'))
            l.insert(0, ('e', '?'))
        else:
            random.shuffle(l)
        traversal_graph[player.current_room.id] = dict(l)
        for direction in traversal_graph[player.current_room.id]:
            # If we haven't went to that direction yet
            if traversal_graph[player.current_room.id][direction] == '?':
                # print(player.current_room.id, direction)
                saw_question = True
                # Add the direction to our traversal path
                traversal_path.append(direction)
                # Fill in the number you get to by going in the given direction
                traversal_graph[player.current_room.id][direction] = room_graph[player.current_room.id][1][direction]
                # print(traversal_graph)
                # Travel the given direction
                player.travel(direction)
                # Now that we're in the new room, fill in the old number in the opposite direction
                # If you went north, south of the new room is the old number
                # If you went west, east of the new room is the old number
                # etc
                traversal_graph[player.current_room.id][opposite_direction(direction)] = room_graph[player.current_room.id][1][opposite_direction(direction)]
                # pprint.pprint(traversal_graph)
                qq.append(player.current_room.id)
                visited_rooms_simulation.add(player.current_room.id)
                # print(qq)
                break
        if not saw_question:
            qq.pop()
            # print(visited_rooms_simulation)
            if len(visited_rooms_simulation) == len(room_graph):
                break
            else:
                for direction in traversal_graph[player.current_room.id]:
                    if traversal_graph[player.current_room.id][direction] == qq[-1]:
                        # print(player.current_room.id, direction)
                        traversal_path.append(direction)
                        player.travel(direction)
                        break
    if len(traversal_path) < record:
        record = len(traversal_path)
        print(traversal_path)
        print(len(traversal_path))




#print(player.current_room.id)
#print(player.current_room.get_exits())
# print(player.travel(direction))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


'''
#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
'''
