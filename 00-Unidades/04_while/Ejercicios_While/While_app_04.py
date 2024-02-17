import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Miguel
apellido: Alvarez
---
Ejercicio: while_04
---
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        numero = int(prompt("Mensaje", "Ingrese el número: "))
        
        while numero < 0 or numero > 9:
            numero = int(prompt("Error", "Reingrese el número"))
        
        
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
    
    
    
'''''   
and - > A and B 
A = True - evalua B
B = False - no evalua B

or - > A or B
A = True - no evalua B
B = False - evalua B
'''''