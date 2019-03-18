import generate_images
import generate_text
import os
import random
import math
import cv2

text_path = 'json.txt'
img_dir = 'images/'

phrase = generate_text.make_phrase(text_path)

print('\n' + phrase + '\n')

list_phrase = phrase.split()

img_path = random.choice(os.listdir(img_dir))

print('Image path:' , img_dir + img_path + '\n')

img = cv2.imread(img_dir + img_path)

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

max_font = 2
min_font = 1

font_size = (1 / (1+(math.e**( 0.1 * (char_len - 50 ))))) * (max_font - min_font) + min_font

print('font size:', font_size)

print()
print(new_list_phrase)

# new_list_phrase += '\n#staywoke'

x0 = 50
tolerance_x0 = 0.1
if abs(font_size - 1) < tolerance_x0:
    x0 = 10

y0, dy = 50, 50
for i, line in enumerate(new_list_phrase.split('\n')):
    y = y0 + i*dy
    y = int(y * font_size)
    cv2.putText(img=img, text=line, org=(x0,y),fontFace=3, fontScale=font_size, color=(0,0,0), thickness=4)
    cv2.putText(img=img, text=line, org=(x0,y),fontFace=3, fontScale=font_size, color=(255,255,255), thickness=2)

cv2.imshow('result', img)
cv2.waitKey(0)

while True:
    y = input('Do you want to save the image (y/n) ')
    
    if y in ['y', 'Y', 'Yes', 'yes', 'true', 'True']:
        cv2.imwrite('Messages/' + img_path + 'motivational_img.jpg', img)
        break
    elif y in ['n', 'N', 'no', 'No', 'NO', 'False', 'false']:
        break

