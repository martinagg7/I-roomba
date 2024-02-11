import tkinter as tk

# estas son las distntas zonas con sus medidas
zonas = {
    'Zona 1': {'coordenadas': (0, 0, 500, 150), 'color': 'light green', 'area': 500 * 150},
    'Zona 2': {'coordenadas': (0, 150, 101, 630), 'color': 'orange', 'area': 480 * 101},
    'Zona 3': {'coordenadas': (191, 150, 500, 630), 'color': 'blue', 'area': 309 * 480},
    'Zona 4': {'coordenadas': (101, 410, 191, 630), 'color': 'purple', 'area': 90 * 220},
}
# se crea la ventana principal donde se mostrarán estas zonas
def configurar_canvas(ventana_principal):
    canvas = tk.Canvas(ventana_principal, width=500, height=630, bg='white')
    canvas.pack()

    # creamos un rectángulo para cada zona pasándoles las medidas
    for zona, info in zonas.items():
        canvas.create_rectangle(*info['coordenadas'], fill=info['color'], outline='black')

    # el mueble
    mueble_coords = (101, 150, 191, 410)
    canvas.create_rectangle(*mueble_coords, fill='brown', outline='black')

    #  nombre para cada zona
    for zona, info in zonas.items():
        x1, y1, x2, y2 = info['coordenadas']
        canvas.create_text(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2, text=zona)

    # mueble
    canvas.create_text((mueble_coords[0] + mueble_coords[2]) / 2, 
                       (mueble_coords[1] + mueble_coords[3]) / 2, 
                       text='Mueble', 
                       fill='white')
    
    return canvas
