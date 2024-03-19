import os
# UPLOAD_FOLDER_PATH = "../static"

def setup():
    try:

    # creating a folder named data
        if not os.path.exists('static/videos'):
            os.makedirs('static/videos')
            print("Created videos directory")
        if not os.path.exists('static/frames'):
            os.makedirs('static/frames')
            print("Created frames directory")

# if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    print("SetUp Completed!!!")