# from teachers import Teacher
# from player import item_list
from Game import Game 
from Item import Item
from player import Player

class Room():
    def __init__(self, room_num, is_lock, key, room_direction, teacher_inside, item_inside, is_shop, shop_items):
        self.room_num = room_num
        self.is_lock = is_lock
        self.key = key
        self.room_direction = room_direction
        self.teacher_inside = Game.teacher[teacher_inside]
        self.item_inside = Game.item[item_inside]
        # self.room_description = room_descriptor
        self.is_shop = is_shop
        self.shop_items = shop_items

    def which_teacher(self):
        return self.teacher_inside.getName()
    
    def is_door_locked(self):
        # check if door is locked 
        # check item list of player and see if they can unlock 
        if self.is_lock:
            if self.key in Player.inventory:
                self.is_lock = False
                return "You have the key to unlock the door."
            else:
                return "Door is locked, you do not have the item to unlock the door."
        else:
            return f"Door opened. You have entered {self.room_num}"

    def dir_to_go(self):
        commands = [] # [["Physics", 'w'], ["Nurse", 'd']]
        for dir in self.room_direction:
            print(f'''Room: {dir[0]}
What to enter to get there: {dir[1]}''')
            commands.append(dir[1])
        
        user_input = ''
        while user_input not in commands:
            user_input = input('Please input the direction you want to go: ')
        
        ind = commands.index(user_input)
        return self.room_direction[ind][0]

        # make player current room the new room 
    def which_Item(self):
        return self.item_inside
    
    def is_it_shop(self):
        return self.is_shop

    def show_room(self):
        if self.is_shop == True:
            return f"This is the room {self.room_num} with {self.teacher_inside} standing inside. The room is a shop. "
        
    def selling_items(self):
        # [['Pencil', '30'], ['Calculator', '50']]
        #
        pass 
