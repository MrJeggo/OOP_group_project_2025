# from teachers import Teacher
# from player import item_list
from Game import Game 
from Item import Item

class Room():
    def __init__(self, room_num, is_lock, room_direction, teacher_inside, item_inside, room_descriptor, is_shop):
        self.room_num = room_num
        self.is_lock = is_lock
        self.room_direction = room_direction
        # self.teacher_inside = Teacher.teacher_inside
        self.item_inside = Item.item_inside
        self.room_description = room_direction
        self.is_shop = is_shop

    def which_teacher(self):
        pass
        return 
    
    def is_door_locked(self):
        # check if door is locked 
        # check item list of player and see if they can unlock 
        pass

    def dir_to_go(self):
        commands = []
        for dir in self.room_direction:
            print(f'''Room: {dir[0]}
What to enter to get there: {dir[1]}''')
            commands.append(dir[1])
        
        user_input = ''
        while user_input not in commands:
            user_input = input('Please input the direction you want to go: ')

        # make player current room the new room 

    def which_Teacher(self):
        pass

    def which_Item(self):
        pass

    def show_room(self):
        return self.room_description
    
    def is_it_shop(self):
        return self.is_shop
    
