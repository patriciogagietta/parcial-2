class nodoCola():
    info, sig = None, None


class Cola():

    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamnio = 0

    def arribo(self, dato):  # Agrega el elemento al final de la cola;
        nodo = nodoCola()
        nodo.info = dato

        if self.__final is None:
            self.__frente = nodo
        else:
            self.__final.sig = nodo
        self.__final = nodo

        self.__tamnio += 1

    def atencion(self):  # Elimina y devuelve el elemento almacenado en el frente de la cola;
        dato = self.__frente.info

        self.__frente = self.__frente.sig
        if self.__frente is None:
            self.__final = None

        self.__tamnio -= 1
        return dato

    def tamanio(self):
        return self.__tamnio

    def cola_vacia(self):
        return self.__frente is None

    def en_frente(self):  # Devuelve el valor del elemento que está almacenado en el frente de la cola sin eliminarlo;
        return self.__frente.info

    # Elimina el elemento en el frente de la cola y lo inserta en el final de la misma;
    def mover_al_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato
