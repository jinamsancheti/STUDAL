# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 23:21:32 2022

@author: jinam
"""

import cv2
import webbrowser

try:
        
    def acad_calender():
        img = cv2.imread("D:\\COMPUTER PROGRAMMING\\STUDAL\\FINAL_CODES\\acad_calender.png") # change file path according to your convinence 
        cv2.resize(img, (1100,650))
        cv2.imshow("orignal",img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def TT():
    
        img = cv2.imread("D:\\COMPUTER PROGRAMMING\\STUDAL\\FINAL_CODES\\Screenshot 2022-08-18 234355.png") # change file path according to your convinence 
        cv2.resize(img, (1100,650))
        cv2.imshow("orignal",img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def Study_Material():
        url = 'https://drive.google.com/drive/folders/1-ThGbmQmwoEU2ROulflhqU72rrxuw5KM'
        webbrowser.open_new_tab(url)
        
except:
    tmsg.showerror("ERROR", "Error Occured !")