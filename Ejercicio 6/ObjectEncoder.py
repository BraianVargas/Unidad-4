import json
from pathlib import Path
from Provincias import Provincia
from ManejadorProvincias import ManejadorProvincias


class ObjectEncoder(object):
    
    __pathArchivo=None
    
    def __init__(self, pathArchivo):
        self.__pathArchivo = pathArchivo

    def guardarJSONArchivo(self, diccionario):
        archivo = self.__pathArchivo
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
        destino.close()

    def leerJSONArchivo(self):
        archivo = self.__pathArchivo
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if(class_name == 'ManejadorProvincias'):
                provincias = d['provincias']
                dProvincias = provincias[0]
                manejador = class_()
                for i in range(len(provincias)):
                    dProvincias = provincias[i]
                    class_name = dProvincias.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dProvincias['__atributos__']
                    unProvincia = class_(**atributos)
                    manejador.agregarProvincia(unProvincia)
            return manejador