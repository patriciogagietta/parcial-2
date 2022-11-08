class HeapMax():

    def __init__(self):
        self.vector = []
        self.tamanio = 0

    def agregar(self, dato, prioridad=1):
        self.vector.append([dato, prioridad])
        self.flotar(self.tamanio)
        self.tamanio += 1

    def buscar(self, buscado):
        for index, value in enumerate(self.vector):
            # print(buscado, value)
            if value[0][0].info == buscado:
                resultado = index
                return resultado

    def flotar(self, indice):
        padre = (indice - 1) // 2
        while (indice > 0 and self.vector[indice][1] > self.vector[padre][1]):
            self.vector[indice], self.vector[padre] = self.vector[padre], self.vector[indice]
            indice = padre
            padre = (indice - 1) // 2

    def hundir(self, indice=0):
        hijo_izq = (indice * 2) + 1
        control = True
        while (control and hijo_izq < self.tamanio):
            mayor = hijo_izq
            hijo_der = hijo_izq + 1
            if hijo_der < self.tamanio:
                if self.vector[hijo_der][1] > self.vector[hijo_izq][1]:
                    mayor = hijo_der

            if self.vector[indice][1] < self.vector[mayor][1]:
                self.vector[indice], self.vector[mayor] = self.vector[mayor], self.vector[indice]
                indice = mayor
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def quitar(self, heapsort=False):
        x, prioridad = self.vector[0][0], self.vector[0][1]
        self.vector[0], self.vector[self.tamanio -
                                    1] = self.vector[self.tamanio-1], self.vector[0]
        self.tamanio -= 1
        self.hundir()
        if not heapsort:
            self.vector.pop()
        return x, prioridad

    def arribo(self, dato, prioridad):
        self.agregar(dato, prioridad)


class HeapMin():

    def __init__(self):
        self.vector = []
        self.tamanio = 0

    def buscar(self, buscado):
        for index, value in enumerate(self.vector):
            # print(buscado, value)
            if value[0][0].info == buscado:
                resultado = index
                return resultado

    def agregar(self, dato, prioridad=3):
        self.vector.append([dato, prioridad])
        self.flotar(self.tamanio)
        self.tamanio += 1

    def flotar(self, indice):
        padre = (indice - 1) // 2
        while (indice > 0 and self.vector[indice][1] < self.vector[padre][1]):
            self.vector[indice], self.vector[padre] = self.vector[padre], self.vector[indice]
            indice = padre
            padre = (indice - 1) // 2

    def hundir(self, indice=0):
        hijo_izq = (indice * 2) + 1
        control = True
        while (control and hijo_izq < self.tamanio):
            mayor = hijo_izq
            hijo_der = hijo_izq + 1
            if hijo_der < self.tamanio:
                if self.vector[hijo_der][1] < self.vector[hijo_izq][1]:
                    mayor = hijo_der

            if self.vector[indice][1] > self.vector[mayor][1]:
                self.vector[indice], self.vector[mayor] = self.vector[mayor], self.vector[indice]
                indice = mayor
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def quitar(self, heapsort=False):
        x, prioridad = self.vector[0][0], self.vector[0][1]
        self.vector[0], self.vector[self.tamanio -
                                    1] = self.vector[self.tamanio-1], self.vector[0]
        self.tamanio -= 1
        self.hundir()
        if not heapsort:
            self.vector.pop()
        return x, prioridad

    def arribo(self, dato, prioridad):
        self.agregar(dato, prioridad)
