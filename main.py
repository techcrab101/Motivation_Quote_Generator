import generate_images
import generate_text
import os
import random
import math
import cv2

text_path = 'json.txt'
img_path = 'images/'

phrase = generate_text.make_phrase(text_path)

print('\n' + phrase + '\n')

list_phrase = phrase.split()

img_path += random.choice(os.listdir(img_path))

print('Image path:' , img_path + '\n')

img = cv2.imread(img_path)

img = generate_images.carve_image(img, size = 320)

img = cv2.GaussianBlur(img, (5,5), 0)

char_len = len(phrase)

print('\n' + 'char length: ' + str(char_len))
print(list_phrase)


text_block_width = math.sqrt(char_len) * 2

print('\n' + 'char width: ' + str(text_block_width))

new_list_phrase = ''
current_phrase_size = 0
tolerance = 5
for i, phrase in enumerate(list_phrase):
    current_phrase_size += len(phrase)
    s = ''
    if abs(text_block_width - current_phrase_size) < tolerance:
        s = '\n'
        current_phrase_size = 0
    new_list_phrase += phrase +' ' + s

print('phrase length:', len(list_phrase))

font_size = ( 1 / char_len ) * 150

font_size = 2 if font_size > 2 else font_size

print('font size:', font_size)

print()
print(new_list_phrase)

new_list_phrase += '\n#staywoke'

y0, dy = 50, 50
for i, line in enumerate(new_list_phrase.split('\n')):
    y = y0 + i*dy
    y = int(y * font_size)
    cv2.putText(img=img, text=line, org=(50,y),fontFace=3, fontScale=font_size, color=(0,0,0), thickness=4)
    cv2.putText(img=img, text=line, org=(50,y),fontFace=3, fontScale=font_size, color=(255,255,255), thickness=2)

cv2.imshow('result', img)
cv2.waitKey(0)
# Pick random image
