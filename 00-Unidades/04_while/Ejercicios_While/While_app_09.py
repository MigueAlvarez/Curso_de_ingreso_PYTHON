import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        '''     forma 1 = declarando variables y solo con if 
        minimo = 1000
        maximo = -1000
        '''
        i = 0 #validador
        
        while i < 5:
            numero = input("Ingrese un número")
            numero = int(numero)
            
            if i == 0:           #si utilizo esto no es necesesario declarar la variable numero (1000 y -1000 en este caso) forma 2
                maximo = numero
                minimo = numero
            else:
                if numero > maximo: #valido con la forma 1, 2 y 3(max y min)
                    maximo = numero
                if numero < minimo:
                    minimo = numero
        i += 1
        
        print(f"Maximo: {maximo} -- Minimo: {minimo}")
        
        '''
            if i == 0 or numero > maximo:   forma 3 hay que declarar si o si las 2 variables
                maximo = numero
            if i == 0 or numero < minimo:
                minimo = numero
        '''
        
        
        
        
        
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
