from ursina import *
import math

app = Ursina()

bullets = []  # List to track bullets
bullet_speed = 2  # Speed of the bullets

window.size = Vec2(800, 800)  # 800x800 pixels
window.fullscreen = False  # Optional: Disable fullscreen to test the square window
window.borderless = False  # Optional: Allow resizing (remove if not needed)

# Configure the camera
camera.orthographic = True
camera.fov = 50  # Vertical size visible
camera.position = (0, 0, -20)  # Camera position

# Calculate screen boundaries manually
scaling_factor = 0.5  # Adjust this if necessary
min_x, max_x = -camera.fov * scaling_factor, camera.fov * scaling_factor
min_y, max_y = -camera.fov * scaling_factor, camera.fov * scaling_factor

# Create the main character
texture = load_texture('../image/greenbaron.png')  # Replace with your texture path
greenBaron = Entity(model='quad', texture=texture, scale=(1, 1), position=(0, 0))


def update():
    move()
    point(greenBaron)

    # Fire bullets when the space key is pressed
    if held_keys['space']:
        shoot()

    # Update bullets
    for bullet in bullets[:]:
        # Move the bullet in its stored direction
        bullet.x += bullet.direction[0] * bullet_speed
        bullet.y += bullet.direction[1] * bullet_speed

        # Remove bullet if it leaves the screen
        if bullet.x < (min_x*1.7) or bullet.x > (max_x*1.7) or bullet.y < min_y or bullet.y > max_y:
            bullets.remove(bullet)
            destroy(bullet)


def move():
    # Constrain the greenBaron movement to within the screen boundaries
    if held_keys['a']:
        greenBaron.x = max(-(max_x * 1.5), greenBaron.x - 0.5)  # Left limit
    if held_keys['d']:
        greenBaron.x = min(max_x * 1.5, greenBaron.x + 0.5)  # Right limit
    if held_keys['w']:
        greenBaron.y = min(max_y, greenBaron.y + 0.5)  # Top limit
    if held_keys['s']:
        greenBaron.y = max(min_y, greenBaron.y - 0.5)  # Bottom limit


def point(target):
    mouse_pos = mouse.position
    dx = mouse_pos.x
    dy = mouse_pos.y
    angle = math.degrees(math.atan2(dy, dx))  # Calculate angle in degrees
    target.rotation_z = -(angle) + 90


def shoot():
    mouse_pos = mouse.position
    # Calculate the direction vector
    dx = mouse_pos.x
    dy = mouse_pos.y
    direction = (dx , dy)

    # Create a new bullet at the greenBaron's position
    bullet = Entity(model='sphere', color=color.red, scale=0.2, position=(greenBaron.x, greenBaron.y, 0))
    bullet.direction = direction  # Store the direction vector in the bullet
    bullets.append(bullet)


app.run()
