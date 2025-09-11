import cv2 as cv 
import mediapipe as mp
import math

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
        return thumb_tip



# Connects the thumb and the index finger together
def connector(pointy, thumby, img, h, w):
        # getting the landmarks for each thumb and pointer tip
        point_tip = pointy 
        thumb_tip = thumby

        point_tip_x = int(point_tip.x * w)
        point_tip_y = int(point_tip.y * h)

        thumb_tip_x = int(thumb_tip.x * w)
        thumb_tip_y = int(thumb_tip.y * h)

        

        # Uses the tip points already calculated in other functions and connects them
        connection = cv.line(img, (point_tip_x, point_tip_y), (thumb_tip_x, thumb_tip_y),(0, 255, 0), 10)

        x_values = (point_tip_x - thumb_tip_x) ** 2
        y_values = (point_tip_y - thumb_tip_y) ** 2

        true_length = math.sqrt(x_values + y_values)
        print(true_length)

        return connection

"""
def length(point_tip_x, point_tip_y, thumb_tip_x, thumb_tip_y):
        x_values = """


   


