# 9.1) Open, display, and print image information
from PIL import Image

img = Image.open("image.jpg")   # change to your file name
img.show()
print(f"Size: {img.size}")
print(f"Format: {img.format}")
print(f"Color model: {img.mode}")



# 9.2) Reduced copy (1/3), horizontal & vertical mirror, save
from PIL import Image

img = Image.open("image.jpg")          # original image

# 3‑fold reduced copy
w, h = img.size
reduced = img.resize((w // 3, h // 3))
reduced.save("reduced.jpg")

# horizontal mirror (left‑right)
mirror_h = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_h.save("mirror_h.jpg")

# vertical mirror (top‑bottom)
mirror_v = img.transpose(Image.FLIP_TOP_BOTTOM)
mirror_v.save("mirror_v.jpg")



# 9.3) Apply a filter to 5 images (SHARPEN as example, not blur)
import os
from PIL import Image, ImageFilter

new_folder = "filtered"
os.makedirs(new_folder, exist_ok=True)

for i in range(1, 6):
    with Image.open(f"{i}.jpg") as img:
        filtered = img.filter(ImageFilter.SHARPEN)
        filtered.save(f"{new_folder}/filtered_{i}.jpg")




# 9.4) Add a text watermark to one or multiple images
from PIL import Image, ImageDraw, ImageFont

def add_watermark(img_path, out_path, text="Watermark"):
    img = Image.open(img_path).convert("RGBA")   # ensure alpha for transparency
    # create a transparent overlay
    overlay = Image.new("RGBA", img.size, (255,255,255,0))
    draw = ImageDraw.Draw(overlay)

    # use a default font or a truetype one; here we rely on Pillow default
    font = ImageFont.load_default()
    # choose position (bottom‑right corner with margin)
    text_bbox = draw.textbbox((0,0), text, font=font)
    text_w, text_h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    x = img.size[0] - text_w - 10
    y = img.size[1] - text_h - 10
    draw.text((x, y), text, font=font, fill=(255,255,255,128))  # semi‑transparent white

    watermarked = Image.alpha_composite(img, overlay).convert("RGB")
    watermarked.save(out_path)

# apply to a single image
add_watermark("image.jpg", "watermarked_image.jpg", "© My Watermark")

# apply to multiple images (example for 1.jpg..5.jpg)
for i in range(1, 6):
    add_watermark(f"{i}.jpg", f"watermarked_{i}.jpg", "© My Watermark")