
import cv2
from gaze_tracking import GazeTracking
import time

start = False

def click(event, x, y, flags, param):
    global start
    if event == cv2.EVENT_LBUTTONDOWN:
        start = True


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
cv2.namedWindow("image")
cv2.setMouseCallback("image", click)
k = 0
t1 = 0
while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()
    text = "Clik on the screen to start acounting"

    if start:
        text = str(int(time.time() - t1))
        if time.time() - t1 < 5:
            if gaze.is_blinking():
                k += 1
        else:
            break
    else:
        t1 = time.time()
            
        

    cv2.putText(new_frame, text, (20, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("image", new_frame)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows() 
webcam.release()
print("Вы маргнули примерно " + str(k//3) + " раз.")


