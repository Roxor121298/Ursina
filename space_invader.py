from ursina import *

app = Ursina()

bullets = []  # List to track bullets

window.size = Vec2(8000, 8000)  # 800x800 pixels
window.fullscreen = False  # Optional: Disable fullscreen to test the square window
window.borderless = False  # Optional: Allow resizing (remove if not needed)

# Configure the camera
camera.orthographic = True
camera.fov = 1000  # Vertical size visible
camera.position = (0, 0, -20)  # Camera position
print('FOV of the camera:', camera.fov)

# Calculate screen boundaries manually
scaling_factor = 0.5  # Adjust this if necessary
min_x, max_x = -camera.fov * scaling_factor, camera.fov * scaling_factor
min_y, max_y = -camera.fov * scaling_factor, camera.fov * scaling_factor

print(f"Horizontal limits: {min_x}, {max_x}")
print(f"Vertical limits: {min_y}, {max_y}")
print(f"Window size (normalized): {window.size}")


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
        cube.x = max(min_x, cube.x - 0.05)  # Left limit
    if held_keys['d']:
        cube.x = min(max_x, cube.x + 0.05)  # Right limit
    if held_keys['w']:
        cube.y = min(max_y, cube.y + 0.05)  # Top limit
    if held_keys['s']:
        cube.y = max(min_y, cube.y - 0.05)  # Bottom limit

def shoot():
    # Create a new bullet at the cube's position
    bullet = Entity(model='cube', color=color.red, scale=(0.1, 0.1, 0.1), position=(cube.x, cube.y, 0))
    bullets.append(bullet)

# Create the main player cube
cube = Entity(model='cube', color=color.orange, scale=(1, 1, 1), position=(0, 0, 0))

app.run()
