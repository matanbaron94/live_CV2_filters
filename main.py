import time
import cv2
import photoshop


video = "docs/vid.mp4"

cap = cv2.VideoCapture(video)
c = photoshop.controlss()

padding_top = 100
padding_left = 150
space = 2


while True:

    success, image = cap.read()

    size = photoshop.frame_size()
    image = cv2.resize(image, (0, 0), fx=size, fy=size)


    focus_frame = image.copy()
    original = image.copy()
    mask = image.copy()
    filter = original.copy()


    height = image.shape[0]
    width = image.shape[1]

    #levels
    filter = photoshop.levels(filter)

    #mask
    mask = photoshop.mask(filter)

    #frame speed
    speed = photoshop.speed()
    time.sleep(speed)


    #focus frame
    y2 = photoshop.focus_y2()
    x1 = photoshop.focus_x1()
    y1 = photoshop.focus_y1()
    x2 = photoshop.focus_x2()

    focus_frame = focus_frame[x1:x2 , y1:y2]



    cv2.moveWindow('controls', padding_left, padding_top)
    cv2.imshow('Fillterd', filter)
    cv2.moveWindow('Fillterd', padding_left + 350 +space, padding_top+height+30+space)
    cv2.imshow('Original', original)
    cv2.moveWindow('Original', padding_left + 350 +space, padding_top)
    cv2.imshow('mask', mask)
    cv2.moveWindow('mask', padding_left + 350 +space+width+space, padding_top+height+30+space)
    cv2.imshow('focus', focus_frame)
    cv2.moveWindow('focus', padding_left + 350 + space + width + space, padding_top)



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print("jj")
        break
