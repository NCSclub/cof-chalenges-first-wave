from PIL import Image

# Flag to encode
flag = "cof{colors_are_codes}"

# Pad flag so length is multiple of 3
while len(flag) % 3 != 0:
    flag += " "  # Add space as padding

# Create a list of RGB tuples
colors = []
for i in range(0, len(flag), 3):
    r = ord(flag[i])
    g = ord(flag[i+1])
    b = ord(flag[i+2])
    colors.append((r, g, b))

# Image size: 1 row of color blocks
img_width = len(colors)
img_height = 1

img = Image.new("RGB", (img_width, img_height))

# Set each pixel to its color
for x, color in enumerate(colors):
    img.putpixel((x, 0), color)

# Save image
img = img.resize((img_width * 50, img_height * 50), resample=Image.NEAREST)
img.save("color_flag.png")

print("✅ Image created: color_flag.png")
