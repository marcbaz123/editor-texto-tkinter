from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox

# Funciones del editor de texto

# Nueva función para crear un nuevo archivo
def nuevo(root, texto, mensaje, ruta, nombre_archivo):
    mensaje.set("Nuevo archivo")
    ruta[0] = ""
    nombre_archivo[0] = "Nuevo archivo"
    texto.delete(1.0, "end")
    root.title("Editor de texto")

# Función para abrir un archivo existente
def abrir(root, texto, mensaje, ruta, nombre_archivo):
    ruta_local = FileDialog.askopenfilename(
        initialdir=".",
        filetypes=(("Archivos de texto","*.txt"),),
        title="Abrir archivo de texto"
    )
    if ruta_local != "":
        with open(ruta_local, 'r') as archivo:
            contenido = archivo.read()
        texto.delete(1.0, "end")
        texto.insert(1.0, contenido)
        ruta[0] = ruta_local
        nombre_archivo[0] = ruta_local.replace("\\", "/").split("/")[-1]
        root.title(ruta_local + " Editor de texto")
        mensaje.set(f"{nombre_archivo[0]}  --   Editor de texto hecho por Marcelo Bazán")

# Función para guardar el archivo actual
def guardar(root, texto, mensaje, ruta, nombre_archivo, guardar_como_func):
    mensaje.set("Guardar archivo")
    if ruta[0] != "":
        contenido = texto.get(1.0, "end-1c")
        with open(ruta[0], "w+") as archivo:
            archivo.write(contenido)
        nombre_archivo[0] = ruta[0].replace("\\", "/").split("/")[-1]
        MessageBox.showinfo(nombre_archivo[0], "Se ha guardado correctamente")
        mensaje.set(f"Se ha guardado {nombre_archivo[0]}  --   Editor de texto hecho por Marcelo Bazán")
    else:
        guardar_como_func(root, texto, mensaje, ruta, nombre_archivo)
# Función para guardar el archivo con un nuevo nombre
def guardar_como(root, texto, mensaje, ruta, nombre_archivo):
    mensaje.set("Guardar archivo como...")
    archivo = FileDialog.asksaveasfilename(title="Guardar archivo", defaultextension=".txt")
    if archivo:
        ruta[0] = archivo
        contenido = texto.get(1.0, "end-1c")
        with open(ruta[0], "w+") as f:
            f.write(contenido)
        nombre_archivo[0] = ruta[0].replace("\\", "/").split("/")[-1]
        MessageBox.showinfo(nombre_archivo[0], "Se ha guardado correctamente")
        mensaje.set(f"Se ha guardado {nombre_archivo[0]}  --   Editor de texto hecho por Marcelo Bazán")
    else:
        mensaje.set("Guardado cancelado")
 # Función para aplicar temas al editor
def aplicar_tema(root, texto, monitor, nombre):
    temas = {
        "Claro": {"bg": "white", "fg": "black", "insertbackground": "black"},
        "Oscuro": {"bg": "#242424", "fg": "#dcdcdc", "insertbackground": "white"},
        "so": {"bg": root.cget("bg"), "fg": "black", "insertbackground": "black"}
    }
    tema = temas[nombre]
    texto.config(bg=tema["bg"], fg=tema["fg"], insertbackground=tema["insertbackground"])
    root.config(bg=tema["bg"])
    if nombre == "Oscuro":
        monitor.config(bg="#1e1e1e", fg="#dcdcdc")
    elif nombre == "Claro":
        monitor.config(bg="#c9c9c9", fg="black")
    else:
        monitor.config(bg=root.cget("bg"), fg="black")
