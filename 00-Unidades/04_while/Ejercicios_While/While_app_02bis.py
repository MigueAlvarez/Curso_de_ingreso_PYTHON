import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Miguel
apellido: Alvarez
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        cuenta_inicial = 0
        acumulador_suma = 0
        while cuenta_inicial < 11:
            if cuenta_inicial % 2 == 0: # % es para buscar resto 0 (numero par)
                acumulador_suma = acumulador_suma + cuenta_inicial
            
            cuenta_inicial += 1
            
        alert("Mensaje", f"La cuenta entre 1 y 11 es: {cuenta_inicial}")
            
        
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()