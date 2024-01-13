import random

class Laberinto:
    def __init__(self, size=10):
        self.size = size
        self.mines=[]
        self.lab = [[' ' for i in range(size)] for j in range(size)]
        self.pos_jugador = (0, 0)
        self.pos_salida = (size-1, size-1)
        self.generar_lab()


    def generar_lab(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < 0.3:
                    a,b = i,j
                    self.lab[i][j] = '#'


        self.lab[0][0] = 'Y'

        while self.lab[self.pos_salida[0]][self.pos_salida[1]] == '#':
            self.pos_salida = (random.randint(0, self.size-1), random.randint(0, self.size-1))

        self.lab[self.pos_salida[0]][self.pos_salida[1]] = 'E'

    def __str__(self):
        lab_str = ''
        for i in range(self.size):
            for j in range(self.size):
                lab_str += self.lab[i][j] + ' '
            lab_str += '\n'
        return lab_str

    def mover_jugador(self, direccion):
        nueva_pos = self.pos_jugador
        if direccion == 'u':
            nueva_pos = (self.pos_jugador[0] - 1, self.pos_jugador[1])
        elif direccion == 'd':
            nueva_pos = (self.pos_jugador[0] + 1, self.pos_jugador[1])
        elif direccion == 'l':
            nueva_pos = (self.pos_jugador[0], self.pos_jugador[1] - 1)
        elif direccion == 'r':
            nueva_pos = (self.pos_jugador[0], self.pos_jugador[1] + 1)


        if nueva_pos[0] >= 0 and nueva_pos[0] < self.size and nueva_pos[1] >= 0 and nueva_pos[1] < self.size:
            if self.lab[nueva_pos[0]][nueva_pos[1]] == '#':
                print("Obstáculo. ¡Fin del juego!")
                return True

            else:
                self.lab[self.pos_jugador[0]][self.pos_jugador[1]] = ' '
                self.pos_jugador = nueva_pos
                self.lab[self.pos_jugador[0]][self.pos_jugador[1]] = 'Y'
                if self.pos_jugador == self.pos_salida:
                    print(lab)
                    print("¡Victoria!")
                    return True
        return False

lab = Laberinto()

print("Bienvenido al Laberinto. Encuentra la salida (E).")

while True:
    print(lab)
    direccion = input("Introduce una dirección (arriba(u), abajo(d), izquierda(l), derecha(r)): ")
    #if lab.mover_jugador(direccion) == False:
    #    break
    if lab.mover_jugador(direccion):
        break