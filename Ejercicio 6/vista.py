import tkinter as tk
from tkinter import messagebox
from provinciaForm import ProvinciaForm
from provinciaForm import StateProvinciaForm
from provinciaForm import NewProvincia
from Provincias import Provincia
from provinciaList import ProvinciaList

class ProvinciaView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.resizable(0, 0)
        self.list = ProvinciaList(self, height=18,background="#F5CC5E")
        self.form = StateProvinciaForm(self)
        self.btn_new = tk.Button(self, text="Agregar Provincia", background="#55F93E")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
    
    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)
    
    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()
        #Ver estado de Provincia en formulario de Provincia
    
    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)