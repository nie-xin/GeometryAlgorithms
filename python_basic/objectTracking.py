import cv2
import numpy as np 

drawing = False
ix, iy = -1, -1

# select ROI
def draw_rec(event, x, y, flags, param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        print('Mouse clicked')
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(frame, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(frame, (ix, iy), (x, y), (0, 255, 0), 1)

cv2.namedWindow('frame')
cap = cv2.VideoCapture('test.avi')
# get first frame for object selecting
ret, frame = cap.read()
#cv2.imshow('frame', frame)
cv2.setMouseCallback('frame', draw_rec)

while(1):
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


# while(cap.isOpened()):
#     ret, frame = cap.read()

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# mouse event

cap.release()
cv2.destroyAllWindows()
