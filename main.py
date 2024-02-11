import tkinter as tk
from configuracion_canvas import configurar_canvas, zonas
from eventos import en_click_canvas

def main():
    ventana_principal = tk.Tk()
    ventana_principal.geometry("600x800")
    ventana_principal.title("Roomba")

    canvas = configurar_canvas(ventana_principal)
    #escuchador de ventos para comprobar si el usuario ha pulsado en la zona y llamar a la función principal que muestra el tiempo estimado de limpieza
    canvas.bind("<Button>", lambda event: en_click_canvas(event, ventana_principal))

    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
