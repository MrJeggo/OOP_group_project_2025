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

pencil = Weapon()
pencil.name = "unsharpend pencil"
pencil.description = "you dealt 10 damage not great not terrible"
pencil.effective_against = []
pencil.attack_power = 10
pencil.ineffective_against = []

sharpend_pencil = Weapon()
sharpend_pencil.name = "pencil"
sharpend_pencil.description = "you dealt 15 damage better than 10"
sharpend_pencil.effective_against = []
sharpend_pencil.attack_power = 15
sharpend_pencil.ineffective_against = []

pencil_sharperner = Miscellaneous()
pencil_sharperner.name = "pencil sharperner"
pencil_sharperner.description = "everyone knows what a pencil sharperner does"

popcorn = Consumable()
popcorn.name = "pocorn kernal"
popcorn.description = "you ate the kernal you gain 5 health"
popcorn.heal_amount = 1

apple = Consumable()
apple.name = "apple"
apple.description = "an apple a day just gave you 50 health"
apple.heal_amount = 50