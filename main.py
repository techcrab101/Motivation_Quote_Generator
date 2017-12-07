import generate_images
import generate_text
import os
import random
import cv2

text_path = 'json.txt'
img_path = 'images/'

phrase = generate_text.make_phrase(text_path)
print(phrase)
list_phrase = phrase.split()

img_path += random.choice(os.listdir(img_path))
print(img_path)

img = cv2.imread(img_path)

img = generate_images.carve_image(img, size = 320)

img = cv2.GaussianBlur(img, (5,5), 0)

char_len = len(phrase)
print(char_len)
print (list_phrase)
print(len(list_phrase))

img =cv2.putText(img=img, text=phrase, org=(200,200),fontFace=3, fontScale=3, color=(0,0,0), thickness=3)
img =cv2.putText(img=img, text=phrase, org=(200,200),fontFace=3, fontScale=3, color=(255,255,255), thickness=1)

cv2.imshow('result', img)
cv2.waitKey(0)
# Pick random image
