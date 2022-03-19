import numpy as np
import cv2





def controlss():
    def passing(p):
        pass

    controlls = cv2.namedWindow('controls',cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow('controls', 350,750)

    cv2.createTrackbar('speed', 'controls', 0, 100, passing)
    cv2.createTrackbar('size', 'controls', 5, 20, passing)

    cv2.createTrackbar('inBlack', 'controls', 0, 255, passing)
    cv2.createTrackbar('inWhite', 'controls', 255, 255, passing)
    cv2.createTrackbar('inGamma', 'controls', 1, 15, passing)
    cv2.createTrackbar('outBlack', 'controls', 0, 255, passing)
    cv2.createTrackbar('outWhite', 'controls', 255, 255, passing)

    # cv2.createTrackbar('rgb-gray', 'controls',1, 1, passing)

    cv2.createTrackbar('up_mask1', 'controls', 1, 255, passing)
    cv2.createTrackbar('up_mask2', 'controls', 1, 255, passing)
    cv2.createTrackbar('up_mask3', 'controls', 1, 255, passing)

    cv2.createTrackbar('low_mask1', 'controls', 1, 225, passing)
    cv2.createTrackbar('low_mask2', 'controls', 1, 225, passing)
    cv2.createTrackbar('low_mask3', 'controls', 1, 225, passing)

    cv2.createTrackbar('Y2', 'controls', 100, 1000, passing)
    cv2.createTrackbar('X2', 'controls', 50, 1000, passing)

    cv2.createTrackbar('Y1', 'controls', 10, 500, passing)
    cv2.createTrackbar('X1', 'controls', 10, 500, passing)




def frame_size():
    size = float(cv2.getTrackbarPos('size', 'controls'))
    size = size / 10

    if size < 0.1:
        size = 0.1
    return size

def speed():
    speed = float(cv2.getTrackbarPos('speed', 'controls'))
    speed = speed / 100
    return speed

def levels(img):
    v1 = int(cv2.getTrackbarPos('inBlack', 'controls'))
    v2 = int(cv2.getTrackbarPos('inWhite', 'controls'))
    v3 = int(cv2.getTrackbarPos('inGamma', 'controls'))
    v4 = int(cv2.getTrackbarPos('outBlack', 'controls'))
    v5 = int(cv2.getTrackbarPos('outWhite', 'controls'))

    inBlack = np.array([v1, v1, v1], dtype=np.float32)
    inWhite = np.array([v2, v2, v2], dtype=np.float32)
    inGamma = np.array([v3, v3, v3], dtype=np.float32)
    outBlack = np.array([v4, v4, v4], dtype=np.float32)
    outWhite = np.array([v5, v5, v5], dtype=np.float32)

    img = np.clip((img - inBlack) / (inWhite - inBlack), 0, 255)
    img = (img ** (1 / inGamma)) * (outWhite - outBlack) + outBlack
    img = np.clip(img, 0, 255).astype(np.uint8)
    return img

def rgb2gray(img):
    v8 = int(cv2.getTrackbarPos('rgb-gray', 'controls'))
    if v8 == 0:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return img
    if v8 == 1:

        return img
    v8 =4

def mask(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    v1 = int(cv2.getTrackbarPos('low_mask1', 'controls'))
    v2 = int(cv2.getTrackbarPos('low_mask2', 'controls'))
    v3 = int(cv2.getTrackbarPos('low_mask3', 'controls'))

    v4 = int(cv2.getTrackbarPos('up_mask1', 'controls'))
    v5 = int(cv2.getTrackbarPos('up_mask2', 'controls'))
    v6 = int(cv2.getTrackbarPos('up_mask3', 'controls'))

    lower_red = np.array([v1, v2, v3])
    upper_red = np.array([v4, v5, v6])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(hsv, img, mask=mask)
    return mask

def focus_y2():
    y2 = int(cv2.getTrackbarPos('Y2', 'controls'))
    if y2 <150:
        y2  = 150
    return y2

def focus_x1():
    x1 = int(cv2.getTrackbarPos('X1', 'controls'))

    return x1

def focus_y1():
    y1 = int(cv2.getTrackbarPos('Y1', 'controls'))
    return y1

def focus_x2():

    x2 = int(cv2.getTrackbarPos('X2', 'controls'))
    if x2 <100:
        x2  = 100
    return x2



