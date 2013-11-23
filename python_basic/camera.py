import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'output2.avi', cv2.cv.CV_FOURCC('I', '4', '2', '0'), fps, size)

success, frame = cameraCapture.read()
numFramesRemaining = 100 * fps - 1

if success:
    print "ready to write the video file"
else:
    print "can not write the video file"

while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, fram = cameraCapture.read()
    numFramesRemaining -= 1
    print numFramesRemaining
