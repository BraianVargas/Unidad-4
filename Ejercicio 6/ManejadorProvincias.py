from Provincias import Provincia

class ManejadorProvincias():

    indice = 0
    __provincias = None

    def __init__(self):
        self.__provincias = []

    def agregarProvincia(self, provincia):
        provincia.rowid = ManejadorProvincias.indice
        ManejadorProvincias.indice+=1
        self.__provincias.append(provincia)

    def getLista(self):
        return self.__provincias
    
    def eliminarProvincia(self, provincia):
        indice = self.obtenerIndice(provincia)
        self.__provincias.pop(indice)
    
    def obtenerIndice(self, provincia):
        bandera = False
        i=0
        while not bandera and i < len(self.__provincias):
            if self.__provincias[i].rowid == provincia.rowid:
                bandera=True
            else:
                i+=1
        return i

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            provincias = [provincia.toJSON() for provincia in self.__provincias]
        )
        return d