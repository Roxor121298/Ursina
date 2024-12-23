
# pip install ursina
from ursina import *

app = Ursina()

bullets = [];


# fonction de base pour le tick (ursina)
def update():
    # pour les keytagging
    if held_keys['a']:  
        cube.x -= 0.05
    if held_keys['d']:  
        cube.x += 0.05
    if held_keys['w']:
        cube.y += 0.05
    if held_keys['s']:
        cube.y -= 0.05

    if held_keys['space']:
        shoot();

    for bullet in bullets:
        bullet.y += 0.2
        if bullet.y > 6:
            bullets.remove(bullet)
            # ne pas oublier de destroy les object pas jsute de les enlever
            # pas de trash collector automatic
            destroy(bullet)

def shoot():
    bullet = Entity(model='cube', color=color.red, scale=(0.1,0.1,0.1), position=(cube.x, cube.y, 0))
    bullets.append(bullet)

cube = Entity(model='cube', color=color.orange, scale=(1, 1, 1), position=(0, 0, 0))


app.run()
