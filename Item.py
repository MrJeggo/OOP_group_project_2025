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

pencil = Weapon("unsharpend pencil","you dealt 10 damage not great not terrible",10,[],[])


sharpend_pencil = Weapon("pencil","you dealt 15 damage better than 10",15,[],[])


pencil_sharperner = Miscellaneous("pencil sharperner","everyone knows what a pencil sharperner does")


popcorn = Consumable("pocorn kernal","you ate the kernal you gain 5 health",5)


apple = Consumable("apple","an apple a day just gave you 50 health",50)
