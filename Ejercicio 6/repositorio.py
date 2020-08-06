from Provincias import Provincia
from ManejadorProvincias import ManejadorProvincias
from ObjectEncoder import ObjectEncoder

class RespositorioProvincias:
    __prov = None
    __manejador = None

    def __init__(self, prov):
        self.__prov = prov
        diccionario = self.__prov.leerJSONArchivo()
        self.__manejador = self.__prov.decodificarDiccionario(diccionario)
    
    def to_values(self, provincia):
        return provincia.getNombre(), provincia.getCapital(), provincia.getHabitantes(), provincia.getDepartamentos()
    
    def obtenerListaProvincias(self):
        return self.__manejador.getLista()
    
    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia

    def grabarDatos(self):
        self.__prov.guardarJSONArchivo(self.__manejador.toJSON())