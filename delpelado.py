import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Apellido: Cabello
Nombre: Ángel Fabián

Enunciado:

Una importante empresa dedicada a la produccion de alfajores nos solicita un aplicacion que les 
permita controlar la produccion, dicha aplicacion contara con dos botones 

    - ALFAJOR ACEPTADO
    - ALFAJOR DESCARTADO

Mediante los cuales se registrara la cantidad total de alfajores producidos. 

Por tratarse de una produccion artesanal, cada alfajor puede variar su peso, por lo cual es importante
poder registrar el mismo al momento ACEPTARLO o DESCARTARLO. Los pesos deberan ser numeros flotantes 
positivos.

Receta en gramos:
Harina 000	         -   20
Almidón de Maíz	     -   5
Manteca	             -   10
Azúcar		         -   10
Cacao Amargo	     -   0.75
Polvo de hornear     -   0.5
Miel	             -   1
Extracto de Vainilla - 	 0.25
Huevo (gr)	         -   5
Dulce de Leche       -	 25


Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Cantidad total de alfajores fabricados
	B - Cantidad total de alfajores aceptados
	C - Cantidad total de alfajores rechazados
	D - Peso promedio de los alfajores aceptados
	E - Peso promedio de los alfajores rechazados

    F - Materia prima total utilizada *
    G - Materia prima total desperdiciada *

    *(Tener en cuenta que la coccion produce una merma de 15% del peso)
    
    Cada kilo de alfajor terminado esta formado por:
    Harina 000             253g
    Almidón de Maíz         65g
    Manteca                130g
    Azúcar                 130g
    Cacao Amargo            10g
    Polvo de hornear         7g
    Miel                    13g
    Extracto de Vainilla     4g
    Huevo (gr)              65g
    Dulce de Leche         323g

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window

        self.title("UTN FRA")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Peso Alfajor")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.btn_aceptar = customtkinter.CTkButton(master=self, text="ACEPTAR", command=self.btn_aceptar_on_click)
        self.btn_aceptar.grid(row=2, pady=10, columnspan=2, sticky="news")

        self.btn_rechazar = customtkinter.CTkButton(master=self, text="RECHAZAR", command=self.btn_rechazar_on_click)
        self.btn_rechazar.grid(row=3, pady=10, columnspan=2, sticky="news")

        self.btn_generar_informe = customtkinter.CTkButton(master=self, text="Generar Informe", command=self.btn_generar_informe_on_click)
        self.btn_generar_informe.grid(row=5, pady=20, columnspan=2, sticky="news")
        
        self.lista_pesos_rechazados = []
        self.lista_pesos_aceptados = []
        self.peso_total_aceptados=0
        self.peso_total_rechazados=0
            
    def btn_aceptar_on_click(self):
        peso_alfajor=self.txt_peso_articulo.get()
        flag_peso=False
        
        for digito in peso_alfajor:
            if(digito>="0" and digito<="9" or digito=="." and float(peso_alfajor)>0):
                flag_peso=True
            else:
                break
        if(flag_peso==True):
            peso_alfajor=float(peso_alfajor)
            self.lista_pesos_aceptados.append(peso_alfajor)
            self.peso_total_aceptados+=peso_alfajor
            mensaje="Alfajor aceptado"
            self.txt_peso_articulo.delete(0,20)
        else:
            mensaje="Por favor ingrese solo dígitos y pesos mayores a 0"
            
        alert("AVISO",mensaje)

    def btn_rechazar_on_click(self):
        peso_alfajor=self.txt_peso_articulo.get()
        flag_peso=False
        
        for digito in peso_alfajor:
            if(digito>="0" and digito<="9" or digito=="." and float(peso_alfajor)>0):
                flag_peso=True
            else:
                break
        if(flag_peso==True):
            peso_alfajor=float(peso_alfajor)
            self.lista_pesos_rechazados.append(peso_alfajor)
            self.peso_total_rechazados+=peso_alfajor
            mensaje="Alfajor rechazado"
            self.txt_peso_articulo.delete(0,20)
        else:
            mensaje="Por favor ingrese solo dígitos y pesos mayores a 0"
        
        alert("AVISO",mensaje)
        
    def btn_generar_informe_on_click(self):
        # A - Cantidad total de alfajores fabricados
        total_fabricados=len(self.lista_pesos_aceptados)+len(self.lista_pesos_rechazados)
        
        # B - Cantidad total de alfajores aceptados
        total_aceptados=len(self.lista_pesos_aceptados)

        # C - Cantidad total de alfajores rechazados
        total_rechazados=len(self.lista_pesos_rechazados)

        # D - Peso promedio de los alfajores aceptados
        promedio_aceptados=(self.peso_total_aceptados/len(self.lista_pesos_aceptados))/1000

        # E - Peso promedio de los alfajores rechazados
        promedio_rechazados=(self.peso_total_rechazados/len(self.lista_pesos_rechazados))/1000
        
        # F/G - Materia prima total utilizada/rechazada *
        peso_total=(self.peso_total_aceptados+self.peso_total_rechazados)/1000
        lista_ingredientes_pesos=[0.253,0.065,0.130,0.130,0.010,0.007,0.013,0.004,0.065,0.323]
        lista_ingredientes_pesos_totales=[]
        lista_ingredientes_pesos_totales_rechazados=[]

        for ingrediente_peso in lista_ingredientes_pesos:
            peso_total_por_ingrediente=(ingrediente_peso*peso_total)/0.85
            lista_ingredientes_pesos_totales.append(peso_total_por_ingrediente)

            peso_total_por_ingrediente_rechazado=(ingrediente_peso*self.peso_total_rechazados/1000)/0.85
            lista_ingredientes_pesos_totales_rechazados.append(peso_total_por_ingrediente_rechazado)
        
        # INFORMES
        mensaje="Cantidad total de alfajores fabricados: {0}\n"\
                "Cantidad total de alfajores aceptados: {1}\n"\
                "Cantidad total de alfajores rechazados: {2}\n"\
                "Peso promedio de los alfajores aceptados {3} kgs.\n"\
                "Peso promedio de los alfajores rechazados: {4} kgs.\n".format(total_fabricados,
                                                                                total_aceptados,
                                                                                total_rechazados,
                                                                                promedio_aceptados,
                                                                                promedio_rechazados)
        alert("AVISO",mensaje)

        mensaje="Materia prima total utilizada\n"\
                "Harina: {0:.3f} kgs.\n"\
                "Almidón de Maíz: {1:.3f} kgs.\n"\
                "Manteca: {3:.3f} kgs.\n"\
                "Azúcar: {3:.3f} kgs.\n"\
                "Cacao Amargo: {4:.3f} kgs.\n"\
                "Polvo de hornear: {5:.3f} kgs.\n"\
                "Miel: {6:.3f} kgs.\n"\
                "Extracto de Vainilla: {7:.3f}\n"\
                "Huevo: {8:.3f} kgs.\n"\
                "Dulce de Leche: {9:.3f} kgs.\n".format(lista_ingredientes_pesos_totales[0],
                                                        lista_ingredientes_pesos_totales[1],
                                                        lista_ingredientes_pesos_totales[2],
                                                        lista_ingredientes_pesos_totales[3],
                                                        lista_ingredientes_pesos_totales[4],
                                                        lista_ingredientes_pesos_totales[5],
                                                        lista_ingredientes_pesos_totales[6],
                                                        lista_ingredientes_pesos_totales[7],
                                                        lista_ingredientes_pesos_totales[8],
                                                        lista_ingredientes_pesos_totales[9])
        alert("AVISO",mensaje)

        mensaje="Materia prima total descartada\n"\
                "Harina: {0:.3f} kgs.\n"\
                "Almidón de Maíz: {1:.3f} kgs.\n"\
                "Manteca: {3:.3f} kgs.\n"\
                "Azúcar: {3:.3f} kgs.\n"\
                "Cacao Amargo: {4:.3f} kgs.\n"\
                "Polvo de hornear: {5:.3f} kgs.\n"\
                "Miel: {6:.3f} kgs.\n"\
                "Extracto de Vainilla: {7:.3f} kgs.\n"\
                "Huevo: {8:.3f} kgs.\n"\
                "Dulce de Leche: {9:.3f} kgs.\n".format(lista_ingredientes_pesos_totales_rechazados[0],
                                                        lista_ingredientes_pesos_totales_rechazados[1],
                                                        lista_ingredientes_pesos_totales_rechazados[2],
                                                        lista_ingredientes_pesos_totales_rechazados[3],
                                                        lista_ingredientes_pesos_totales_rechazados[4],
                                                        lista_ingredientes_pesos_totales_rechazados[5],
                                                        lista_ingredientes_pesos_totales_rechazados[6],
                                                        lista_ingredientes_pesos_totales_rechazados[7],
                                                        lista_ingredientes_pesos_totales_rechazados[8],
                                                        lista_ingredientes_pesos_totales_rechazados[9])
        alert("AVISO",mensaje)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
