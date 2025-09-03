from tkinter import *
from funciones import nuevo, abrir, guardar, guardar_como, aplicar_tema

# Variables globales como listas
ruta = [""]
nombre_archivo = ["Nuevo archivo"]

# Configuración raíz
root = Tk()
root.title("Editor de texto")
texto = Text(root, undo=True)  # Area de texto que habilita undo/redo
texto.pack(fill=BOTH, expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = StringVar()
mensaje.set(f"{nombre_archivo[0]} - Editor de texto hecho por Marcelo Bazán")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

# Menú superior
menubar = Menu(root)
root.config(menu=menubar)

# Menú Archivo
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=lambda: nuevo(root, texto, mensaje, ruta, nombre_archivo))
filemenu.add_command(label="Abrir", command=lambda: abrir(root, texto, mensaje, ruta, nombre_archivo))
filemenu.add_command(label="Guardar", command=lambda: guardar(root, texto, mensaje, ruta, nombre_archivo, guardar_como))
filemenu.add_command(label="Guardar como", command=lambda: guardar_como(root, texto, mensaje, ruta, nombre_archivo))
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

#Menu 
edicionmenu = Menu(menubar, tearoff=0)
edicionmenu.add_command(label="Deshacer -- ctrl + z ", command=texto.edit_undo)
edicionmenu.add_command(label="Rehacer -- ctrl + y", command=texto.edit_redo)
edicionmenu.add_separator()
edicionmenu.add_command(label="Cortar -- ctrl + x", command=lambda: texto.event_generate("<<Cut>>"))
edicionmenu.add_command(label="Copiar -- ctrl + c", command=lambda: texto.event_generate("<<Copy>>"))
edicionmenu.add_command(label="Pegar -- ctrl + v", command=lambda: texto.event_generate("<<Paste>>"))
edicionmenu.add_command(label="Eliminar", command=lambda: texto.delete(SEL_FIRST, SEL_LAST))
menubar.add_cascade(menu=edicionmenu, label="Edición")

# Menú Tema
temamenu = Menu(menubar, tearoff=0)
temamenu.add_command(label="Claro", command=lambda: aplicar_tema(root, texto, monitor, "Claro"))
temamenu.add_command(label="Oscuro", command=lambda: aplicar_tema(root, texto, monitor, "Oscuro"))
temamenu.add_command(label="Sistema", command=lambda: aplicar_tema(root, texto, monitor, "so"))
menubar.add_cascade(menu=temamenu, label="Tema")
