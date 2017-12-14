import generate_images
import generate_text
import os
import random
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

new_list_phrase = ''
for i, phrase in enumerate(list_phrase):
    s = ''
    if i % 3 == 0 and i != 0:
        s = '\n'
    new_list_phrase += phrase +' ' + s

print('phrase length:', len(list_phrase))

font_size = ( 1 / char_len ) * 100

font_size = 3 if font_size > 3 else font_size

print('font size:', font_size)

print()
print(new_list_phrase)

img =cv2.putText(img=img, text=new_list_phrase, org=(200,200),fontFace=3, fontScale=font_size, color=(0,0,0), thickness=3)
img =cv2.putText(img=img, text=new_list_phrase, org=(200,200),fontFace=3, fontScale=font_size, color=(255,255,255), thickness=1)

cv2.imshow('result', img)
cv2.waitKey(0)
# Pick random image
