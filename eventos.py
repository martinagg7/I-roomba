import tkinter as tk
from configuracion_canvas import zonas

#  para que sea más fácil la velocidad de limpieza de roomba es de 1000 cm² por minuto 
velocidad_limpieza = 1000  

"función que nos permite que cuando señalemos una zona se abra una ventana con el area de esta y el tiempo estimado de limpieza"
def abrir_info_zona(zona, ventana_principal):
    tiempo_limpieza = zonas[zona]['area'] / velocidad_limpieza
    ventana_info = tk.Toplevel(ventana_principal)
    ventana_info.title(zona)
    tk.Label(ventana_info, text=f"Zona: {zona}").pack()
    tk.Label(ventana_info, text=f"Área: {zonas[zona]['area']} cm²").pack()
    tk.Label(ventana_info, text=f"Tiempo estimado de limpieza: {tiempo_limpieza:.2f} minutos").pack()

"función para comprobar en que zona está pulsado exctamente el usario"
def en_click_canvas(evento, ventana_principal):
    x, y = evento.x, evento.y
    for zona, info in zonas.items():
        x1, y1, x2, y2 = info['coordenadas']
        if x1 < x < x2 and y1 < y < y2:
            abrir_info_zona(zona, ventana_principal)
            break
