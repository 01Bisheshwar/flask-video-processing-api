import cv2
import os
from moviepy.editor import VideoFileClip
import subprocess
import shutil
# from ultralytics import YOLO

# def videoToFrames(video):
#     currentframe = 0

#     while (True):

#         # reading from frame
#         ret, frame = video.read()

#         if ret:
#             # if video is still left continue creating images
#             name = 'static/frames/frame_' + str(currentframe) + '.jpg'
#             print('Creating...' + name)

#             # writing the extracted images
#             cv2.imwrite(name, frame)

#             # increasing counter so that it will
#             # show how many frames are created
#             currentframe += 1
#         else:
#             break

#     return currentframe

# def processVideo(path,name):
#     subprocess.run('yolo detect predict model=yolov8s.pt source=" '+path+name+'"')
#     # os.system('yolo detect predict model=yolov8s.pt source="'+path+name+'"')
#     clip = VideoFileClip(path+".".split(name)[0]+'.avi')
#     clip.write_videofile(path+'final.mp4', codec='libx264', audio_codec='aac', preset='slow', bitrate='5000k')
#     # os.system('ffmpeg -i {"'+path+".".split(name)[0]+'.avi"} -vcodec libx264 {"'+path+'final.mp4"}')

def processVideo(username, name):
    try:
        # Get disk usage statistics
        total, used, free = shutil.disk_usage("/")

        # Convert bytes to GB for better readability
        total_gb = total / (2**30)
        used_gb = used / (2**30)
        free_gb = free / (2**30)

        # Print disk usage information
        print("Total Space: {:.2f} GB".format(total_gb))
        print("Used Space: {:.2f} GB".format(used_gb))
        print("Free Space: {:.2f} GB".format(free_gb))
        path1 = os.path.join(os.getcwd(), 'static')
        path = os.path.join(path1, username + "/")
        print('Curr Dir : ',os.getcwd())
        print(os.listdir(path1))
        print(os.listdir(os.getcwd()))
        print('Path : ',path)
        print('Name of file : ',name)
        # Run YOLO object detection
        result = subprocess.run(['python', 'detect.py', '--source', './data/images/bus.jpg'], capture_output=True, text=True)
        print(os.listdir(os.getcwd()))
        print(os.listdir(os.path.join(os.getcwd(), 'runs')))

        if result.returncode != 0:
            # YOLO command failed, print error and command output
            print("YOLO command execution failed with error:")
            print(result.returncode)
            print("my error is : ",result.stderr)
            print('Error ended')
        else:
            # YOLO command succeeded, continue with video conversion
            input_video_path = os.path.join("./runs/detect/predict", name.rsplit('.', 1)[0] + '.avi')
            output_video_path = os.path.join(path, 'final.mp4')

            # Convert the processed video to .mp4
            clip = VideoFileClip(input_video_path)
            clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac', preset='slow', bitrate='5000k')

            print("Video processing completed successfully!")

            # DELETE THE VIDEOS AND DIRECTORIES LATER
            # SEND THE VIDEO TO THE FRONTEND
    except Exception as e:
        print(f"Error processing video: {e}")

def process(name, username):
    try:
        # Construct path to the video
        
        # path = os.path.join("/static/", username + "/")

        # Call processVideo
        processVideo(username, name)
    except Exception as e:
        print(f"Error in processing: {e}")
