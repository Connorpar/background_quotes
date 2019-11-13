# Connor Parish (connorparish9@gmail.com)
# This is a script to make computer backgrounds out of quotes

import random
import time
import csv
import os
import pandas as pd
from pathlib import Path
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


# config
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1280
COLOR = (255, 255, 255)
SPACING = 3

def recommend_font_size(text, img_w, img_h):
    size = 50
    l = len(text)**2

    resize_heuristic = 0.98
    resize_actual = 0.93
    while l > img_w*img_h:
        l = l * resize_heuristic
        size = size * resize_actual

    return int(size)


def select_background_image():
    prefix = "background_images/"
    options = os.listdir(prefix)
    return prefix + random.choice(options)


def select_font():
    prefix = "fonts/"
    options = os.listdir(prefix)
    return prefix + random.choice(options)


def wrap_text(text, w=30):
    new_text = ""
    new_sentence = ""
    for word in text.split(" "):
        delim = " " if new_sentence != "" else ""
        new_sentence = new_sentence + delim + word
        if len(new_sentence) > w:
            new_text += "\n" + new_sentence
            new_sentence = ""
    new_text += "\n" + new_sentence
    return new_text


def write_image(text, output_filename, background_img):
	# setup
	text = wrap_text(text)
	img = Image.new("RGBA", (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255))

	# background
	back = Image.open(background_img, 'r')
	back = back.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
	img_w, img_h = back.size
	bg_w, bg_h = img.size

	offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
	img.paste(back, offset)

	FONT = select_font()
	# print(output_filename + " has " + FONT)
	FONT_SIZE = recommend_font_size(text, img_w, img_h)
	IF = ImageFont.truetype(FONT, FONT_SIZE)

	# text
	font = ImageFont.truetype(FONT, FONT_SIZE)
	draw = ImageDraw.Draw(img)
	img_w, img_h = img.size
	x = img_w / 2
	y = img_h / 2
	textsize = draw.multiline_textsize(text, font=IF, spacing=SPACING)
	text_w, text_h = textsize
	x -= text_w / 2
	y -= text_h / 2
	draw.multiline_text(align="center", xy=(x, y), text=text, fill=COLOR, font=font, spacing=SPACING)
	draw = ImageDraw.Draw(img)

	# output
	img.save(output_filename)

def create_background(quote, author, output_filename):
	# text
	text = quote + " \n -" + author
	write_image(text, output_filename, select_background_image())

if __name__ == '__main__':
	NUM_QUOTES = 8
	OUTPUT_DIR = Path("C:\\Users\\Connor Parish\\Pictures\\Backgrounds")
	used_quotes = []
	
	quotes =  pd.read_csv('./author_quotes.csv')

	for i in range(NUM_QUOTES):
		rand = random.randint(0,len(quotes) - 1)
		if(rand not in used_quotes):
			used_quotes.append(rand)
			f_name = "Output image_" + str(time.time())+ ".png"
			create_background(quotes["Quotes"][rand], quotes["Authors"][rand], OUTPUT_DIR / f_name)


