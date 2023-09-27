# 5- Dissenya el taulell d'escacs

class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

class Piece(object):
    def __init__(self,color, alive):
        self.color = color
        self.alive = alive
        
    def __str__(self):
        pass
        
    def can_move(self, _from: Position, to: Position, tablero) -> bool:
        pass
            
    def check_collision(self, _from: Position, to: Position, tablero):
        vertical = abs(_from.x - to.x)
        horizontal = abs(_from.y - to.y)
        if vertical == 0 or horizontal == 0:
            for i in range(min(_from.x, to.x), max(_from.x, to.x) + 1):
                for j in range(min(_from.y, to.y), max(_from.y, to.y) + 1):
                    if i == _from.x and j == _from.y:
                        continue  # Evita verificar la posición de origen de la pieza
                    if isinstance(tablero[i][j], Piece):
                        if tablero[i][j].color == self.color:
                            print("Colisión con tu equipo")
                            return True
                        else:
                            print("Colisión con pieza enemiga")
            return False
        elif vertical == horizontal:
            step_vertical = 1 if vertical > 0 else -1
            step_horizontal = 1 if horizontal > 0 else -1
            x, y = _from.x + step_vertical, _from.y + step_horizontal
            while x != to.x and y != to.y:
                target_piece = tablero[x][y]
                # Verificar si hay una pieza en la casilla actual
                if isinstance(target_piece, Piece):
                    # Verificar si la pieza es aliada
                    if target_piece.color == self.color:
                        # Si es una pieza aliada en el camino, retorna True
                        x += step_vertical
                        y += step_horizontal
                        print("Colisión con tu equipo")
                        return True
                    elif target_piece.color != self.color:
                        print("Colisión con pieza enemiga")
                x += step_vertical
                y += step_horizontal
    
    def eliminated(self):
        self.alive = False

class Pawn(Piece):
    def __init__(self,color, first_move, alive):
        self.color = color
        self.first_move = first_move
        self.alive = alive
        
    def __str__(self):
        return "♟" if self.color == "blancas" else "♙"
    
    def can_capture(self, _from: Position, to: Position, tablero):
        vertical = abs(_from.x - to.x)
        horizontal = abs(_from.y - to.y)
        if vertical == horizontal:
            step_vertical = 1 if vertical > 0 else -1
            step_horizontal = 1 if horizontal > 0 else -1
            x, y = _from.x + step_vertical, _from.y + step_horizontal
            while x != to.x and y != to.y:
                print(x, y)
                target_piece = tablero[x][y]
                print(str(target_piece))
                # Verificar si hay una pieza en la casilla actual
                if isinstance(target_piece, Piece):
                    # Verificar si la pieza es aliada
                    if target_piece.color == self.color:
                        # Si es una pieza aliada en el camino, retorna False
                        x += step_vertical
                        y += step_horizontal
                        print("Colisión con tu equipo")
                        return False
                    elif target_piece.color != self.color:
                        print("Colisión con pieza enemiga")
                        return True
                x += step_vertical
                y += step_horizontal
        
    def can_move(self, _from: Position, to: Position, tablero) -> bool:
        vertical = abs(_from.x - to.x)
        horizontal = abs(_from.y - to.y)
        if (self.first_move and vertical == 2) or (self.first_move and vertical == 1):
            return vertical == 2 or vertical == 1
        elif vertical == horizontal:
            return self.can_capture(_from, to, tablero)
        else: return vertical == 1
        

    def check_collision(self, _from: Position, to: Position, tablero):
        return super().check_collision(_from, to, tablero)
    
    def actu_first_move(self):
        self.first_move = False
    
    def eliminated(self):
        self.alive = False

class Tower(Piece):
    def __init__(self,color):
        self.color = color
        
    def __str__(self):
        return "♜" if self.color == "blancas" else "♖"
        
    def can_move(self, _from: Position, to: Position, tablero) -> bool:
        vertical = abs(_from.x - to.x)
        horizontal = abs(_from.y - to.y)
        # Si delta_row es 0 se mueve verticalmente, si delta_col es 0 se mueve horizontal y si son iguales, diagonalmente
        return vertical == 0 or horizontal == 0
    
    def check_collision(self, _from: Position, to: Position, tablero):
        return super().check_collision(_from, to, tablero)
    
    def move(self, to: Position):
        self.position = to
        
    def eliminated(self):
        self.alive = False
        
class Horse(Piece):
    def __init__(self,color):
        self.color = color
        
    def __str__(self):
        return "♞" if self.color == "blancas" else "♘"
        
    def can_move(self, _from: Position, to: Position, tablero) -> bool:
        vertical = abs(_from.x - to.x)
        horizontal = abs(_from.y - to.y)
        # Caballo es una L: 2 en una direccion y 1 perpendicular a esa dirección
        return (vertical == 2 and horizontal == 1) or (vertical == 1 and horizontal == 2)
    
    def check_collision(self, _from: Position, to: Position, tablero):
        # Verificar si la posición de destino está ocupada por una pieza aliada
        destination_piece = tablero[to.x][to.y]
        if isinstance(destination_piece, Piece) and destination_piece.color == self.color:
            print("Colisión con pieza aliada en la casilla de destino")
            return True
        else: return False
    
    def move(self, to: Position):
        self.position = to
        
    def eliminated(self):
        self.alive = False
        
class King(Piece):
    def __init__(self,color):
        self.color = color
        
    def __str__(self):
        return "♛" if self.color == "blancas" else "♕"
        
    def can_move(self, _from: Position, to: Position, tablero) -> bool:
        return _from.y in list(range(to.y-1, to.y+2)) and _from.x in list(range(to.x-1, to.x+2))

    def check_collision(self, _from: Position, to: Position, tablero):
        return super().check_collision(_from, to, tablero)
    
    def move(self, to: Position):
        self.position = to
        
    def eliminated(self):
        self.alive = False

class Queen(Piece):
    def __init__(self,color):
        self.color = color
        
    def __str__(self):
        return "♚" if self.color == "blancas" else "♔"
        
    def can_move(self, _from: Position, to: Position, tablero) -> bool:
        vertical = abs(_from.x - to.x)
        horizontal = abs(_from.y - to.y)
        # Si vertical es 0 se mueve verticalmente, si horizontal es 0 se mueve horizontal y si son iguales, diagonalmente
        return horizontal == 0 or vertical == 0 or vertical == horizontal
    
    def check_collision(self, _from: Position, to: Position, tablero):
        return super().check_collision(_from, to, tablero)
        
    def eliminated(self):
        self.alive = False
        
class Bishop(Piece):
    def __init__(self,color):
        self.color = color
        
    def __str__(self):
        return "♝" if self.color == "blancas" else "♗"
        
    def can_move(self, _from: Position, to: Position, tablero) -> bool:
        vertical = abs(_from.x - to.x)
        horizontal = abs(_from.y - to.y)
        return horizontal == vertical
    
    def check_collision(self, _from: Position, to: Position, tablero):
        return super().check_collision(_from, to, tablero)
    
    def move(self, to: Position):
        self.position = to
        
    def eliminated(self):
        self.alive = False

def crear_tablero() -> list:
    tablero = []
    lista_lletres = ["A","B","C","D","E","F","G","H"," "]
    lista_num = ["1","2","3","4","5","6","7","8", " "]
    for i in range(9):
        tablero.append([])
        for j in range(8):
            if i == 8: tablero[i].append(lista_lletres[j])
            elif (i == 0 and j == 0) or (i == 0 and j == 7): tablero[i].append(Tower("negras"))
            elif (i == 0 and j == 1) or (i == 0 and j == 6): tablero[i].append(Horse("negras"))
            elif (i == 0 and j == 2) or (i == 0 and j == 5): tablero[i].append(Bishop("negras"))
            elif (i == 0 and j == 3): tablero[i].append(King("negras"))
            elif (i == 0 and j == 4): tablero[i].append(Queen("negras"))
            elif i==1: tablero[i].append(Pawn("negras", True, True))
            elif i == 6: tablero[i].append(Pawn("blancas", True, True))
            elif (i == 7 and j == 0) or (i == 7 and j == 7): tablero[i].append(Tower("blancas"))
            elif (i == 7 and j == 1) or (i == 7 and j == 6): tablero[i].append(Horse("blancas"))
            elif (i == 7 and j == 2) or (i == 7 and j == 5): tablero[i].append(Bishop("blancas"))
            elif (i == 7 and j == 3): tablero[i].append(King("blancas"))
            elif (i == 7 and j == 4): tablero[i].append(Queen("blancas"))
            elif (i+j)%2 == 0: tablero[i].append('■')
            else: tablero[i].append('□')
        tablero[i].append(lista_num[7-i])
        
    imprimir_tablero(tablero)
    return tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        fila_str = [str(item) for item in fila]
        print(" ".join(fila_str))
        
def comprobar_ficha(pieza) -> bool:
    return isinstance(pieza, (Piece))

def comprobar_color(pieza, turno_color) -> bool:
    return pieza.color == turno_color

def turno(tablero: list, ronda: int) -> list:
    tablero = tablero
    turno_color = ""
    if ronda % 2 == 0: 
        print("Ronda de las negras")
        turno_color = "negras"
    else: 
        print("Ronda de las blancas")
        turno_color = "blancas"
    
    origen = str(input("Escoge la pieza que quieras mover así a2: "))
    fila_origen, col_origen =  8 - int(origen[1]), ord(origen[0]) - ord('a')

    pieza = tablero[fila_origen][col_origen]
    
    # Comprueba que sea una ficha y su turno
    while not comprobar_ficha(pieza) or not comprobar_color(pieza, turno_color):
        if comprobar_ficha(pieza) == False:
            origen = str(input("No hay pieza en esa posición, escoge de nuevo: "))
        elif pieza.color != turno_color: 
            origen = str(input("No puedes escoger piezas de tu rival, escoge de nuevo: "))
        fila_origen, col_origen =  8 - int(origen[1]), ord(origen[0]) - ord('a')
        pieza = tablero[fila_origen][col_origen]
        
        
    destino = str(input("Escoge la posición a la que quieras mover la pieza: "))
    fila_destino, col_destino = 8 - int(destino[1]), ord(destino[0]) - ord('a')
        
    colision = pieza.check_collision(
        Position(fila_origen,col_origen),Position(fila_destino,col_destino), tablero)

    while not pieza.can_move(Position(
        fila_origen,col_origen),Position(fila_destino,col_destino), tablero) or colision == True :
        if colision == True:
            destino = str(input("Esa movimiento colisiona con tu equipo, escoge de nuevo: "))
            fila_destino, col_destino = 8 - int(destino[1]), ord(destino[0]) - ord('a')
            colision = pieza.check_collision(Position(
                fila_origen,col_origen),Position(fila_destino,col_destino), tablero)
        else: 
            destino = str(input("Esa pieza no puede realizar ese movimiento, escoge de nuevo: "))
            fila_destino, col_destino = 8 - int(destino[1]), ord(destino[0]) - ord('a')
    else:
        # Si la pieza era un Peón, se actualiza el first_move
        if isinstance(pieza, (Pawn)): pieza.actu_first_move()
        # Actualiza el destino con la ficha
        tablero[fila_destino][col_destino] = pieza
    # Pinta el fondo 
    if (fila_origen+col_origen) % 2 == 0: tablero[fila_origen][col_origen] = "■"
    else: tablero[fila_origen][col_origen] = "□"
    
    return tablero

def count_remaining_pieces(tablero, color):
    pieces = 0
    for i in range(9):
        for j in range(9):
            if isinstance(tablero[i][j], Piece) and tablero[i][j].color == color:
                pieces +=1
    return pieces

def __init__():
    partida = True
    ronda = 1
    negras = 16
    blancas = 16
    print(f"                  Negras: {negras}")
    tablero_inicial = crear_tablero()
    print(f"                  Blancas: {blancas}")
    turnoo = turno(tablero_inicial, ronda)
    ronda += 1
    while partida == True :
        print(f"                  Negras: {negras}")
        imprimir_tablero(turnoo)
        print(f"                  Blancas: {blancas}")
        turno(turnoo, ronda)
        ronda += 1
        negras = count_remaining_pieces(turnoo, "negras")
        blancas = count_remaining_pieces(turnoo, "blancas")
        if blancas == 0 or negras == 0: partida = False

__init__()

