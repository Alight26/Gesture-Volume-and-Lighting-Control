import cv2 as cv 
import mediapipe as mp

# Finds the location of the pointer fingers tip and draws a circle around it 
def pointer_tip(hand_landmarks, img, h, w):
            pointer_tip = hand_landmarks.landmark[8]

            # extracting those coordinates 
            pointer_x = pointer_tip.x
            pointer_y = pointer_tip.y

            # Converting to pixel coordinates 
            pointer_x = int(pointer_x * w)
            pointer_y = int(pointer_y * h)

            # Drawing a circle around index finger tip 
            index_point = cv.circle(img, (pointer_x, pointer_y), 20, (100, 55, 0), -1)

            return index_point

# Finds the location of the thumb tip and draws a finger around it

def thumb_tip(hand_landmarks, img, h, w):
        thumb_tip = hand_landmarks.landmark[4]

        # Extracting the coordinates 
        thumb_x = thumb_tip.x
        thumb_y = thumb_tip.y

        # Converting to pixel coordinates 
        thumb_x = int(thumb_x * w)
        thumb_y = int(thumb_y * h)

        # Drawing the circle around the thumb 
        thumb_point = cv.circle(img, (thumb_x, thumb_y), 20, (100, 55, 0), -1)