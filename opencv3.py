import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening the camera")
else:
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Camera', frame)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()



