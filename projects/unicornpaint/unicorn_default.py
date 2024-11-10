import unicornhat as unicorn
import random
import time

# Set your default configuration
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

# Get the width and height of the Unicorn HAT
width, height = unicorn.get_shape()

def random_sparkles():
    while True:
        # Randomly select a pixel position
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        
        # Randomly select a color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        # Set the pixel to the random color
        unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()
        
        # Briefly display the sparkle
        time.sleep(0.1)
        
        # Turn off the pixel
        unicorn.set_pixel(x, y, 0, 0, 0)
        unicorn.show()
        #comment
        

# Run the random sparkles function