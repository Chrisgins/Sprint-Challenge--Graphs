from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
reverse_path=[]

# creating a fn that will return the reversed direction
def r_direction(dir):
    if dir == 'n':
        return 's':
    if dir == 's':
        return 'n':
    if dir == 'w':
        return 'e':
    if dir == 'e':
        return 'w':    
    else:
        return "invalid"   

# track visited room in a dictionary

rooms = {}

# first room has the lists of exits
rooms[player.curren_room.id] = player.current_room.get_exits()

# if len of rooms hit < num of rooms in the graph -first room
while len(room) < len(room_graph) -1:
    # if current room hasn't been visited
    if player.current_room.id not in rooms:
        # set the list of exits to room in visited dictionary
        rooms[player.current_room.id] = player.current_room.get_exits()
        # bread crumb the last room as visited
        l_room = reverse_path[-1]
        rooms[player.current_room.id].remove(l_room)
    # Hit a dead-end? Then remove the last path from reverse_path
    while len(rooms[player.current_room.id]) < 1:
        reverse = reverse_path.pop()
        # go back
        player.travel(reverse)
        # then add to the traversed path
        traversal_path.append(reverse)
    # handle unexplored rooms
    else:
        # select last exited 
        l_exit =rooms[player.current_room.id].pop()
        # add to traversed path
        traversal_path.append(l_exit)
        # put ya thing down, flip it and reverse it
        reverse_path.append(r_direction(l_exit))
        player.travel(l_exit)    










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
