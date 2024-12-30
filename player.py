class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.inventory_max_weight = 50
        self.inventory = []
        self.inventory_size = 0
        # add more atributes as needed

    def calculate_inventory_size(self):
        for i in self.inventory:
            self.inventory_size = self.inventory_size + i.weight

    def add_item(self, item):
        if (self.inventory_size + item.weight) <= self.inventory_max_weight:
            self.inventory.append(item)
        else:
            print("Your inventory is brimming; there is no space for more...")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 50

    def move(self,room):
        print(f'You have moved into the {room.name}.')

        # add more code here

    # add more methods as needed
