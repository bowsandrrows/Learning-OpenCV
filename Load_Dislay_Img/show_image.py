import cv2

img = cv2.imread('../Photos/flower004.jpg', cv2.IMREAD_UNCHANGED)  # the default value is: cv2.IMREAD_COLOR or (1).
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('flower', img)
cv2.imshow('flower_gray', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
