from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO
from haiku_gen import return_haiku, generate_image
from set_wallpaper import set_wallpaper
import numpy as np

# Set to True to return fixed values instead of querying openai api
test_status = False

# List of three lines of Haiku
haiku = return_haiku(test=test_status)

# Url for image generated
image_url = generate_image(haiku, test=test_status)

# Open image with pillow
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)

# Crop image to aspect ratio
aspect_ratio = (16,9)

I = np.asarray(img)
img_dim = I.shape[0] # Image from openai is square so this is both height and width
vertical_margin = int((img_dim - ((img_dim / aspect_ratio[0]) * aspect_ratio[1])) / 2)
I_crop = I[vertical_margin:img_dim-vertical_margin, 0:img_dim]

# Resize image to desktop dimensions
im = Image.fromarray(np.uint8(I_crop))
im_resized = im.resize((2880,1800))
I_resized = np.asarray(im_resized)
draw_cropped = ImageDraw.Draw(im_resized)

# get new height and width dimensions of resized image
height = I_resized.shape[0]
width = I_resized.shape[1]

# Set font
font = ImageFont.truetype(r"hikoo-desktop\fonts\PoetsenOne-Regular.ttf", width*0.05)

# Draw each line of Haiku, draw as text with a 'shadow'
for n, line in enumerate(haiku):
    offset = (width*0.06)*n # Moves each line down an amount
    v_padding = height*0.3
    h_padding = width*0.04
    draw_cropped.text((width-h_padding-2, height+offset-v_padding+2),line,(12,61,25),font=font,anchor='rb')
    draw_cropped.text((width-h_padding, height+offset-v_padding),line,(255,255,255),font=font,anchor='rb')

# Save the image
image_path = "hikoo-desktop\images\dailyHaikuImage.png"
im_resized.save(image_path)

# Set windows background
set_wallpaper(image_path)