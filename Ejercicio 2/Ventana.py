import requests
import Tkinter as tk
from Tkinter import *
import ttk
import tkFont as font
import tkMessageBox

class Ventana(tk.Tk):
    __ventana=None
    __cantDolares=None
    __Conversion=None
    __venta=None

    def __init__(self):
        complete_url='https://www.dolarsi.com/api/api.php?type=dolar'
        r=requests.get(complete_url)
        x=r.json()
        i=0

        while (i<len(x)) &(x[i]['casa']['nombre'] != 'Oficial'):
            i+=1
        if(i<len(x)):
            self.__venta=float(x[i]['casa']['venta'].replace(',','.'))


        self.__ventana=Tk()
        self.__ventana.title("Conversor de moneda")
        self.__ventana.geometry("330x105")
        self.__ventana.resizable(0,0)

        self.__cantDolares=IntVar()
        self.__Conversion=StringVar()
        self.valor=IntVar()

        self.cuerpo=ttk.Frame(self.__ventana,relief="sunken",padding=(20,10))
        self.txtBxDolar=ttk.Entry(self.cuerpo,textvariable=self.__cantDolares,font="Helvetica 11")
        self.lblDolares=ttk.Label(self.cuerpo,text="Dolares", padding=(20,5), anchor=tk.CENTER)
        self.lblConversion=ttk.Label(self.cuerpo, textvariable=self.__Conversion, padding=(20,5), anchor=tk.CENTER)
        self.btnSalir=ttk.Button(self.cuerpo,text="Salir", width=20,command=self.salir)

        self.cuerpo.grid(row=0,column=0,sticky='nw')
        self.txtBxDolar.grid(row=0,column=1,sticky='nwes')
        self.lblDolares.grid(row=0,column=2,sticky='nwes')
        self.lblConversion.grid(row=1,column=0,sticky='nwes',columnspan=3)
        self.btnSalir.grid(row=2,column=2,sticky='nwes')
        self.__cantDolares.trace('w',self.Calcular)

    def Calcular(self,*args):
        try:
            cant=self.__cantDolares.get()
            if(cant!=''):
                self.valor.set(cant*self.__venta)
                self.__Conversion.set('es equivalente a '+str(self.valor.get())+' pesos')
                self.txtBxDolar.focus()
            else:
                self.valor.set(0)
                self.__Conversion.set('es equivalente a '+str(self.valor.get())+' pesos')
                self.txtBxDolar.focus()
        except ValueError:
            tkMessageBox.showerror(title='Error de tipo',message='Debe ingresar un valor numerico')
            self.valor.set(0)
            self.__Conversion.set('es equivalente a '+str(self.valor.get())+' pesos')
            self.txtBxDolar.focus()
        

    def test(self):
        self.__ventana.mainloop()
        return 0
    def salir(self):
        self.__ventana.destroy()
