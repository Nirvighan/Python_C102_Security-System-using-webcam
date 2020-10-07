import cv2

def take_snapshot():
    videoCapObj = cv2.VideoCapture(1)
    result = True
    while(result):
        ret,frame = videoCapObj.read()
        cv2.imwrite("newPicture.jpg",frame)
        result = False

    videoCapObj.release()
    cv2.destroyAllWindows()

take_snapshot()