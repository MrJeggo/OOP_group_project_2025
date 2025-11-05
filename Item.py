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


