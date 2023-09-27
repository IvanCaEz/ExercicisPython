class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Pawn:
    def __init__(self, name, movement, icon, alive, position: Position):
        self.name = name
        self.movement = movement
        self.icon = icon
        self.alive = alive
        self.position = position
        
    def __str__(self):
        return self.icon
        
    def can_move(self, _from: Position, to: Position) -> bool:
        return to.y in list(_from.y, _from.y+self.movement)
    
    def move(self, to: Position):
        self.position = to
        
    def eliminated(self):
        self.alive = False

