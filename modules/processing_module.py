import cv2
import os

def videoToFrames(video):
    currentframe = 0

    while (True):

        # reading from frame
        ret, frame = video.read()

        if ret:
            # if video is still left continue creating images
            name = 'static/frames/frame_' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    return currentframe


def process(name):
    print(os.path.abspath("")+os.path.join("/static/videos", name))
    video = cv2.VideoCapture(os.path.abspath("")+os.path.join("/static/videos", name))
    num_frames = videoToFrames(video)
    print(num_frames)