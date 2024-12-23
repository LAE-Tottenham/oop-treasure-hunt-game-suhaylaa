from place import Place
from player import Player
from item import Item
from person import person
from time import sleep 

class Game():
    def __init__(self):
        self.current_place = None
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # places
        bedroom = Place('Bedroom')
        dining = Place('Dining Room', True)
        attic = Place('Attic')
        basement = Place('Basement',True)
        kitchen = Place('Kitchen')
        office = Place('Office')
        living = Place('Living Room')
        garden = Place('Garden') 
        entrance = Place('Entrance')
        frontYard = Place('Front Yard',True)
        
        

        bedroom.add_next_place(dining)
        bedroom.add_next_place(kitchen)
        kitchen.add_next_place(living)
        kitchen.add_next_place(office)
        living.add_next_place(attic)
        living.add_next_place(garden)
        attic.add_next_place(dining)
        dining.add_next_place(basement)
        garden.add_next_place(basement)
        dining.add_next_place(garden)
        garden.add_next_place(entrance)
        entrance.add_next_place(frontYard)
        
        self.current_place =  bedroom
        # etc. 
        
        # items & people
        wallet = Item('Wallet',4,'thing')
        key = Item('Key',2,'tool')
        bedroom.add_item(wallet)
        bedroom.add_item(key)
        
        note = Item('Code',1,'thing')
        dining.add_item(note)

        crowbar = Item('Crowbar',9,'weapon')
        doorknob = Item('Doorknob',4,'tool')
        attic.add_item(crowbar)
        attic.add_item(doorknob)

        framedMap = Item('Framed Map',0,'thing')
        chocolate = Item('Chocolate',2,'food')
        basement.add_item(chocolate)
        basement.add_item(framedMap)

        diary = Item('Diary',0,'book')
        bandages = Item('Bandages',2,'medicine')
        class chef(person):
            def talk(self):
                print("It would be best if you went back to bed immediately.")
        c = chef('Chef','Colin')
        kitchen.add_item(diary)
        kitchen.add_item(bandages)
        kitchen.add_person(c)

        apple = Item('Apple',1,'food')
        gun = Item = ('Gun,',8,'weapon')
        office.add_item(apple)
        office.add_item(gun)
        
        childBook = Item("Child's Book",0,'thing')
        phone = Item('Phone',0,'broken')
        candle = Item('Candle',0,'thing')
        class maid(person):
            def talk(self):
                print('''           *Panicked look* 
        Please stay away from the front door it really isn't safe!
        You may find more interesting information upstairs in the attic.''')
        m = maid('Maid','Agnes')
        living.add_item(childBook)
        living.add_item(phone)
        living.add_item(candle)
        living.add_person(m)

        litterBox = Item('Litter Box',0,'thing')
        hammer = Item('Hammer',10,'weapon')
        class butler(person):
            def talk(self):
                print(''' There is no starightforward path to leaving this house.
        Perhaps more success would be found downstairs.''')
        b = butler('Butler','Geoffrey')
        garden.add_item(litterBox)
        garden.add_item(hammer)
        garden.add_person(b)

        class driver(person):
            def talk(self):
                print(' *Stands silently and ominously* ')
        d = driver('Driver','Richard')
        entrance.add_person(d)


        # finish the setup function..

    def start(self):
        print('''


 _     _  _______  ___      _______  _______  __   __  _______ 
| | _ | ||    ___||   |    |      _||   _   ||  |_|  ||    ___|
| || || ||   |___ |   |    |     |  |  | |  ||       ||   |___
|       ||    ___||   |    |     |  |  | |  ||       ||    ___| 
|   _   ||   |___ |   |___ |     |_ |  |_|  || ||_|| ||   |___
|__| |__||_______||_______||_______||_______||_|   |_||_______|


 
''')
        name = input("Enter player name: ")
        player = Player(name)
        print('''
              
              
              
              
              
              
              
              
              ''')
        sleep(2)
        
        print('''You awaken with a sudden gasp, your body stiff and disoriented. As your eyes flutter open, 
              the oppressive weight of your fear clings to you like a suffocating blanket. 
              You're not in your bed. This isn't your home.

              In fact, you can't remember how you got here.
''')
        sleep(2)
        

        print('''
              


                ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░   
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                ░▒▓███████▓▒░░▒▓████████▓▒░░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                                       
                                                                                       
                                                                                                          ''')

        sleep(2)
       
        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        opt = input("""
What would you like to do?
1. Move in to a different room
2. Pickup item
3. Check inventory
etc.      
""")
        if opt == "1":
            opt2 = input("Which room would you like to enter? ")
            self.current_place.show_next_places()
            if self.current_place.next_places[0].locked == True or self.current_place.next_places[1].locked == True:
                print("This room is currently locked")
                if self.current_place.next_places[0].name == 'Dining Room' or self.current_place.next_places[1].name == 'Dining Room':
                    print("You need to find the Doorknob for this room.")
                elif self.current_place.next_places[0].name == 'Basement' or self.current_place.next_places[1].name == 'Basement':
                    print('''You need to find the code for the keypad to this room.
                             Perhaps you should look in the dining room.''')
                elif self.current_place.next_places[0].name == 'Front Yard' or self.current_place.next_places[1].name == 'Front Yard':
                    print("You need to find the key to unlock this door.")

            if self.current_place.next_places[0].locked == True:
                self.current_place = self.current_place.next_places[1]
            elif self.current_place.next_places[1].locked == True:
                self.current_place = self.current_place.next_places[0]
                
            if opt2 == 1:
                self.current_place = self.current_place.next_places[0]
            elif opt2 == 2:
                self.current_place = self.current_place.next_places[1]


               

        elif opt == "2":
            # add code
            pass
        elif opt == "3":
            # add code
            pass
            
game = Game()
game.setup()
game.start()
