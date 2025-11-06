import Player 
class teacher: 
    def __init__(self,name, maxhealth,attackdamage,subject):
        self._name = name
        self.health = maxhealth 
        self._maxhealth = maxhealth
        self.attackdamage = attackdamage
        self.subject = subject

    def heal(self):
        if self.health < self._maxhealth*0.9:
            self.health *= 1.1
            return f"The {self._name} has healthed by 10%"
        
    def resethealth(self):
        if Player.is_dead() == True: 
            Player self.health = self._maxhealth
  
    def getName(self):
        return self._name
    
    def getSubject(self):
        return self.subject
    
    # heeeee
    