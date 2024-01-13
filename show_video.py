import cv2


vid_cup = cv2.VideoCapture('Videos/VID-20221103-WA0044_1.mp4')

success, img = vid_cup.read()
while success:
    # normal video format: cv2.imshow("Video", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", gray)
    # Press the "Esc" key to break the loop, (keycode is 27)
    if cv2.waitKey(15) & 0xFF == 27:
        break
    success, img = vid_cup.read()
vid_cup.release()
cv2.destroyAllWindows()
