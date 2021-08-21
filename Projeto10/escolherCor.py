import cv2
import os
import json
import numpy as np

def callback(x):
   return

def carrega_parametros():   
   lowH = 0
   lowS = 0
   lowV = 0
   highH = 179
   highS = 255
   highV = 255

   lowR = 0
   lowG = 0
   lowB = 0
   highR = 255
   highG = 255
   highB = 255
    
   return lowH, highH, lowS, highS, lowV, highV, lowR, highR, lowG, highG, lowB, highB

def barras_hsv():
   cv2.namedWindow(image_name)
   cv2.resizeWindow(image_name, 400, 300)
   cv2.createTrackbar('lowH',image_name,lowH,179,callback)
   cv2.createTrackbar('highH',image_name,highH,179,callback)
   cv2.createTrackbar('lowS',image_name,lowS,255,callback)
   cv2.createTrackbar('highS',image_name,highS,255,callback)
   cv2.createTrackbar('lowV',image_name,lowV,255,callback)
   cv2.createTrackbar('highV',image_name,highV,255,callback)
    
   cv2.setTrackbarPos('lowH',image_name,lowH)
   cv2.setTrackbarPos('highH',image_name,highH)
   cv2.setTrackbarPos('lowS',image_name,lowS)
   cv2.setTrackbarPos('highS',image_name,highS)
   cv2.setTrackbarPos('lowV',image_name,lowV)
   cv2.setTrackbarPos('highV',image_name,highV)

def barras_rgb():
   cv2.namedWindow(image_name)
   cv2.resizeWindow(image_name, 400, 300)
   cv2.createTrackbar('lowR',image_name,lowR,255,callback)
   cv2.createTrackbar('highR',image_name,highR,255,callback)
   cv2.createTrackbar('lowG',image_name,lowG,255,callback)
   cv2.createTrackbar('highG',image_name,highG,255,callback)
   cv2.createTrackbar('lowB',image_name,lowB,255,callback)
   cv2.createTrackbar('highB',image_name,highB,255,callback)

   cv2.setTrackbarPos('lowR',image_name,lowR)
   cv2.setTrackbarPos('highR',image_name,highR)
   cv2.setTrackbarPos('lowG',image_name,lowG)
   cv2.setTrackbarPos('highG',image_name,highG)
   cv2.setTrackbarPos('lowB',image_name,lowB)
   cv2.setTrackbarPos('highB',image_name,highB)  

lowH, highH, lowS, highS, lowV, highV, lowR, highR, lowG, highG, lowB, highB = carrega_parametros()

captura = cv2.VideoCapture(0)
mode = "HSV"
image_name = mode +" color space"
cv2.namedWindow(image_name)

captura.read()
barras_hsv()

while True:
    _, image1 = captura.read()

    if mode=="RGB":
        lowR = cv2.getTrackbarPos('lowR', image_name)
        highR = cv2.getTrackbarPos('highR', image_name)
        lowG = cv2.getTrackbarPos('lowG', image_name)
        highG = cv2.getTrackbarPos('highG', image_name)
        lowB = cv2.getTrackbarPos('lowB', image_name)
        highB = cv2.getTrackbarPos('highB', image_name)
        img1_cvt = image1.copy()
        lower = np.array([lowB, lowR, lowG])
        higher = np.array([highB, highR, highG])
        
    elif mode=="HSV":
        lowH = cv2.getTrackbarPos('lowH', image_name)
        highH = cv2.getTrackbarPos('highH', image_name)
        lowS = cv2.getTrackbarPos('lowS', image_name)
        highS = cv2.getTrackbarPos('highS', image_name)
        lowV = cv2.getTrackbarPos('lowV', image_name)
        highV = cv2.getTrackbarPos('highV', image_name)
        img1_cvt = cv2.cvtColor(image1.copy(),cv2.COLOR_BGR2HSV)
        lower = np.array([lowH, lowS, lowV])
        higher = np.array([highH, highS, highV])    
    
    mask1 = cv2.inRange(img1_cvt, lower, higher)
    
    image_final1 = cv2.bitwise_and(image1, image1, mask=mask1)    

    cv2.imshow('imagem final 1', image_final1)    
    
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord("q"):
        captura.release()
        cv2.destroyAllWindows()
        break
    elif k == ord("m"):
        if mode =="RGB":
            mode = "HSV"
            lowR = cv2.getTrackbarPos('lowR', image_name)
            highR = cv2.getTrackbarPos('highR', image_name)
            lowG = cv2.getTrackbarPos('lowG', image_name)
            highG = cv2.getTrackbarPos('highG', image_name)
            lowB = cv2.getTrackbarPos('lowB', image_name)
            highB = cv2.getTrackbarPos('highB', image_name)
            cv2.destroyWindow(image_name)
            image_name = mode +" color space"
            cv2.namedWindow(image_name)
            barras_hsv()
            
        else:
            mode ="RGB"
            lowH = cv2.getTrackbarPos('lowH', image_name)
            highH = cv2.getTrackbarPos('highH', image_name)
            lowS = cv2.getTrackbarPos('lowS', image_name)
            highS = cv2.getTrackbarPos('highS', image_name)
            lowV = cv2.getTrackbarPos('lowV', image_name)
            highV = cv2.getTrackbarPos('highV', image_name)
            cv2.destroyWindow(image_name)
            image_name = mode +" color space"
            cv2.namedWindow(image_name)
            barras_rgb()
