import os
import cv2
import imutils
import uuid
import time

username = input('Username: ')

id = uuid.getnode()

max_height_or_width = 900


images_directory = './images'

filenames = sorted([f for f in os.listdir(images_directory) if ([f.lower().endswith(ext) for ext in ('jpg', 'png', 'jpeg', 'bmp')])])

# for image_filename in filenames:
image_index = 0

try: 
    with open('labels.txt', 'r', encoding='utf8') as f:
        labels_lines = [i.split('\t') for i in f.readlines() if i != '\n']
except Exception as e:
    labels_lines = []

if len(labels_lines) == 0:
    print('First run, starting from 0th image')
else:
    filename_continue_from = labels_lines[-1][0]
    index_continue_from = len(labels_lines) - 1
    print('Continuing from after index %s (filename: %s)' % (index_continue_from + 1, filename_continue_from))
    image_index = index_continue_from + 1

while True: 
    if image_index < 0:
        image_index = 0
    if image_index == len(filenames):
        print("Done!")
        break
    print('current image / total number of images: %s / %s' % (image_index + 1, len(filenames) + 1))
    image_filename = filenames[image_index]
    
    if image_filename in [i[0] for i in labels_lines]:
        print('[WARNING] Image label exists')

    full_filename = os.path.join(images_directory, image_filename)
    image = cv2.imread(full_filename)
    height, width, _ = image.shape
    image = imutils.resize(image, width=max_height_or_width) if height < width else imutils.resize(image, height=max_height_or_width)

    cv2.imshow(full_filename, image)
    key_value = cv2.waitKey(0)
    cv2.destroyAllWindows()

    # ! score selection
    if key_value in [ord(str(i)) for i in [0, 1, 2, 3, 4, 5]]: 
        print("[LABEL] Score: %s (%s)" % (key_value, image_filename))
        with open('labels.txt', 'a', encoding='utf8') as f:
            f.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (image_filename, chr(key_value), id, username, round(time.time() * 1000), image_index))
        image_index += 1
                
    # ! previous image 
    elif key_value == ord('a'):
        print("Go to previous image")
        image_index -= 1
        
    # ! next image
    elif key_value == ord('d'):
        print("Go to next image")
        image_index += 1
    
    elif key_value == ord('q'):
        print("Quit")
        break
