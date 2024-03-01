import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

-Nombre
-Edad (debe ser mayor a 12)
-Altura (no debe ser negativa)
-Días que asiste a la semana (1, 3, 5)
-Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
A) El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
B) El porcentaje de clientes que asiste solo 1 día a la semana.
C) Nombre y edad del cliente con más altura.
D) Determinar si los clientes eligen más ir 1, 3 o 5 días
E) Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True
        contador_clientes = 0
        
        acumulador_kg_3 = 0
        acumulador_clientes_3 = 0
        acumulador_clientes_1 = 0
        acumulador_clientes_5 = 0
        
        bandera_maximo = False
        peso_muerto_pr = 0
        edad_pr = 0
        nombre_pr = ""
        
        altura_max = 0
        edad_max = 0
        nombre_max = ""
        
        while seguir == True:
            nombre = prompt("Mensaje", "Introduzca su nombre:")

            edad = int(prompt("Mensaje", "Introduzca su edad:"))
            while edad < 12:
                edad = int(prompt("Error", "Reintroduzca su edad:"))
            
            altura = float(prompt("Mensaje", "Introduzca su altura:"))
            while altura < 0:
                altura = float(prompt("Error", "Reintroduzca su altura:"))
            
            dias = prompt("Mensaje", "Introduza los días que asiste:")
            while dias != "1" and dias != "3" and dias != "5":
                dias = prompt("Error", "Reintroduzca los días que asistió:")
            
            kilos = float(prompt("Mensaje", "Introduzca los kg que levanta en peso muerto:"))
            while kilos < 1:
                kilos = float(prompt("Error", "Reintroduzca los kg que levanta en peso muerto:"))
                
                
            if altura > altura_max:
                altura_max = altura
                edad_max = edad
                nombre_max = nombre
            
            match dias:
                case "3":
                    acumulador_clientes_3 += 1
                    acumulador_kg_3 += kilos
                case "1":
                    acumulador_clientes_1 += 1
                case "5":
                    acumulador_clientes_5 += 1
                    if bandera_maximo == False or edad_pr < edad:
                        edad_pr = edad
                        nombre_pr = nombre
                        peso_muerto_pr = kilos
                        bandera_maximo = True
                        
            seguir = question("Mensaje", "¿Desea continuar?")
            contador_clientes += 1
        
        
        total_clientes = acumulador_clientes_1 + acumulador_clientes_3 + acumulador_clientes_5
        
        if acumulador_clientes_3 > 0:
            promedio = acumulador_kg_3 / acumulador_clientes_3
        
        porcentaje_clientes = (acumulador_clientes_1 * 100) / total_clientes
        
        if acumulador_clientes_1 > acumulador_clientes_3 and acumulador_clientes_1 > acumulador_clientes_5:
            mensaje = "La gente prefiere ir al gimnasio un día a la semana"
        elif acumulador_clientes_3 > acumulador_clientes_5:
            mensaje = "La gente prefiere ir al gimnasio tres días a la semana"
        else:
            mensaje = "La gente prefiere ir al gimnasio cinco días a la semana"
        
        alert("Punto A", f"Mensaje el promedio de kg que levantan las personas que asisten solo 3 días es: {promedio}%")
        alert("Punto B", f"El porcentaje de los clientes que asisten un solo dia a la semana es de: {porcentaje_clientes}")
        alert("Punto C", f"{nombre_max} ({edad_max} años) es el cliente más alto ({altura_max} cm.)")
        alert("Punto D", mensaje)
        alert("Punto E", f"{nombre_pr} ({edad_pr} años) fue el que más kg levantó en peso muerto con: {peso_muerto_pr}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()