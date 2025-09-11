import cv2 as cv 
import mediapipe as mp
import math
import subprocess, time

def volume_up():
    subprocess.run(["cliclick", "kp:F12"])

def volume_down():
    subprocess.run(["cliclick", "kp:F11"])

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
        return thumb_point



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
        


        return



_last = None
_last_time = 0

def length(true_length):
    global _last, _last_time

    now = time.time()

    if _last is None:
        _last = true_length
        return

    diff = true_length - _last

    # only trigger if enough change & not too fast
    if diff >= 100 and (now - _last_time) > 0.15:
        volume_up()
        print("Volume up")
        _last_time = now

    elif diff <= -100 and (now - _last_time) > 0.15:
        volume_down()
        print("Volume down")
        _last_time = now

    # update baseline
    _last = true_length




        
'''

        # finding the circle distance to see if I can draw another circle
        int_checker = point / 18

        int_check = isinstance(int_checker, int)

        # Checks if it is the correct length and an integer
        if int_check is True:
                temp_circle = cv.circle(img, (x_values, y_values), 20, (100, 55, 0), -1)
                arr.append((int_checker, temp_circle))
                count += 1
                
        # check if length between thumb and index is smaller than the last array element
        if point > 18 and len(arr) >= 1:
                if point < arr[-1][0]:
                    arr.pop(count)
                    count -= 1

        return 

'''








        


   


