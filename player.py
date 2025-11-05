class Player:
    def __init__(self, sanity,max_sanity, confidence, inventory):
        self.sanity = sanity          
        self.confidence = confidence  
        self.inventory = inventory
        self.max_sanity = max_sanity

    def is_dead(self):
        if self.sanity > 1:
            return False
        else:
            return True
        
    def adjust_sanity(self, amount):
        self.sanity = max(0, min(self.max_sanity, self.sanity + amount))
        if self.sanity == 0:
            print("You’ve lost your mind completely...")
        elif self.sanity < 30:
            print("Your head feels dizzy. The world distorts slightly.")

    def adjust_max_sanity(self,amount):
        self.max_sanity += amount
        print("You've increased your maximum sanity by " +str(amount)+" to "+str(self.max_sanity))
    
    def adjust_confidence(self, amount):
        self.confidence += amount
        reduction = self.confidence/(self.confidence+100)
        reduction_percent = round(reduction * 100, 1)
        print(f"Your confidence is now {self.confidence}.")
        print(f"Resulting in a damage reduction of: {reduction_percent}%")
        
    def show_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("🧳 Inventory:")
        for item, qty in self.inventory.items():
            print(f" - {item}: {qty}")
    