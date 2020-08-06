from repositorio import RespositorioProvincias
from vista import ProvinciaView
from ObjectEncoder import ObjectEncoder
from controlador import ControladorProvincias

def main():
    prov = ObjectEncoder('datos.json')
    repo = RespositorioProvincias(prov)
    vista = ProvinciaView()
    ctrl = ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()
