from place import Place
from player import Player
from person import *
from time import sleep 
from fight import *

class Game():
    def __init__(self):
        self.current_place = None
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # places
        bedroom = Place('Bedroom')

        global dining
        dining = Place('Dining Room', True)

        attic = Place('Attic')
    
        global basement
        basement = Place('Basement',True)

        kitchen = Place('Kitchen')
        office = Place('Office')
        living = Place('Living Room')
        garden = Place('Garden') 
        entrance = Place('Entrance')

        global frontYard
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
        basement.add_next_place(living)
        office.add_next_place(bedroom)
        entrance.add_next_place(attic)
        attic.add_next_place(bedroom)
        
        self.current_place =  bedroom
        # etc. 
        
        # items & people
        wallet = thing('wallet',4,'thing')
        
        global key
        key = thing('Key',2,'tool')

        bedroom.add_item(wallet)
        bedroom.add_item(key)
        
        puzzle = thing('Puzzle',7,'puzzle')
        water = thing('Water',5,'food')
        dining.add_item(puzzle)
        dining.add_item(water)

        crowbar = thing('Crowbar',9,'weapon')

        global doorknob
        doorknob = thing('Doorknob',4,'tool')

        attic.add_item(crowbar)
        attic.add_item(doorknob)

        framedMap = thing('Framed Map',3,'thing')
        chocolate = thing('Chocolate',2,'food')
        basement.add_item(chocolate)
        basement.add_item(framedMap)

        diary = thing('Diary',6,'book')
        bandages = thing('Bandages',2,'medicine')
        class chef(person):
            def talk(self):
                print("Chef: It would be best if you went back to bed immediately.")

        global c
        c = chef('Chef','Colin')
        kitchen.add_item(diary)
        kitchen.add_item(bandages)
        kitchen.add_person(c)

        apple = thing('Apple',1,'food')
        gun = thing('Gun,',8,'weapon')
        office.add_item(apple)
        office.add_item(gun)
        
        childBook = thing("Child's Book",4,'thing')
        phone = thing('Phone',8,'broken')
        candle = thing('Candle',2,'thing')
        class maid(person):
            def talk(self):
                print('''           
                      *Panicked look* 

        Maid:   Please stay away from the front door it really isn't safe!
                You may find more interesting information upstairs in the attic.
                      ''')
        global m
        m = maid('Maid','Agnes')
        living.add_item(childBook)
        living.add_item(phone)
        living.add_item(candle)
        living.add_person(m)

        litterBox = thing('Litter Box',6,'thing')
        hammer = thing('Hammer',10,'weapon')
        shovel = thing('Shovel',12,'weapon')
        class butler(person):
            def talk(self):
                print(''' 
        Butler: There is no straightforward path to leaving this house.
                Perhaps more success would be found downstairs.
                      ''')
        global b 
        b = butler('Butler','Geoffrey')
        garden.add_item(hammer)
        garden.add_person(b)
        garden.add_item(shovel)

        class driver(person):
            def talk(self):
                print('''
        'My Kidnapper's personal driver appears to be lurking in the corner.'
                      
         Driver: *Stands silently and ominously*
                      ''')
        global d
        d = driver('Driver','Richard')
        hat = thing('Hat',2,'thing')
        entrance.add_person(d)
        entrance.add_item(litterBox)
        entrance.add_item(hat)

            
        # finish the setup function..

    def start(self):
        play_game = True
        print('''


 _     _  _______  ___      _______  _______  __   __  _______ 
| | _ | ||    ___||   |    |      _||   _   ||  |_|  ||    ___|
| || || ||   |___ |   |    |     |  |  | |  ||       ||   |___
|       ||    ___||   |    |     |  |  | |  ||       ||    ___| 
|   _   ||   |___ |   |___ |     |_ |  |_|  || ||_|| ||   |___
|__| |__||_______||_______||_______||_______||_|   |_||_______|


 
''')
        name = input("Enter player name: ")
        player = Player(name,12,30)

        sleep(2)
        
        print('''You awaken with a sudden gasp, your body stiff and disoriented. As your eyes flutter open, 
              the oppressive weight of your fear clings to you like a suffocating blanket. 
              You're not in your bed. This isn't your home.

              In fact, you can't remember how you got here.
''')
        sleep(6)
        

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
        while play_game == True:
            print("You find yourself within the " + self.current_place.name)
            player.add_places_been(self.current_place)
            if self.current_place.name == 'Basement':
                count = player.places_been.count('Basement')
                if count == 1:
                    print('''
                      You look at the rotting basement door and realise.
                      There's only one safe way out - down.
                      
                      There is a small window on the back wall. It's a tight squeeze... but its the easiest way out.
                     
                      
                       ''')
                sleep(1)
                while True:
                    option = input('''
                                1. Would you like to run away or...
                                2. Would you like to fight and get revenge...
                                ''')
                    if option == '1':
                        sleep (2)
                        print('''


    You don't look back. You just run, the world ahead of you, and freedom finally within your reach...
                ''')
                        sleep(2)
                        print(''' 
    .------..------..------..------.     .------..------..------..------.
    |G.--. ||A.--. ||M.--. ||E.--. |.-.  |O.--. ||V.--. ||E.--. ||R.--. |
    | :/\: || (\/) || (\/) || (\/) ((5)) | :/\: || :(): || (\/) || :(): |
    | :\/: || :\/: || :\/: || :\/: |'-.-.| :\/: || ()() || :\/: || ()() |
    | '--'G|| '--'A|| '--'M|| '--'E| ((1)) '--'O|| '--'V|| '--'E|| '--'R|
    `------'`------'`------'`------'  '-'`------'`------'`------'`------'
    ''')    
                        play_game = False
                        break
                    elif option == '2':
                        print("Good choice...")
                        break
                    else:
                        print("Invalid input. Try again")
                        continue
                
            if self.current_place.name == 'Front Yard':
                            w = 0
                            for i in player.inventory:
                                if i.type == 'weapon':
                                    w = w + 1
                            if w > 0:
                                H = Boss('Husband Richard',100,15,25)
                                boss_fight(player,H)
                                play_game = False
                            else:
                                print('You need a weapon to beat your husband and finally escape. You lose!')
                                print('''
.------..------..------..------.     .------..------..------..------.
|G.--. ||A.--. ||M.--. ||E.--. |.-.  |O.--. ||V.--. ||E.--. ||R.--. |
| :/\: || (\/) || (\/) || (\/) ((5)) | :/\: || :(): || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: |'-.-.| :\/: || ()() || :\/: || ()() |
| '--'G|| '--'A|| '--'M|| '--'E| ((1)) '--'O|| '--'V|| '--'E|| '--'R|
`------'`------'`------'`------'  '-'`------'`------'`------'`------'
                                          ''')
                                sleep(1)
                                print('''
                                
                                      
                                      Your body was buried in a ditch not too far away. No one ever found you.
                                      ''')
                                play_game = False
                                break
            opt = input(f'''
    What will you do, Dear {player.name}
    1. Venture in to another hall
    2. Claim an artifact
    3. Inspect your belongings
    4. Converse with someone
        
    ''')
            if opt == "1":
                self.current_place.show_next_places()
                opt2 = input("Which room would you like to enter? ")
                if len(self.current_place.next_places) == 1:
                    if self.current_place.next_places[int(opt2)-1].locked == True:
                        print(f'The door to this chamber has been sealed. Choose another option, Dear {player.name}')
                        continue
                    
                    else:
                        self.current_place =self.current_place.next_places[0]

                    
                elif len(self.current_place.next_places) == 2:
                    if self.current_place.next_places[int(opt2)-1].locked == True:
                        print("This chamber cannot be accessed.")
                        if self.current_place.next_places[int(opt2)-1].name == 'Dining Room':
                            print("You need to find the Doorknob for this room.")
                        elif self.current_place.next_places[int(opt2)-1].name == 'Basement':
                            print('''You need to find the code for the keypad to this room.
                                        Perhaps you should look in the dining room.''')
                        elif self.current_place.next_places[int(opt2)-1].name == 'Front Yard':
                            print("You need to find the key to unlock this door.")
                                
                        if opt2 == '1':
                            self.current_place =self.current_place.next_places[1]
                        elif opt2 == '2':
                            self.current_place =self.current_place.next_places[0]

                        print(f'You cannot access that room so you must go to the {self.current_place.name}')

                    else: 
                        if opt2 == '1':
                            self.current_place = self.current_place.next_places[0]
                        elif opt2 == '2':
                            self.current_place = self.current_place.next_places[1]
                
                elif len(self.current_place.next_places) == 3:
                    while True:
                        if self.current_place.next_places[int(opt2)-1].locked == True:
                            print("This chamber cannot be accessed.")
                            if self.current_place.next_places[int(opt2)-1].name == 'Dining Room':
                                print("You need to find the Doorknob for this room.")
                            elif self.current_place.next_places[int(opt2)-1].name == 'Basement':
                                print('''You need to find the code for the keypad to this room.
                                            Perhaps you should look in the dining room.''') 
                            elif self.current_place.next_places[int(opt2)-1].name == 'Front Yard':
                                print("You need to find the key to unlock this door.")

                        opt3 = input("Please choose a different room you would like to enter? ")
                        self.current_place.show_next_places()
                        if self.current_place.next_places[int(opt3)-1].locked == False:
                            if opt3 == '1':
                                self.current_place = self.current_place.next_places[0]
                            elif opt3 == '2':
                                self.current_place = self.current_place.next_places[1]
                            elif opt3 == '3':
                                self.current_place = self.current_place.next_places[2]
                            break
                        else:
                            print('This room is locked, pick another.')
                            continue
                  

            elif opt == "2":
                self.current_place.show_items()
                Q1 = input("Which artifact would you like to claim? ")
                if self.current_place.items[int(Q1)-1].name == 'Puzzle':
                    P = MGame()
                    P.play_game()
                    print("You have unlocked a secret item!")
                    note = thing('Code',1,'thing')
                    player.add_item(note)
                    print("You now have the code for the basement! It has been unlocked.")
                    basement.locked = False

                elif self.current_place.items[int(Q1)-1].name == 'Doorknob':
                    print("You have obtained the doorknob for the dining room! It has been unlocked.")
                    dining.locked = False
                    
                elif self.current_place.items[int(Q1)-1].name == 'Key':
                    player.add_item(key)
                    print("You have obtained the key for the front door! The Front Yard has been unlocked.")
                    frontYard.locked = False  
                else:

                    player.add_item(self.current_place.items[int(Q1)-1])
                    self.current_place.items.remove(self.current_place.items[int(Q1)-1])
                    if player.inventory_full == True:
                        Q2 = input("Would you like to remove an item from your inventory? Y/N").upper()
                        if Q2 == "Y":
                            player.show_inventory()
                            Q3 = input("What would you like to remove? ")
                            while True:
                                if Q3.isdigit():
                                    player.inventory.remove[player.inventory[int(Q3)-1]]
                                    break
                                else:
                                    print("Invalid input. Try again.")
                                    continue

                        elif Q2 == 'N':
                            pass
                        else:
                            print("Invalid input. Try again.")


            elif opt == "3":
                player.calculate_inventory_size()
                player.check_inventory()
                pass
            elif opt == '4':
                if self.current_place.name == 'Kitchen':
                    c.talk()
                    player.talk(self.current_place)
                    if player.fight == True:
                        chef = Boss("Chef",75,8,20)
                        boss_fight(player,chef)
                        if player.alive == False:
                            play_game = False
                elif self.current_place.name == 'Living Room':
                    m.talk()
                    player.talk(self.current_place)
                elif self.current_place.name == 'Garden':
                    b.talk()
                    player.talk(self.current_place)
                elif self.current_place.name == 'Entrance':
                    d.talk()
                    player.talk(self.current_place)
                else:
                    print('There is no one in this room to converse with.')
                    continue
            
game = Game()
game.setup()
game.start()
