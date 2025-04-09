import qrcode
from qrcode.constants import ERROR_CORRECT_L
from PIL import Image
import random

# === Step 1: Create the fragile QR code (untouched) ===
qr = qrcode.QRCode(
    version=5,
    error_correction=ERROR_CORRECT_L,  # lowest correction
    box_size=10,
    border=4,
)

qr.add_data("cof{you_found_it_wasnt_easy_huh}")
qr.make(fit=True)

# Save the unmodified QR
fragile_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
fragile_img.save("fragile_qr.png")
print("[✔] Saved fragile_qr.png")

# === Step 2: Load it again to make a copy and break it ===
broken_img = Image.open("fragile_qr.png")
pixels = broken_img.load()
width, height = broken_img.size

def erase_block(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if 0 <= i < width and 0 <= j < height:
                pixels[i, j] = (255, 255, 255)

# Delete 50 blocks, each 10–14 px
for i in range(50):
    size = random.randint(10, 14)
    x = random.randint(20, width - size - 20)
    y = random.randint(20, height - size - 20)
    erase_block(x, y, size)
    print(f"[×] Erased block at ({x},{y}) size {size}")

# Save the broken version separately
broken_img.save("broken_qr.png")
print("[⚠] Saved broken_qr.png (damaged)")
