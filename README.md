Editor de Texto en Python con Tkinter

Este proyecto es un editor de texto desarrollado en Python utilizando la librería estándar Tkinter.
El objetivo es contar con un programa ligero, funcional y fácil de usar, que sirva tanto como herramienta práctica como también de ejemplo en el desarrollo de interfaces gráficas con Python.

Funcionalidades principales

Gestión de archivos:

Crear un nuevo archivo

Abrir un archivo existente

Guardar

Guardar como

Edición de texto:

Deshacer (Ctrl+Z)

Rehacer (Ctrl+Y)

Cortar (Ctrl+X)

Copiar (Ctrl+C)

Pegar (Ctrl+V)

Eliminar selección

Soporte de temas: Claro, Oscuro y Sistema

Atajos de teclado para mejorar la productividad

Barra de estado inferior que muestra el nombre del archivo activo

Requisitos

Python 3.x

Tkinter (incluido en la instalación estándar de Python en la mayoría de los sistemas)

Instalación y uso

Clonar el repositorio:

git clone https://github.com/marcbaz123/editor-texto-tkinter.git
cd editor-texto-tkinter


Ejecutar el programa:

python main.py


El editor se abrirá con todas las funcionalidades disponibles.

Atajos de teclado

Ctrl + N: Nuevo archivo

Ctrl + O: Abrir archivo

Ctrl + S: Guardar

Ctrl + Shift + S: Guardar como

Ctrl + Z: Deshacer

Ctrl + Y: Rehacer

Ctrl + Q: Salir

Detalles técnicos relevantes

El proyecto se apoya en algunas características clave de Tkinter:

Text(root, undo=True): habilita la funcionalidad de deshacer y rehacer en el área de texto.

texto.edit_undo() y texto.edit_redo(): permiten revertir o repetir cambios en el texto.

texto.event_generate("<<Cut>>"), "<<Copy>>" y "<<Paste>>": generan eventos propios de Tkinter para manejar las operaciones de portapapeles de manera nativa.

Uso de Menu con tearoff=0 para generar menús desplegables profesionales sin la opción de "separar" el menú.

Implementación de temas mediante una función aplicar_tema que modifica dinámicamente colores de interfaz y del área de texto.
