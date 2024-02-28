import cv2
video_path = "C:\sim py\Internship\WhatsApp Video 2023-07-24 at 5.20.03 PM.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video stream")
else:
    while True:
        ret, frame = cap.read()
        
        if ret:
            cv2.imshow('Video', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
