import tkinter as tk
import math
import re


class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("calculadora")
        self.ventana.configure(bg="blue")
        
        
        self.pantalla = tk.Entry(self.ventana, width=60, bg="lightblue", borderwidth=5, fg="black")
        self.pantalla.grid(row=0, column=0, padx=9, pady=9, columnspan=4)
        
        self.crear_botones()
   
    def crear_botones(self):
        botones = [
            ("1",1,0), ("2",1,1), ("3",1,2),
            ("4",2,0), ("5",2,1), ("6",2,2),
            ("7",3,0), ("8",3,1), ("9",3,2),
            ("0",4,0), ("c",1,3), ("+",2,3),
            ("-",3,3), ("*",4,3), ("=",4,1),
            ("/",4,2), ("dist(",5,1), (",",5,2), (")",5,3)
        ]
        
        for(text, row, column) in botones:
            button = tk.Button(self.ventana, text=text, bg="lightblue",fg="black", padx=28, pady=28, command=lambda t=text: self.boton_click(t))
            button.grid(row=row, column=column)
                
    def boton_click(self, valor):
        if valor == "=":
            expresion = self.pantalla.get()
            try:
                if expresion.startswith("dist"):
                    distancia = self.calcular_distancia(expresion)
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, str(distancia)) 
                else:
                    resultado = str(eval(expresion))
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, resultado)
            
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error")

        elif valor == "c":
            self.pantalla.delete(0, tk.END)
        else:
            current = self.pantalla.get()
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, current + valor)

    def calcular_distancia(self,expr):
        coords = re.findall(r"-?\d+(?:\.\d+)?",expr)
        if len(coords) !=4:
            raise ValueError("se requieren 4 numeros para calcular la distancia")
        x1, y1, x2, y2 = map(float, coords)
        return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 4)
                
        
ventana = tk.Tk()
Calculadora = Calculadora(ventana)
ventana.mainloop()
