

import tkinter as tk

class calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("calculadora")
        self.ventana.configure(bg="blue")
        
        self.pantalla = tk.Entry(self.ventana, width=50, bg="lightblue", borderwidth=5, fg="black")
        self.pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        
        self.crear_botones()
   
    def crear_botones(self):
        botones = [
            ("1",1,0), ("2",1,1), ("3",1,2),
            ("4",2,0), ("5",2,1), ("6",2,2),
            ("7",3,0), ("8",3,1), ("9",3,2),
            ("0",4,0), ("+",1,3), ("-",2,3),
            ("*",3,3), ("/",4,3), ("=",4,1),
            ("c",4,2)
        ]
        
        for(text, row, column) in botones:
            button = tk.Button(self.ventana, text=text, bg="lightblue",fg="black", padx=30, pady=30, command=lambda t=text: self.boton_click(t))
            button.grid(row=row, column=column)
                
    def boton_click(self, valor):
        if valor == "=":
            try:
                result = str(eval(self.pantalla.get()))
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, result)
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error")

        elif valor == "c":
            self.pantalla.delete(0, tk.END)
        else:
            current = self.pantalla.get()
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, current + valor)
                
        
ventana = tk.Tk()
calculadora = calculadora(ventana)
ventana.mainloop()
