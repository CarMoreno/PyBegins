"""Asi hacemos que nuestro proyecto Django no dependa del sitio donde se cree
y lo podamos mover de carpeta las veces que queramos hacerlo"""
import os
import Image
import webbrowser


name = os.path.join(os.path.dirname(__file__), "python.bmp").replace('\\', '/')
# name = "C:\Users\Carlos\Desktop\Python\\python.bmp"
img = webbrowser.open(name)
#img.show()
# otraBase = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print base
print name