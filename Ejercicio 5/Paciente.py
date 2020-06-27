import re
class Paciente(object):
    telefonoRegex=re.compile(r"\([0-9]{3}\)[0-9]{7}")

    __apellido=None
    __nombre=None
    __telefono=None
    __altura=None
    __peso=None

    def __init__(self,Nombre,Apellido,Telefono,Altura,Peso):
        self.__apellido = self.requerido(Apellido,'Apellido es un valor requerido')
        self.__nombre = self.requerido(Nombre,'Nombre es un valor requerido')
        self.__telefono = self.requerido(Telefono,'Telefono es un valor requerido')
        self.__altura = self.requerido(Altura,'Altura es un valor requerido')
        self.__peso = self.requerido(Peso,'Peso es un valor requerido')

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def formatoValido(self,valor,regex,mensaje):
        if not valor or not regex.match(valor):
            raise ValueError
        return valor
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                apellido=self.__apellido,
                nombre=self.__nombre,
                telefono=self.__telefono,
                altura=self.__altura,
                pes0=self.__peso
            )
        )
        return d
