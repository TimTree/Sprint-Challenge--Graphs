from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Queue, Stack
import pprint

def opposite_direction(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    else:
        return 'e'


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

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
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
