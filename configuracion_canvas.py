import tkinter as tk

# Aquí definimos las zonas globales para poder acceder desde otros módulos
zonas = {
    'Zona 1': {'coordenadas': (0, 0, 500, 150), 'color': 'light green', 'area': 500 * 150},
    'Zona 2': {'coordenadas': (0, 150, 101, 630), 'color': 'orange', 'area': 480 * 101},
    'Zona 3': {'coordenadas': (191, 150, 500, 630), 'color': 'blue', 'area': 309 * 480},
    'Zona 4': {'coordenadas': (101, 410, 191, 630), 'color': 'purple', 'area': 90 * 220},
}

def configurar_canvas(ventana_principal):
    canvas = tk.Canvas(ventana_principal, width=500, height=630, bg='white')
    canvas.pack()
    dibujar_zonas(canvas)
    dibujar_mueble(canvas)
    return canvas

def dibujar_zonas(canvas):
    for zona, info in zonas.items():
        canvas.create_rectangle(*info['coordenadas'], fill=info['color'], outline='black')
        # Añadir nombre de la zona
        x1, y1, x2, y2 = info['coordenadas']
        canvas.create_text(x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2, text=zona)

def dibujar_mueble(canvas):
    coordenadas_mueble = (101, 150, 191, 410)
    canvas.create_rectangle(*coordenadas_mueble, fill='brown', outline='black')
    # Añadir nombre del mueble
    canvas.create_text(
        (coordenadas_mueble[0] + coordenadas_mueble[2]) / 2,
        (coordenadas_mueble[1] + coordenadas_mueble[3]) / 2,
        text='Mueble',
        fill='white'
    )
