from PIL import Image

# Open the image
img = Image.open("rudra.jpg")

# Convert the image to RGB if it is not already in RGB format
img = img.convert("RGB")


# Get the dimensions of the image
width, height =img.size

# Define a function to convert brightness to ASCII character
def brightness_to_ascii(brightness):
    if brightness == 0:
        return "."
    elif 1 <= brightness <= 50:
        return "]"
    elif 51 <= brightness <= 100:
        return "*"
    elif 101 <= brightness <= 150:
        return "0"
    elif 151 <= brightness <= 200:
        return "$"
    else:
        return "#"

# Loop through each pixel in the image
for y in range(height):
    for x in range(width):
        # Get the RGB values of the pixel
        r, g, b = img.getpixel((x, y))
        
        # Calculate the brightness
        brightness = (r + g + b) // 3
        
        # Convert brightness to ASCII character and print
        print(brightness_to_ascii(brightness), end="")
    
    # Move to the next line after each row
    print()

