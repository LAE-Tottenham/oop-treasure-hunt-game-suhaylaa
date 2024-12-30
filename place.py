class Place():
    def __init__(self, given_name, locked=False):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.locked = locked
        self.next_places = []
        self.items = []
        self.people =[]
        # add more atributes as needed

    def add_next_place(self,place):
        self.next_places.append(place)

    def add_item(self, item):
        self.items.append(item)
        
    def add_person(self,person):
        self.people.append(person)


    def show_next_places(self):
        print("The possible places open for exploring are: ")
        for i in range(0,len(self.next_places)):
            print(f'{i+1}. {self.next_places[i].name}')

    def show_items(self):
        print("The artifacts available within this space are: ")
        for i in range(0,len(self.items)):
            print(f'{i+1}.{self.items[i].name}')

    # add more methods as needed

b = Place('bedroom')
c = Place('c')
d = Place('d')
b.add_next_place(c)
b.add_next_place(d)
