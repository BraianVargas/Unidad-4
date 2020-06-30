from tkinter import *
import tkinter as tk
from tkinter import ttk,StringVar,messagebox,font
import requests
from datetime import datetime
import time
import os
class PCotizaciones:
    __Ventana=None
    __Info_Api=None
    def __init__(self):
        self.__Ventana=Tk()
        self.__Ventana.geometry('600x300')
        self.__Ventana.title('Cotizaciones')
        self.__Ventana.configure(bg='White')
        self.fuente=font.Font(weight='bold',font='Arial 12')
        tk.Label(self.__Ventana,text='COTIZACIONES',font='Arial 20',bg='White',fg='Blue').grid(row=0,column=2)
        self.Hora=StringVar()
        self.Guardar()
        self.longitud=len(self.__Info_Api)
        self.Boton=tk.Button(self.__Ventana,text='Actualizar',command=self.Actualizar,fg="Black",font=self.fuente,bg='White')
        self.Boton.grid(row=self.longitud,column=2,sticky=S)
        self.Hora.set('No hubo actualizaciones')
        self.Fechalbl=tk.Label(self.__Ventana,textvariable=self.Hora,font=self.fuente,fg='Blue')
        self.Fechalbl.grid(row=self.longitud+1,column=2,sticky=S)
        self.__Ventana.mainloop()
    def Actualizar(self):
        self.__Info_Api=None
        self.Guardar()
        hora=datetime.now().hour
        minuto=datetime.now().minute
        self.Hora.set('Ultima Actualizacion '+str(hora)+':'+str(minuto))
    def Guardar(self):
        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        self.__Info_Api=r.json()
        self.longitud=len(self.__Info_Api)
        for i in range(len(self.__Info_Api)):
            dolartxt=self.__Info_Api[i]['casa']['nombre'].split()
            if(dolartxt[0].lower()=='dolar'):
                if( self.__Info_Api[i]['casa']['compra']!='No Cotiza' and  self.__Info_Api[i]['casa']['venta']!=0):            
                    self.DatoDolar=StringVar()
                    self.DatoCompra=StringVar()
                    self.DatoVenta=StringVar()
                    self.DatoDolar.set(self.__Info_Api[i]['casa']['nombre'])
                    self.DatoCompra.set(self.__Info_Api[i]['casa']['compra'].replace(',','.'))
                    self.DatoVenta.set(self.__Info_Api[i]['casa']['venta'].replace(',','.'))
                    tk.Label(self.__Ventana,textvariable=self.DatoDolar,font=self.fuente,bg='White').grid(row=i+1,column=0,sticky=W)
                    tk.Label(self.__Ventana,text='Compra:',font=self.fuente,bg='White').grid(row=i+1,column=1,sticky=W)
                    tk.Label(self.__Ventana,textvariable=self.DatoCompra,font=self.fuente,bg='White').grid(row=i+1,column=2,sticky=W)
                    tk.Label(self.__Ventana,text='Venta:',font=self.fuente,bg='White').grid(row=i+1,column=3,sticky=W)
                    tk.Label(self.__Ventana,textvariable=self.DatoVenta,font=self.fuente,bg='White').grid(row=i+1,column=4,sticky=W)                   