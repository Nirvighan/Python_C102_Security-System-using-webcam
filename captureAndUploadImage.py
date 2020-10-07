import cv2
import dropbox
import time
import random
start_time = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    videoCapObj = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCapObj.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False

    return image_name
    print("SNAPSHOT IS TAKEN")

    videoCapObj.release()

    cv2.destroyAllWindows()


def uploadFiles(image_name):
    access_token = "3r652F1gy6QAAAAAAAAAAXPSMVagVaDPkYVvDWbjOEJZtuf3P1gZDEfdAPilPTCz"
    file = image_name
    file_from = file
    file_to = "/newFolder1/"+(image_name)
    dbx = dropbox.Dropbox()

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")


def main():
    while(True):
        if((time.time()-start_time)>=60):
            name = takeSnapshot()
            uploadFiles(name)


main()

