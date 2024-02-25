import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Miguel
apellido: Alvarez
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag = True
        
        nombre_candidato_mas_votos = None
        max_cantidad_votos = None
        
        menor_votado = None
        menos_votado_nombre = None
        menos_votado_edad = None
        
        edad_contador = 0
        votos_totales = 0
        candidatos_contador = 0
        
        while flag == True:
            nombre_candidato = prompt("Mensaje", "Introduzca nombre del candidato:")
            if nombre_candidato == None:
                break
            
            edad_candidato = prompt("Mensaje", "Introduzca edad del candidato:")
            edad_candidato = int(edad_candidato)
            while edad_candidato < 25:
                edad_candidato = prompt("Mensaje", "La edad del candidato tiene que ser mayor a 25 años.")
                edad_candidato = int(edad_candidato)
                
            cantidad_votos = prompt("Mensaje", "Cantidad de votos que recibió:")
            cantidad_votos = int(cantidad_votos)
            
            while cantidad_votos < 0:
                cantidad_votos = prompt("Mensaje", "Ingrese la cantidad de votos:")
                cantidad_votos = int(cantidad_votos)
                
            if max_cantidad_votos == None or cantidad_votos > max_cantidad_votos:
                nombre_candidato_mas_votos = nombre_candidato
                max_cantidad_votos = cantidad_votos
                
            if menor_votado == None or cantidad_votos < menor_votado:
                menor_votado = cantidad_votos
                menos_votado_nombre = nombre_candidato
                menos_votado_edad = edad_candidato
            
            edad_contador += edad_candidato
            votos_totales += cantidad_votos
            
            flag = question("Mensaje", "¿Desea seguir ingresando?")
            candidatos_contador += 1
            
        promedio = edad_contador / candidatos_contador
        
        alert("Mensaje", f"El candidato con más votos fue {nombre_candidato_mas_votos}")
        alert("Mensaje", f"El candidato, {menos_votado_nombre} ({menos_votado_edad} años), fue el menos votado.")
        alert("Mensaje", f"El promedio de edad de los candidatos es de: {promedio}")
        alert("Mensaje", f"El total de sufragios en el día de hoy fue de: {votos_totales}")
        
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
