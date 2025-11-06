class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, attack_power, effective_against=None, ineffective_against=None):
        super().__init__(name, description)
        self.attack_power = attack_power
        self.effective_against = effective_against or []  
        self.ineffective_against = ineffective_against or [] 


class Consumable(Item):
    def __init__(self, name, description, heal_amount):
        super().__init__(name, description)
        self.heal_amount = heal_amount


class Miscellaneous(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

# here be items matey

# weapons stored here
# Please add the effective against and ineffective against when you are adding the bosses

pencil = Weapon("unsharpend pencil","you dealt 10 damage not great not terrible",10,[],[])

calculator = Weapon("scientific calculator","you subtraced 13 health from your foes",13,[],[])

bettercalculator=Weapon("Graphic calculator","you subtracted 10*2 health",20,[],[])

sharpend_pencil = Weapon("pencil","you dealt 15 damage better than 10",15,[],[])

# miscellaneous items

pencil_sharperner = Miscellaneous("pencil sharperner","everyone knows what a pencil sharperner does")

# keys 



# consumables

popcorn = Consumable("pocorn kernal","you ate the kernal you gain 5 health",5)

milk = Consumable("Milk","you drank the milk you gain 20 health")

apple = Consumable("apple","an apple a day just gave you 50 health",50)
