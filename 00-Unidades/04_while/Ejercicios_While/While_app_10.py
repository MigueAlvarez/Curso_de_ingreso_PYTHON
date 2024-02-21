import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Miguel
apellido: Alvarez
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_pos = 0
        acumulador_neg = 0
        contadores_pos = 0
        contadores_neg = 0
        contador_ceros = 0
        
        flag = True
        minimo_pos = 0
        # bandera = True -> Es un control de estado (puede ser True ó False)
        # MAXIMOS Y MINIMOS NO SE INICIALIZAN
        
        while True:
            numero = prompt("Mensaje", "Ingrese número")
            if numero != None and numero != "":
                numero = int(numero)
            else:
                break
            
            if numero > 0:
                acumulador_pos += numero
                contadores_pos += 1
            elif numero < 0:
                acumulador_neg += numero
                contadores_neg += 1
            else:
                contador_ceros += 1
            
            
        diferencia = contadores_pos - contadores_neg
        
        mensaje = f"Resultado: \n A. La suma acumulada de negativos es: {acumulador_neg}\n B. La suma acumulada de positivos es: {acumulador_pos}\n C. Cantidad de números positivos es: {contadores_pos}\n D. Cantidad de números negativos es: {contadores_neg}\n Cantidad de ceros es: {contador_ceros}\n F. La diferencia entre positivos y negativos es: {diferencia}"
            
        alert("Mensaje", mensaje)
        
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
