# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:43:47 2021

@author: Priyanshi
"""

import cv2
import numpy as np
vid = cv2.VideoCapture(0)#to start the video we use this function
while(1):#while loop bcoz we need to update the frame one by one and we need to keep updating them
    
    _,frame = vid.read()#to read a image and then to add the image at that time to frame
    cv2.imshow("kvideo",frame)#to show the read function we use this function
    q = cv2.waitKey(1)#waitkey yha isliye lgai h ki ek point pe apan ko rokni bhi h video nhi to while loop ki wjah se wo chlta hi jayega
    if q == ord('q'): # breaking conditions , ord is used to find ascii of any character
       break
vid.release()#to release the video

cv2.destroyAllWindows()
