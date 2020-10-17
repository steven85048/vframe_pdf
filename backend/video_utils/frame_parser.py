import pafy
import cv2

FRAME_CAPTURE_INTERVAL = 1000 # in ms

def extract_frames_from_youtube(youtube_url, path_out):
    vc = _vidcap_from_youtube(youtube_url)
    _extract_image_frames(vc, path_out)

def _vidcap_from_youtube(youtube_url):
    video = pafy.new(youtube_url)
    print(video.title)
    stream = video.getbest()
    return cv2.VideoCapture(stream.url)

def _vidcap_from_local_video(vid_path):
    return cv2.VideoCapture(vid_path)

def _extract_image_frames(vidcap, path_out):
    """
    Extract frames from a video at FRAME_CAPTURE_INTERVAL milliseconds and
    stores those frames into path_out.
    """
    count = 1

    success,image = vidcap.read()
    success = True

    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * FRAME_CAPTURE_INTERVAL))

        success,image = vidcap.read()
        if(success):
            cv2.imwrite(path_out + 'frame{}.jpg'.format(count), image)

        count = count + 1

if __name__ == "__main__":
    path_out = 'test_frames/'
    test_youtube_vid = 'https://www.youtube.com/watch?v=DNMO-MdmO6g&ab_channel=HiroshiNakamura'

    extract_frames_from_youtube(test_youtube_vid, path_out)