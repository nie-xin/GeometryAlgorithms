import numpy as np
import cv2

#clicked = False
#def onMouse(event, x, y, flags, param):
    #global clicked
    #if event == cv2.cv.CV_EVENT_LBUTTONUP:
        #clicked = True

#cameraCapture = cv2.VideoCapture(0)
#while(True):
    #ret, frame = cameraCapture.read()

    #cv2.imshow('fram', frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

#cameraCapture.release()
#cv2.destroyAllWindows()

#cv2.namedWindow('Capture')
#cv2.setMouseCallback('Capture', onMouse)

#print 'Showing camera feed, Click window or press an key to stop.'
#success, frame = cameraCapture.read()
#while success and cv2.waitKey(1) == -1 and not clicked:
    #cv2.imshow('Capture', frame)
    #success, frame = cameraCapture.read()

#cv2.destroyWindow('Capture')

cap = cv2.VideoCapture('test.avi')


while(cap.isOpened()):
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

