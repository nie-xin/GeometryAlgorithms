import cv2

image = cv2.imread('lena.jpg')
cv2.imwrite('MyPic.jpg',image)

byteArray = bytearray(image)
grayImage = numpy.array(grayByteArray).reshape(height, width)
bgrImage = numpy.array(bgrByteArray).reshape(height, width, 3)

#grayImg = cv2.imread('lena.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
#cv2.imwrite('GrayPic.jpg', grayImg)


