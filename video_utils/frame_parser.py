import numpy as np
import cv2
print(cv2.__version__)

IMAGE_IN = 'test-video.mp4'
IMAGE_OUT = 'test_frames/'

def extract_image_frames(path_in, path_out):
    count = 1

    vidcap = cv2.VideoCapture(path_in)
    success,image = vidcap.read()
    success = True

    print(vidcap.isOpened())

    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
        success,image = vidcap.read()
        print('Read frame {}'.format(count))
        cv2.imwrite(path_out + 'frame{}.jpg'.format(count), image)
        count = count + 1

extract_image_frames(IMAGE_IN, IMAGE_OUT)