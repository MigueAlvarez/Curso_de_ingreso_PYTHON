import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Un famoso casino de mar del plata, requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:
-Nombre
-Importe ganado (mayor o igual $1000)
-Género (“Femenino”, “Masculino”, “Otro”)
-Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:
A) Nombre y género de la persona que más ganó.
B) Promedio de dinero ganado en Ruleta.
C) Porcentaje de personas que jugaron en el Tragamonedas.
D) Cuál es el juego menos elegido por los ganadores.
E) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
F) Porcentaje de dinero en función de cada juego.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True
        acumulador_ganadores = 0
        
        bandera_max = False
        max_ganador_nombre = ""
        max_ganador_genero = ""
        max_ganador = 0
        
        contador_ruleta = 0
        contador_tragamonedas = 0
        contador_poker = 0
        
        acumulador_ganado_ruleta = 0
        
        contador_no_poker = 0
        acumulador_no_poker = 0
        
        
        while seguir == True:
            nombre = prompt("Mensaje", "Ingrese su nombre:")
            while nombre == None:
                nombre = prompt("Mensaje", "Reingrese su nombre:")
                break
            
            genero = prompt("Mensaje", "Ingrese su género:")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Error", "Reingrese su género:")
                
            juego = prompt("Mensaje", "Ingrese el juego:")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("Error", "Reingrese el juego:")
            
            importe_ganado = float(prompt("Mensaje", "Ingrese el monto ganado:"))
            while importe_ganado <= 1000:
                importe_ganado = float(prompt("Error", "Reingrese el monto ganado (mayor a $1000):"))
            
            if bandera_max == False or importe_ganado > max_ganador:
                max_ganador = importe_ganado
                max_ganador_genero = genero
                max_ganador_nombre = nombre
                bandera_max = True
            
            match juego:
                case "Ruleta":
                    acumulador_ganado_ruleta += importe_ganado
                    contador_ruleta += 1
                case "Tragamonedas":
                    contador_tragamonedas += 1
                case "Poker":
                    contador_poker += 1
            
            if juego != "Poker" and importe_ganado > 15000:
                contador_no_poker += 1
                acumulador_no_poker += importe_ganado
            
            seguir = question("Mensaje", "¿Desea seguir?")
            acumulador_ganadores += 1
        
        if contador_ruleta > 0:
            promedio_ruleta = importe_ganado / contador_ruleta
            
        total_ganadores = contador_poker + contador_ruleta + contador_tragamonedas
        porcentaje_tragamonedas = (contador_tragamonedas * 100) / total_ganadores
        
        if contador_ruleta < contador_tragamonedas and contador_ruleta < contador_poker:
            mensaje = "La 'Ruleta' fue el juego menos elegido por los ganadores"
        elif contador_poker < contador_tragamonedas:
            mensaje = "El 'Poker' fue el juego menos elegido por los ganadores"
        else:
            mensaje = "Las 'Tragamonedas' fue el juego menos elegido por los ganadores"
            
        if contador_no_poker > 0:
            promedio_no_poker = acumulador_no_poker / contador_no_poker
            mensaje_E = f"El promedio de importe ganado por las personas que no jugaron Poker y ganaron más de $15000 es de: {promedio_no_poker}"
        else:
            mensaje_E = "No hay suficientes datos para calcular el promedio."
        
        alert("Punto A", f"{max_ganador_nombre} ({max_ganador_genero}) fue el más ganador/a")
        alert("Punto B", f"El promedio de dinero ganado en la 'Ruleta' es de: {promedio_ruleta}")
        alert("Punto C", f"El porcentaje de de personas que jugaron a las 'Tragamonedas' es de: {porcentaje_tragamonedas}%")
        alert("Punto D", mensaje)
        alert("Punto E", mensaje_E)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()