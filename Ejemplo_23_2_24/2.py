import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive. (EVALUAR)
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''
'''
Notas de evaluación: Si no aparece en el enunciado, ni pelota.
                     Si hay cosas que no se pueden validar, seguir.
                     Pensar que el usuario siempre va a poner los datos bien.

Antes de empezar:
1) Identificar:
a) ¿Qué va antes del While?
b) ¿Qué va dentro del While?
c) ¿Qué va fuera del While?

2) Empezar con las carga de datos.

'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #¿Qué va antes del While? 
        seguir = True
        
        contador_masculino_IOT_IA = 0
        
        IOT_contador = 0
        IA_contador = 0
        RVRA_contador = 0
        
        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0
        contador_IOT_edad = 0
        
        contador_femenino_IA = 0
        acumulador_femenino_edad = 0
        
        bandera_minimo = False
        minima_edad = 0
        nombre_minimo = ""
        genero_minimo = ""
        
        #¿Qué va dentro del While? Se empieza por acá
        while seguir == True: #Se puede usar el "seguir = " como bandera, es decir solo pondriamos "while seguir:"
            nombre = prompt("Mensaje", "Ingrese nombre:") #Si no dice el enunciado nada para validar el nombre que no me interese, seguimos.
            
            edad = prompt("Mensaje", "Ingrese edad:")
            edad = int(edad)
            while edad < 18:
                edad = prompt("Error", "Reingrese edad:") #Tengo la validacion de la edad
                edad = int(edad)
            
            genero = prompt("Mensaje", "Ingrese genero:")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro": #va "and" pq te aseguras que no puso nada que sea algo que no este en la lista de opciones
                genero = prompt("Error", "Reingrese genero:")

            tecnologia = prompt("Mensaje", "Ingrese tecnologia: ")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("Error", "Reingrese tecnologia:")
            
            #1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive. (EVALUAR)
            if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50: #Poner () despues del and porque es como un X en matematicas
                contador_masculino_IOT_IA += 1
            #2) - Tecnología que mas se votó.
            if tecnologia == "IOT":
                IOT_contador += 1
                #4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42. (Aprovecho que tengo ya creada el contador de IOT)
                if edad >= 18 and edad <= 25 or edad >= 33 and edad <= 42:
                    contador_IOT_edad += 1
            elif tecnologia == "IA":
                IA_contador += 1
            else:
                RVRA_contador += 1
                #6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                if bandera_minimo == False or edad < minima_edad:
                    minima_edad = edad
                    nombre_minimo = nombre
                    genero_minimo = genero
                    bandera_minimo = True
                                
            #3) - Porcentaje de empleados por cada genero
            match genero:
                case "Masculino":
                    contador_masculino += 1
                case "Femenino":
                    contador_femenino += 1
                    #5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                    if tecnologia == "IA":
                        contador_femenino_IA += 1
                        acumulador_femenino_edad += edad
                case "Otro":
                    contador_otro += 1
            
                

            seguir = question("Seguir", "¿Desea continuar?") #sirve para detener la carga de datos del usuario - si pone que NO devuelve un False - siempre es la última sentencia del While.
################################################################################################################################## 
        #¿Qué va fuera del While?
        #2) - Tecnología que mas se votó.
        if IOT_contador > IA_contador and IOT_contador > RVRA_contador:
            tecnologia_mas_votada = "IA"
        elif IA_contador > RVRA_contador:
            tecnologia_mas_votada = "IOT"
        else:
            tecnologia_mas_votada = "RV/RA"
        # 3) - Porcentaje de empleados por cada genero
        total_empleados = contador_masculino + contador_femenino + contador_otro
        porcentaje_masculino = (contador_masculino * 100) / total_empleados
        porcentaje_femenino = (contador_femenino * 100) / total_empleados
        porcentaje_otro = (contador_otro * 100) / total_empleados
        
        #4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42. OJO QUE NO ESTA ACLARADO SOBRE QUE SE SACA EL PORCENTAJE - PREGUNTAR AL PROFE!
        porcentaje_IOT_edad = (contador_IOT_edad * 100) / total_empleados
        
        #5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        promedio_edad_femenino = acumulador_femenino_edad / contador_femenino_IA
        
        print(f"1. Cantidad de empleados de género masculino que votaron por IOT o IA (entre 25 y 50 años): {contador_masculino_IOT_IA}")
        print(f"2. La tecnologia que mas se voto es: {tecnologia_mas_votada}")
        print(f"3. El porcentaje de empleados es:\n\tMasculinos: {porcentaje_masculino}\n\tFemenino: {porcentaje_femenino}\n\tOtro: {porcentaje_otro}")
        print(f"4. El porcentaje de empleados que votaron por IOT es: {porcentaje_IOT_edad}")
        print(f"5. El promedio de edad de las empleadas que votaron por IA es de: {promedio_edad_femenino}")
        print(f"6. El empleado {nombre_minimo}, de {minima_edad} años ({genero_minimo}), fue el más joven que votó RV/RA")
        
        
        pass 
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()