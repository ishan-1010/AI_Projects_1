import cv2
import mediapipe as mp  # mediapipe is a library for hand detection
import time

cap = cv2.VideoCapture(0)  # 0 is for webcam, 1 is for external camera

mpHands = mp.solutions.hands
hands = mpHands.Hands()  # Hands() is a class
mpDraw = mp.solutions.drawing_utils  # drawing_utils is a class

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(
        img, cv2.COLOR_BGR2RGB
    )  # mediapipe only works with RGB images
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)  # this will print the coordinates of the hand

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                print(id, lm)  # id is the index of the landmark, lm is the landmark
                h, w, c = img.shape  # height, width, channel
                cx, cy = int(lm.x * w), int(lm.y * h)  # center x, center y
                print(id, cx, cy)
                # if id == 0:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(
                img, handLms, mpHands.HAND_CONNECTIONS
            )  # draw landmarks on the image

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
    )  # (image, text, position, font, scale, color, thickness)

    cv2.imshow("Image", img)
    cv2.waitKey(1)  # 1 is for 1 millisecond
