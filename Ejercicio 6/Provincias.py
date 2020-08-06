class Provincia():

    rowid = 0
    __nombre = ''
    __capital = ''
    __habitantes = 0
    __departamentos = 0

    def __init__(self, nombre, capital, habitantes, departamentos):
        self.__nombre = self.requerido(nombre, "Nombre es un valor requerido")
        self.__capital = self.requerido(capital, "Capital es un valor requerido")
        self.__habitantes = self.requerido(habitantes, "Cantidad de habitantes es un valor requerido")
        self.__departamentos = self.requerido(departamentos, "Cantidad de departamentos es un valor requerido")
    
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def getNombre(self):
        return self.__nombre
    
    def getCapital(self):
        return self.__capital
    
    def getHabitantes(self):
        return self.__habitantes

    def getDepartamentos(self):
        return self.__departamentos
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                capital = self.__capital,
                habitantes = self.__habitantes,
                departamentos = self.__departamentos
            )
        )
        return d