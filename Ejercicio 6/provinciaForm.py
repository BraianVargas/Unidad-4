import tkinter as tk
from tkinter import messagebox
from Provincias import Provincia
from conexion import Conexion

class ProvinciaForm(tk.LabelFrame):

    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos", "Temperatura", "Sensación Térmica", "Humedad")
    
    def __init__(self, master, campos=fields, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, background="#EFD665",
        **kwargs)
        self.frame = tk.Frame(self,background="#EFD665")
        self.entries = list(map(self.crearCampo, enumerate(campos)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text, background="#EFD665",)
        entry = tk.Entry(self.frame, width=25, background="#FEFFE3")
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        # a partir de un Provincia, obtiene el estado
        # y establece en los valores en el formulario de entrada
        con = Conexion()
        nombre = provincia.getNombre()
        con = Conexion.getClima(self=con, city=nombre)
        values = (provincia.getNombre(), provincia.getCapital(),
        provincia.getHabitantes(), provincia.getDepartamentos(), *con)
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearProvinciaDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo Provincia
        values = [e.get() for e in self.entries]
        provincia=None
        try:
            try:
                provincia = Provincia(*values)
            except NameError as e:
                messagebox.showerror(str(e), parent=self)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class NewProvincia(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = ProvinciaForm(self,campos=("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos"))
        self.btn_add = tk.Button(self, text="Confirmar",
        command=self.confirmar, background="#55F93E")
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    
    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()
        
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

class StateProvinciaForm(ProvinciaForm):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)