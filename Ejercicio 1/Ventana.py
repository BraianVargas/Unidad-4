import tkinter as tk
from tkinter import *
from tkinter import ttk, font
class Ventana(tk.Tk):
    __ventana=None
    __altura=None
    __peso=None
    __mensaje=None
    __estado=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Calculadora IMC")
        self.__ventana.geometry("450x350")
        self.__ventana.resizable(0,0)

        self.__altura=IntVar()
        self.__peso=IntVar()
        self.__mensaje=StringVar()
        self.__estado=StringVar()

        self.cabecera=ttk.Frame(self.__ventana,relief="raised",padding=(20,10))
        self.lblCabecera=ttk.Label(self.cabecera, text="Calculadora de IMC",font="Arial 18",padding=(20,5),anchor=tk.CENTER,background="#ccc")
        self.cuerpo=ttk.Frame(self.__ventana,padding=(10,5))
        separador= ttk.Separator(self.cuerpo,orient=tk.HORIZONTAL)

        #"***SECTOR ALTURA***"
        self.lblAltura=ttk.Label(self.cuerpo,text="Altura: ",font="Helvetica 8",padding=(0,15))
        self.bxAltura=ttk.Entry(self.cuerpo,textvariable=self.__altura,font="Helvetica 14",width=30)
        self.lblCm=ttk.Label(self.cuerpo,anchor=tk.CENTER,text="cm",font="Helvetica 8",background="#AFB0AF",padding=5)

        #"***SECTOR PESO***"
        self.lblPeso=ttk.Label(self.cuerpo,text="Peso: ",font="Helvetica 8",padding=(0,15))
        self.bxPeso=ttk.Entry(self.cuerpo,textvariable=self.__peso,font="Helvetica 14",width=30)
        self.lblKg=ttk.Label(self.cuerpo,anchor=tk.CENTER,text="kg",font="Helvetica 8",background="#AFB0AF",padding=5)

        separador1= ttk.Separator(self.cuerpo,orient=tk.HORIZONTAL)

        #"***SECTOR ALTURA***"
        self.cabecera.grid(row=0, column=0,sticky='we')
        self.lblCabecera.grid(row=0, column=0,columnspan=3,sticky='we')
        separador.grid(row=1, column=0,columnspan=4,sticky='we')
        self.cuerpo.grid(row=1,column=0,columnspan=3,sticky='nw')
        self.lblAltura.grid(row=3,column=1,sticky='nw')
        self.bxAltura.grid(row=3,column=2)
        self.lblCm.grid(row=3,column=3)
        separador1.grid(row=5, column=0,columnspan=4,sticky='we')


        #"***SECTOR PESO***"
        self.lblPeso.grid(row=6,column=1,sticky='nw')
        self.bxPeso.grid(row=6,column=2)
        self.lblKg.grid(row=6,column=3)
        separador2= ttk.Separator(self.cuerpo,orient=tk.HORIZONTAL)
        separador2.grid(row=7, column=0,columnspan=4,sticky='we')

        #"***SECTOR BOTONES***"
        self.btnCalc=tk.Button(self.cuerpo,text="Calcular",bg="#77CC77",width=20,command=self.Calcula)
        self.btnLimp=tk.Button(self.cuerpo,text="Limpiar",bg="#77CC77",width=20,command=self.Limpiar)
        self.btnCalc.grid(row=8,column=2,sticky='w')
        self.btnLimp.grid(row=8,column=2,sticky='e')

        #***SECTOR MUESTRA***
        self.result=tk.Frame(self.__ventana,relief="raised",bg="#9CE59C",padx=20,pady=30)
        self.result.grid(row=9,column=0)
        self.res=ttk.Label(self.result,text="Tu indice de Masa Corporal es: ",font="Helvetica 8",foreground="#027602",background="#9CE59C")
        self.res.grid(row=0,column=0,sticky='nw')
        self.res1=ttk.Label(self.result,textvariable=self.__mensaje,font="Helvetica 16 bold",foreground="#027602",background="#9CE59C")
        self.res1.grid(row=0,column=1,sticky='nw')
        self.res2=ttk.Label(self.result,textvariable=self.__estado,font="Arial 14",foreground="#027602",background="#9CE59C")
        self.res2.grid(row=1,column=0,sticky='nswe')

    def Calcula(self):
        try:
            
            self.alturaM=float(self.__altura.get())/100
            self.alturaM=self.alturaM**2
            if(self.alturaM==0):
                self.alturaM=1
            self.__total=float(self.__peso.get())/self.alturaM
            self.__mensaje.set("{:.2f}".format(self.__total))

            if(self.__total<18.5):
                self.res2.configure(foreground='black', background='blue')
                self.__estado.set("Peso inferior al normal")

            if(self.__total>=18.5 and self.__total<=24.9):
                self.res2.configure(foreground='black', background='green')
                self.__estado.set("Peso normal")

            if(self.__total>=25 and self.__total<=29.9):
                self.res2.configure(foreground='black', background='orange')
                self.__estado.set("Peso superior al normal")

            if(self.__total>30):
                self.res2.configure(foreground='black', background='red')
                self.__estado.set("Obesidad")
        except:
            pass

    def Limpiar(self):
        self.__estado.set("")
        self.__altura.set("")
        self.__peso.set("")
        self.__mensaje.set("")
        self.res2.configure(foreground='#9CE59C', background='#9CE59C')


    def test(self):
        self.__ventana.mainloop()
        return 0
