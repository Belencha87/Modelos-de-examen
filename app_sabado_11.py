import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
5 - De Disney nos quieren contratar para realizar un soft que realice 
los descuentos en las entradas por el dia de la semana
    los lunes y martes tiene un 50% de descuento
    los miércoles un 40% de descuento
    los jueves un 30% de descuento
    los viernes un 10% de descuento
    los sábados y domingos no hay descuento
la entrada general es de $3000 y debemos preguntar cuántas entradas quiere, 
mostrando el precio final por todas las entradas requeridas por el usuario

6 - Al ejercicio 5 agregar lo siguiente- 
la entrada tiene un costo inicial de $3000, pero si saca las entradas 
y es  nacido en argentina te sale $2500 y si es nacionalizado en 
la Argentina $2000

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_dias = customtkinter.CTkLabel(master=self, text="Día")
        self.label_dias.grid(row=0, column=0, padx=20, pady=10)
        
        dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        self.combobox_dias = customtkinter.CTkComboBox(master=self, values=dias)
        self.combobox_dias.grid(row=0, column=1, padx=20, pady=(10, 10))

        self.label_cantidad = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label_cantidad.grid(row=1, column=0, padx=10, pady=10)
        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        
        self.label_nacionalidad = customtkinter.CTkLabel(master=self, text="Nacionalidad")
        self.label_nacionalidad.grid(row=2, column=0, padx=20, pady=10)
        nacionalidad = ['Argentino', 'Nacionalizado', 'Extranjero']
        self.combobox_nacionalidad = customtkinter.CTkComboBox(master=self, values=nacionalidad)
        self.combobox_nacionalidad.grid(row=2, column=1, padx=20, pady=(10, 10))

        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=3, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=3, column=1, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        pass
    
if __name__ == "__main__":
    app = App()
    app.mainloop()