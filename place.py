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
        print("The possible places you can go to are: ")
        for place in self.next_places:
            for i in len(self.next_places):
                print(f'{i+1}". " {place.name}')

    # add more methods as needed
