import os
# UPLOAD_FOLDER_PATH = "../static"

def create_folder(name):
    try:
    # creating a folder named data
        if not os.path.exists('static/'+name):
            os.makedirs('static/'+name)
            print("Created "+name+" directory")

# if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # print("SetUp Completed!!!")

def setup():
    try:
    # creating a folder named data
        if not os.path.exists('static'):
            os.makedirs('static')
            print("Created Static directory")
        
        command = f'pip show ultralytics'
        exit_code = os.system(command)

    # Check the exit code to determine if the library is installed
        if exit_code == 0:
            print(f"ultralytics is installed!")
        else:
            print(f"ultralytics is being installed!")
            os.system('pip install ultralytics -q')

# if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    print("SetUp Completed!!!")