import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
1.   Apellido
2.   Edad, entre 18 y 90 años inclusive.
3.   Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
4.   Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = None
        edad = None
        estado_civil = None
        nro_legajo = None
        
        while apellido == None:
            apellido = prompt("Mensaje", "Ingrese su apellido:")
            
            edad = int(prompt("Mensaje", "Ingrese su edad:"))
            while edad < 18 or edad > 90:
                edad = int(prompt("Mensaje", "Ingrese su edad:"))
                
            estado_civil = prompt("Mensaje", "Ingrese su estado civil:")
            while estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a":
                    estado_civil = prompt("Mensaje", "Ingrese su estado civil:")
            
            nro_legajo = int(prompt("Mensaje", "Ingrese número de legajo:"))
            while nro_legajo < 1000 or nro_legajo > 9999:
                nro_legajo = int(prompt("Mensaje", "Ingrese número de legajo:"))
        
        self.combobox_tipo.set(estado_civil)
        self.txt_apellido.delete(0, "end")
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, "end")
        self.txt_edad.insert(0, edad)
        self.txt_legajo.delete(0, "end")
        self.txt_legajo.insert(0, nro_legajo)
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
