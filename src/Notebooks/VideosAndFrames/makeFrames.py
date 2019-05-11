import cv2
 
# Opens the Video file
cap= cv2.VideoCapture('IMG4177.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    num = f"{i:04d}"
    cv2.imwrite(str(num)+'.jpg',frame)
#    if i > 4000:
#        break
    i+=1
 
cap.release()
cv2.destroyAllWindows()
