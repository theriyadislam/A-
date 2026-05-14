# Task1
import requests
from PIL import Image
from io import BytesIO

# 1. Download an image (use any postcard URL)
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunset_at_Sant_Antoni.jpg/800px-Sunset_at_Sant_Antoni.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# 2. Crop: (left, upper, right, lower) – adjust to your needs
cropped = img.crop((100, 50, 700, 400))

# 3. Save to current folder with a new name
cropped.save("postcard_cropped.jpg")
print("Cropped image saved as 'postcard_cropped.jpg'")



# Task2
from PIL import Image

# Dictionary: holiday -> file name (adjust paths to your images)
cards = {
    "Christmas": "christmas.jpg",
    "New Year": "newyear.jpg",
    "Easter": "easter.jpg"
}

holiday = input("Which holiday do you need a postcard for? ")
filename = cards.get(holiday)

if filename:
    img = Image.open(filename)
    img.show()          # opens the image with the default viewer
else:
    print("Sorry, no card for that holiday.")



# Task3
from PIL import Image, ImageDraw, ImageFont

# --- Reuse the dictionary from Task 10.2 ---
cards = {
    "Christmas": "christmas.jpg",
    "New Year": "newyear.jpg",
    "Easter": "easter.jpg"
}

holiday = input("Which holiday? ")
name = input("Who do you want to congratulate? ")

filename = cards.get(holiday)
if not filename:
    print("Holiday not found.")
    exit()

# Load the postcard
img = Image.open(filename).convert("RGBA")
W, H = img.size
draw = ImageDraw.Draw(img)

# --- Choose bold and regular fonts ---
# Try common bold font paths (Windows / Linux); fallback to default
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 60)          # Arial Bold (Windows)
except:
    try:
        font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)  # Linux
    except:
        font_bold = ImageFont.load_default()

try:
    font_normal = ImageFont.truetype("arial.ttf", 50)
except:
    font_normal = ImageFont.load_default()

# --- Build the message with two different styles ---
message1 = f"{name},"
message2 = "congratulations!"

# Measure text widths (approximate for centering)
bbox1 = draw.textbbox((0,0), message1, font=font_bold)
bbox2 = draw.textbbox((0,0), message2, font=font_normal)
w1, h1 = bbox1[2]-bbox1[0], bbox1[3]-bbox1[1]
w2, h2 = bbox2[2]-bbox2[0], bbox2[3]-bbox2[1]

total_w = w1 + w2
# Position at bottom-centre
x = (W - total_w) // 2
y = H - max(h1, h2) - 40   # 40px from bottom

# Draw the two parts (different colours & fonts)
draw.text((x, y), message1, fill=(255,0,0,255), font=font_bold)   # red, bold
draw.text((x + w1, y), message2, fill=(0,0,255,255), font=font_normal)  # blue, regular

# Save as PNG
output_name = f"congratulations_{name}.png"
img.save(output_name)
print(f"Saved as '{output_name}'")


