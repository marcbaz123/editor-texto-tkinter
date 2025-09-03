from tkinter import *
from editor import root, texto, monitor, mensaje, ruta, nombre_archivo
from funciones import nuevo, abrir, guardar, guardar_como

# Atajos de teclado
root.bind('<Control-n>', lambda e: nuevo(root, texto, mensaje, ruta, nombre_archivo))
root.bind('<Control-o>', lambda e: abrir(root, texto, mensaje, ruta, nombre_archivo))
root.bind('<Control-s>', lambda e: guardar(root, texto, mensaje, ruta, nombre_archivo, guardar_como))
root.bind('<Control-Shift-S>', lambda e: guardar_como(root, texto, mensaje, ruta, nombre_archivo))
root.bind('<Control-z>', lambda e: texto.edit_undo())
root.bind('<Control-y>', lambda e: texto.edit_redo())
root.bind('<Control-q>', lambda e: root.quit())

# Bucle de aplicación
root.mainloop()
