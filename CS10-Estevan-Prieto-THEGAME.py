import sys 

node = None
class Room:
    def __init__(self, name, description, n_path, e_path, s_path, w_path):
        '''Etner in the room name, room description, and rooms you can access from directions as follows: north, east, south, west
        '''
        self.name = name
        self.description = description
        self.north = n_path
        self.east = e_path
        self.south = s_path
        self.west = w_path
        
    def move (self, direction):
        if direction in ['q', 'quit', 'exit']:
            sys.exit(0)
        while True:
            global node
            node = globals()[getattr(self,direction)]
            break



while True:
    
    print node.name
    print node.description
    command = raw_input('> ')
    if command in ['north','south','east','west']:
        try:
            node.move(command)
        except:
            print 'You can\'t go that way.'

    

        