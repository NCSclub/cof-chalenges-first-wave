from stegano import lsb
from PIL import Image

print(lsb.reveal("stego_r.png"))
print(lsb.reveal("stego_g.png"))
print(lsb.reveal("stego_b.png"))