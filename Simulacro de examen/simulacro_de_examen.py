import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
'''
Miguel Alvarez - T.M.

Simulacro Turno Mañana

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.
Cada televidente que vota deberá ingresar:

- Nombre del votante
- Edad del votante (debe ser mayor a 13)
- Género del votante (Masculino, Femenino, Otro)
- El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
- No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:
1) El promedio de edad de las votantes de género Femenino 
2) Del votante más viejo, su nombre.
3) Nombre del votante más joven qué votó a Gianni.
4) Nombre de cada participante y porcentaje de los votos qué recibió.
5) El nombre del participante que debe dejar la casa (El que tiene más votos)

'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True
        
        contador_votos = 0
        
        contador_votos_fem = 0
        contador_edad_fem = 0
        
        bandera_maximo = False
        edad_viejo = 0
        nombre_viejo = ""
        
        edad_joven = 0
        nombre_joven = ""
        
        contador_gianni = 0
        contador_giovani = 0
        contador_esteban = 0
        
        while seguir == True:
            nombre_votante = prompt("Mensaje", "Ingresar nombre del votante:")
            
            edad_votante = int(prompt("Mensaje", "Introduzca edad del votante:"))
            while edad_votante < 13:
                edad_votante = prompt("Mensaje", "Reingrese edad")
                edad_votante = int(edad_votante)
            
            genero = prompt("Mensaje", "El genero es:")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Mensaje", "Erro, reingrese genero")
            
            voto_neg = prompt("Mensaje", "El voto negativo es para:")
            while voto_neg != "Gianni" and voto_neg != "Giovani" and voto_neg != "Esteban":
                voto_neg = prompt("Mensaje", "Reingrese el voto negativo")
            
            if genero == "Femenino":
                contador_edad_fem += edad_votante
                contador_votos_fem += 1
            
            if bandera_maximo == False or edad_votante < edad_viejo:
                edad_viejo = edad_votante
                nombre_viejo = nombre_votante
                bandera_maximo = True
            
            match voto_neg:
                case "Gianni":
                    contador_gianni += 1
                    if edad_votante > edad_joven:
                        nombre_joven = nombre_votante
                case "Giovani":
                    contador_giovani += 1
                case "Esteban":
                    contador_esteban += 1
            
            seguir = question("Mensaje", "¿Desea seguir?")
            contador_votos += 1
            
        if contador_votos_fem > 0: #Para que no divida por 0 (poner esto porque suman puntos)
            promedio_votos_fem = contador_votos_fem / contador_edad_fem
        
        total_votos_negativos = contador_giovani + contador_giovani + contador_esteban
        porcentaje_gianni = (contador_gianni * 100) / total_votos_negativos
        porcentaje_giovani = (contador_giovani * 100) / total_votos_negativos
        porcentaje_esteban = (contador_esteban * 100) / total_votos_negativos
        
        if contador_esteban > contador_gianni and contador_esteban > contador_giovani:
            perdedor = "Esteban"
        elif contador_gianni > contador_giovani:
            perdedor = "Gianni"
        else:
            perdedor = "Giovani"
        
        alert("Mensaje", f"1. El porcentaje de votos femenino es: {promedio_votos_fem}")
        alert("Mensaje", f"2. El votante mas viejo fue: {nombre_viejo}")
        alert("Mensaje", f"3. {nombre_joven} fue el/la más joven que votó por Gianni")
        alert("Mensaje", f"4. Porcentaje de los participantes\n\tGianni: {porcentaje_gianni}%\n\tGiovani: {porcentaje_giovani}%\n\tEsteban: {porcentaje_esteban}%")
        alert("Mensaje", f"5. El que debe abandonar es: {perdedor}")
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()