import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Enunciado:

1 - Crear una aplicacion que permita cargar clientes y tickets para una sala de juegos.
    A - Cada cliente y ticket deben ser almacenados en dos listas distintas.
    B - El nombre de cada cliente debe ingresarse solamente en letras minusculas, sin espacios
        ni signos de puntuacion.
    C - El boton de mostrar ventas debe iniciar bloqueado si aun no se cargo ninguna,
        luego de la primer carga debe habilitarse en caso de que se quiera ver las ventas del dia.
    D - Luego de realizar cada venta, el campo de nombre de la aplicacion debe quedar vacio (limpiarlo)


2 - Ahora el usuario además de lo solicitado en el punto anterior, deberá ingresar el importe del ticket
    A - El importe lo debemos almacenar en otra lista distinta.
    B - El importe debemos validar que sea un numero entero valido.
    C - Al presionar el boton "Generar Informe", debemos mostrar por consola el Nombre del cliente, Nombre del juego e Importe del ticket con mayor importe y del ticket con menor importe.
    E - También debemos mostrar el promedio de todos los importes ingresados.

3 - 3 - Al presionar el botón "Generar informe por juego" debemos mostrar:
    A - Importe total de cada juego
    B - Cantidad de tickets con importes superior o igual $1.000
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(
            master=self, text="Nombre cliente")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_nombre_cliente = customtkinter.CTkEntry(
            master=self, fg_color="green")
        self.txt_nombre_cliente.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Juegos")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        self.juegos = ['Tejo', 'Bowling', 'Samba', 'Fichines']
        self.combobox_juego = customtkinter.CTkComboBox(
            master=self, values=self.juegos)
        self.combobox_juego.grid(row=1, column=1, padx=20, pady=10)

        self.btn_agregar_ventas = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_venta_on_click)
        self.btn_agregar_ventas.grid(
            row=3, pady=20, columnspan=2, sticky="news")

        self.btn_mostrar_ventas = customtkinter.CTkButton(
            master=self, text="Mostrar Ventas", command=self.btn_mostrar_venta_on_click)
        self.btn_mostrar_ventas.grid(
            row=4, pady=20, columnspan=2, sticky="news")

        self.label3 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label3.grid(row=2, column=0, padx=20, pady=10)
        self.txt_importe_ticket = customtkinter.CTkEntry(master=self)
        self.txt_importe_ticket.grid(row=2, column=1)

        self.btn_generar_informe = customtkinter.CTkButton(
            master=self, text="Generar Informe", command=self.btn_generar_informe_on_click)
        self.btn_generar_informe.grid(
            row=5, pady=20, columnspan=2, sticky="news")

        self.btn_generar_informe_juegos = customtkinter.CTkButton(
            master=self, text="Generar Informe Juegos", command=self.btn_generar_informe_juegos_on_click)
        self.btn_generar_informe_juegos.grid(
            row=6, pady=20, columnspan=2, sticky="news")

        self.lista_clientes = []
        self.lista_juegos = []
        self.lista_importe = []
        self.btn_mostrar_ventas.configure(state="disabled")

    def btn_agregar_venta_on_click(self):
        nombre_cliente = self.txt_nombre_cliente.get()
        juego = self.combobox_juego.get()
        importe = self.txt_importe_ticket.get()
        flag_validacion = True

        
        for letra in nombre_cliente:
            if (letra < "a" or letra > "z"):
                flag_validacion = False
                print("Vuelva a ingresar el nombre, solo letras minusculas")
                break

        for numero in importe:
            if (numero < "0" or numero > "9"):
                flag_validacion = False
                print("Error")
                break

        if (flag_validacion == True):
            self.lista_clientes.append(nombre_cliente)
            self.lista_juegos.append(juego)
            self.lista_importe.append(int(importe))
            self.btn_mostrar_ventas.configure(state="normal")
            self.txt_nombre_cliente.delete(0, 100000)
            print("La validacion es correcta")

    def btn_generar_informe_on_click(self):
        longitud_lista = len(self.lista_importe)
        maximo = None
        minimo = None
        suma = 0
        promedio = 0
    
        for indice in range(longitud_lista):
            if (maximo == None or self.lista_importe[indice] > maximo):
                maximo = self.lista_importe[indice]
                minimo_indice = indice

            if (minimo == None or self.lista_importe[indice] < minimo):
                minimo = self.lista_importe[indice]
                maximo_indice = indice

            suma = suma + int(self.lista_importe[indice])
            promedio = suma / longitud_lista

        
        
        print (f'El ticket de menor importe es: {minimo}, el nombre del cliente: {self.lista_clientes[minimo_indice]}, el juego: {self.lista_juegos [minimo_indice]}\nEl ticket de mayor importe es: {maximo}, el nombre del cliente: {self.lista_clientes[maximo_indice]}, el juego: {self.lista_juegos[maximo_indice]}\nEl promedio es: {promedio}')
        
    
    

    def btn_mostrar_venta_on_click(self):
        #hacer un for mostrar los nombres precio y juego
        suma = 0
        for indice in range(len(self.lista_clientes)):
            suma = suma + self.lista_importe[indice]
        print(f'La suma de las ventas del dia es: {suma}')
    
        
    def btn_generar_informe_juegos_on_click(self):

        pass #hacer el for y dentro match ej si el juego es bowling sumar importes...etc
    #contador 
        contador =  0 
        juegos= self.combobox_juego.get()
        
        for juego in len(juegos):
            match(juego):
                case "Tejo" | "Bowling" | "Samba" |"Fichines":
                    contador ==self.lista_importe.append
                    if(juego >= "1000"):
                        print("El ticket es superior a $1000")
                    


if __name__ == "__main__":
    app = App()
    app.mainloop()
