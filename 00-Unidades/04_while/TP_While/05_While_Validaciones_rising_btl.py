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
        #1.
        apellido_user = ""
        
        while apellido_user == "":
            apellido_user = prompt("Mensaje", "Ingrese su apellido: ")
            self.txt_apellido.insert(0, apellido_user)
        #2.
        edad_user = None
        while True:
            edad = prompt("Mensaje", "Ingrese su edad: ")
            edad_user = int(edad)
            if edad_user < 18 and edad_user > 90:
                self.txt_edad.insert(0, edad_user)
            elif edad_user == None:
                break

        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
