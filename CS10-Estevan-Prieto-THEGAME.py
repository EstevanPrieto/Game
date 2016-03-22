import sys 
#Sets up aspects of the rooms
node = None
class Room:
    def __init__(self, name, description, n_path, e_path, s_path, w_path):
        '''Enter in the room name, room description, and rooms you can access from directions as follows: north, east, south, west
        '''
        self.name = name
        self.description = description
        self.north = n_path
        self.east = e_path
        self.south = s_path
        self.west = w_path

#Makes you able to move to each room       
    def move (self, direction):
        while True:
            global node
            node = globals()[getattr(self,direction)]
            break

#Rooms in the game
start = Room('Camp Center', 'TBA', 'n_exit', 'lab', 's_exit', 'storage')
s_exit = Room('South Exit', 'TBA', 'start', None, 'mount', None)
lab = Room('Laboratory', 'TBA', None, 'e_exit', 'arm', 'start')
arm = Room('Armory', 'TBA', 'lab', None, None, None)
e_exit = Room('East Exit', 'TBA', None, 'forest', None, 'lab')
n_exit = Room('North Exit', 'TBA', 'highway', None, 'start', None)
storage = Room('Pantry', 'TBA', 'farm', 'start', None, 'w_exit')
farm = Room('Farm', 'TBA', None, None, 'storage', None) 
w_exit = Room('West Exit', 'TBA', None, 'storage', None, 'area_one')
mount = Room('Mountain Base', 'TBA', 's_exit', None, 'slope', None)
slope = Room('Slopes', 'TBA', 'mount', 'cliff', 'peak', None)
cliff = Room('Cliff', 'TBA', None, None, None, 'slope')
peak = Room('Peak', 'TBA', 'slope', 'e_peak', None, 'w_peak')
e_peak = Room('East Peak', 'TBA', None, None, None, 'peak')
w_peak = Room('West Peak', 'TBA', None, 'peak', None, None)

node = start #sets your location to the starting room in the game

#prints where you are and checks if you can move that way; prompts you for where to go or if you want to quit
while True:    
    print node.name
    print node.description
    command = raw_input('> ')
    if command in ['north','south','east','west']:
        try:
            node.move(command)
        except:
            print 'You can\'t go that way.'
    if command in ['q', 'quit', 'exit']:
        sys.exit(0)

    

        