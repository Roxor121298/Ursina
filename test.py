from ursina import *

app = Ursina()

# Configuration de la caméra pour une vue orthographique
camera.orthographic = True
camera.fov = 10  # Taille verticale visible
camera.position = (0, 0, -2)  # Positionner la caméra

cube = Entity(model='cube', color=color.orange, scale=(1, 1, 1), position=(0, 0, 0))

app.run()
