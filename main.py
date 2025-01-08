from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO
from haiku_gen import *
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
im = Image.fromarray(np.uint8(I_crop))

# get new height and width dimensions of cropped image
height = I_crop.shape[0]
width = I_crop.shape[1]

draw_cropped = ImageDraw.Draw(im)

# Set font
font = ImageFont.truetype("hikoo-desktop\PoetsenOne-Regular.ttf", 50)

# Draw each line of Haiku, draw as text with a 'shadow'
for n, line in enumerate(haiku):
    offset = 60*n # Moves each line down an amount
    v_padding = 200
    h_padding = 50
    draw_cropped.text((width-h_padding-2, height+offset-v_padding+2),line,(12,61,25),font=font,anchor='rb')
    draw_cropped.text((width-h_padding, height+offset-v_padding),line,(255,255,255),font=font,anchor='rb')

# Save the image
im.save('hikoo-desktop/images/dailyHaikuImage.png')

