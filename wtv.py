from ursina import *

app = Ursina()

bullets = []  # List to track bullets

window.size = Vec2(8000, 8000)  # 800x800 pixels
window.fullscreen = False  # Optional: Disable fullscreen to test the square window
window.borderless = False  # Optional: Allow resizing (remove if not needed)

# Configure the camera
camera.orthographic = True
camera.fov = 100  # Vertical size visible
camera.position = (0, 0, -20)  # Camera position


# Calculate screen boundaries manually
scaling_factor = 0.5  # Adjust this if necessary
min_x, max_x = -camera.fov * scaling_factor, camera.fov * scaling_factor
min_y, max_y = -camera.fov * scaling_factor, camera.fov * scaling_factor



def update():
    move()

    # Fire bullets when the space key is pressed
    if held_keys['space']:
        shoot()

    # Update bullets
    for bullet in bullets[:]:
        bullet.y += 0.2
        if bullet.y > max_y:  # Remove bullet if it leaves the screen
            bullets.remove(bullet)
            destroy(bullet)

def move():
    # Constrain the cube's movement to within the screen boundaries
    if held_keys['a']:
        cube.x = max(-(max_x*1.7), cube.x - 0.5)  # Left limit
    if held_keys['d']:
        cube.x = min(max_x*1.7, cube.x + 0.5)  # Right limit
    if held_keys['w']:
        cube.y = min(max_y, cube.y + 0.5)  # Top limit
    if held_keys['s']:
        cube.y = max(min_y, cube.y - 0.5)  # Bottom limit

def shoot():
    # Create a new bullet at the cube's position
    bullet = Entity(model='cube', color=color.red, scale=(0.1, 0.1, 0.1), position=(cube.x, cube.y, 0))
    bullets.append(bullet)

# Create the main player cube
texture = load_texture('../image/greenbaron.png')
if not texture:
    print("Failed to load texture: green_barong.png")


cube = Entity(model='quad', texture=texture, scale=(1, 1, 1), position=(0, 0, 0))


app.run()
