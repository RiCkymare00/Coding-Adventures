from PIL import Image

density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'.                                "

image = Image.open("bazza.jpeg")
width = int(image.size[0])
height = int(image.size[1])
resized_image = image.resize((width, height))
ascii_art = ''

for y in range(height):
    for x in range(width):
        pixel_value = image.getpixel((x,y))
        pixel_opacity = int((pixel_value[0] + pixel_value[1] + pixel_value[2])/3)
        #char_index = int((1 - pixel_opacity / 256) * len(density) - 1)
        char_index = int((pixel_opacity / 256) * len(density))
        ascii_char = density[char_index]
        ascii_art += ascii_char
    ascii_art += '\n'

print(ascii_art)