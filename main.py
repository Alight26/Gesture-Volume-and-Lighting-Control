import cv2 as cv 
import mediapipe as mp 

# Initializes the hand
mp_hands = mp.solutions.hands

mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence = 0.5,
                       min_tracking_confidence = 0.5)

cap = cv.VideoCapture(1)

while True:
    ret, img = cap.read()
    img = cv.flip(img, 1)
    if not ret:
        break

    RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(RGB_img)

    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[idx].classification[0].label

            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, c = img.shape
            x,y = int(hand_landmarks.landmark[0].x * w), int(hand_landmarks.landmark[0].y * h)
            cv.putText(img, hand_label, (x,y-20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    cv.imshow('img', img)
    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
