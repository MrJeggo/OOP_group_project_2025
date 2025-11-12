from Item import Weapon 
from Item import Miscellaneous
from Item import Consumable
from teachers import Teacher

class Game:
    item = {"pencil": Weapon("unsharpend pencil","you dealt 10 damage not great not terrible",10,[],[]),
            "calculator": Weapon("scientific calculator","you subtraced 13 health from your foes",13,[],[]),
            "bettercalculator": Weapon("Graphic calculator","you subtracted 10*2 health",20,[],[]),
            "sharpend_pencil": Weapon("pencil","you dealt 15 damage better than 10",15,[],[]), 
            # miscellaneous items
            "pencil_sharperner": Miscellaneous("pencil sharperner","everyone knows what a pencil sharperner does"),
            # keys 
            # consumables
            "popcorn": Consumable("pocorn kernal","you ate the kernal you gain 5 health",5),
            "milk": Consumable("Milk","you drank the milk you gain 20 health",20),
            "apple": Consumable("apple","an apple a day just gave you 50 health",50)}
    
    teacher = {"Mr Autum": Teacher("Atum",60,10,"Physiks"),
               "Mrs Vegedable": Teacher("Vegedable",100,15,"Chinese"),
               "Mr L'Boo": Teacher("L'Boo",120, 20,"Buisness"),
               "Mr Darken": Teacher("Darken",300,20,"Pricipal"),
               "Mrs Chilly": Teacher("Chilly",500,25,"Math"),
               "Mr Jeygo": Teacher("Jaygo",600,30,"CS"),
              }
    room = {}
    def __init__(self, player):
        self.player = player      
        self.current_room = None            
        self.victory = False               
