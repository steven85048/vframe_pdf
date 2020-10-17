import pafy
import cv2

IMAGE_IN = 'test-video.mp4'
IMAGE_OUT = 'test_frames/'

test_youtube_vid = 'https://www.youtube.com/watch?v=DNMO-MdmO6g&ab_channel=HiroshiNakamura'

def vidcap_from_youtube(youtube_url):
    video = pafy.new(youtube_url)
    print(video.title)
    stream = video.getbest()
    return cv2.VideoCapture(stream.url)

def extract_image_frames(vidcap, path_in, path_out):
    count = 1

    success,image = vidcap.read()
    success = True

    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 10000))

        success,image = vidcap.read()
        if(success):
            cv2.imwrite(path_out + 'frame{}.jpg'.format(count), image)

        count = count + 1

vc = vidcap_from_youtube(test_youtube_vid)
extract_image_frames(vc, IMAGE_IN, IMAGE_OUT)