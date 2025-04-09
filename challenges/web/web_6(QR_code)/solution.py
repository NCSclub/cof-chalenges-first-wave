from PIL import Image

# Open the broken QR code image
img = Image.open("broken_qr.png").convert("RGB")
pixels = img.load()

# Coordinates and block sizes of erased areas
restoration_blocks = [
    (385, 268, 14), (357, 215, 11), (363, 185, 12), (223, 285, 12), (238, 335, 13),
    (194, 274, 14), (353, 26, 12), (307, 305, 10), (50, 264, 11), (291, 336, 11),
    (216, 106, 11), (301, 403, 13), (230, 305, 10), (279, 133, 12), (124, 357, 12),
    (164, 290, 14), (304, 105, 11), (258, 403, 12), (20, 187, 12), (114, 88, 11),
    (24, 160, 13), (260, 44, 12), (254, 221, 10), (113, 267, 11), (99, 392, 13),
    (348, 180, 14), (223, 211, 12), (348, 388, 11), (25, 150, 10), (398, 360, 11),
    (235, 29, 13), (88, 196, 13), (402, 382, 13), (29, 391, 13), (329, 316, 11),
    (306, 230, 11), (344, 160, 12), (288, 235, 12), (79, 321, 13), (211, 369, 12),
    (92, 154, 11), (419, 78, 10), (414, 312, 11), (335, 275, 13), (123, 377, 12),
    (193, 31, 11), (119, 34, 14), (263, 253, 10), (36, 117, 14), (166, 309, 11),
]

# Restore each block to black
for x, y, size in restoration_blocks:
    for i in range(x, x + size):
        for j in range(y, y + size):
            pixels[i, j] = (0, 0, 0)  # black

# Save the restored image
img.save("restored_qr.png")
print("[✔] QR code restored and saved as restored_qr.png")
