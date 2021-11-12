# import win32com.client as win32
# from PIL import ImageGrab
# import win32process
# import numpy as np
import pyautogui
import time 
import os

# import subprocess
# import msvcrt
# import math
# import cv2
# import win32gui #, win32ui, win32con
 
pyautogui.FAILSAFE = False

# def get_hwnds_for_pid (pid):
#   def callback (hwnd, hwnds):
#     if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
#       _, found_pid = win32process.GetWindowThreadProcessId (hwnd)
#       if found_pid == pid:
#         hwnds.append (hwnd)
#     return True

#   hwnds = []
#   win32gui.EnumWindows (callback, hwnds)
#   return hwnds

filelist=os.listdir('.')
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
  if not(fichier.endswith(".png")):
    filelist.remove(fichier)

# scrcpy = subprocess.Popen ([r"C:\\Users\\dniwa\\Adb\\scrcpy.exe"]) 
loop_time = time.time()

# CutScreenGame = 2
mouseDelay = 0.2
TimeStampDelay = 0

DelayVICTORY = 5

xMovLoc = 1233
FPS = 0 
yMovLoc = 430
# for hwnd in get_hwnds_for_pid (scrcpy.pid):
#   Rect  = win32gui.GetWindowRect(hwnd)
#   # Title = win32gui.GetWindowText(hwnd)

#   x = Rect[2] - Rect[0] 
#   y = Rect[3] - Rect[1]

#   xPercent = math.ceil(x - (x * .011713))
#   yPercent = math.ceil(y - (y * .0208333))
 
  # CutsScreen = int(yPercent / CutScreenGame)
  # print(CutsScreen)


while (True):  
  print("#######")
  print("#RESET#")
  print("#######")

  # 
  xDontGrab = 0
  xCards = 0

  # CLICK VICTORY
  xVICTORY = 0
  xVICTORY1 = 0
  
  # CLICK DEFEATED 
  xDEFEATED = 0
  xDEFEAT = 0

  # CLICK xWINNER
  xWINNER = 0

  # CLICK ADVENTURE
  xADVENTURE = 0

  # FINDING STAGE
  xFIXRIGHTARROW = 0

  # CLICK STAGE
  xRIGHTPOSITION = 0
  xSTAGE19 = 0
  xSTART = 0

  # FIX STAGE
  xFIX1 = 0
  xFIX2 = 0


  # for i in range(3):
  #   for x in range(len(filelist)):
  #     try:
  #       FPS = 1 / (time.time() - loop_time)
  #     except ZeroDivisionError: 
  #       pass

  #     loop_time = time.time()
  #     print(FPS)

  #     try:
  #       xCards, yCards = pyautogui.locateCenterOnScreen(filelist[x], confidence=0.8, grayscale = True)
  #       xDontGrab, yDontGrab  = pyautogui.locateCenterOnScreen('ENDTURN.jpg',  confidence=0.8, grayscale = True)
  #       print(xdontgrab)
  #       if int(xCards) != 0 and int(xdontgrab) != 0:
  #         pyautogui.moveTo(xCards, yCards)
  #         pyautogui.dragTo(322, 131, mouseDelay, button='left')
  #         print("DRAG CARDS")

  #     except TypeError:
  #         pass


  try:
    FPS = 1 / (time.time() - loop_time)
  except ZeroDivisionError: 
    pass

  loop_time = time.time()
  print("FPS : ", FPS)

  # xDontGrab = 266

  try:
    xDontGrab, yDontGrab  = pyautogui.locateCenterOnScreen('ENDTURN.jpg',  confidence=0.8, grayscale = True)
    print("xDontGrab", xDontGrab)
    if int(xDontGrab) != 0:
      for i in range(2):
        for x in range(len(filelist)):
          try:
            xCards, yCards = pyautogui.locateCenterOnScreen(filelist[x], confidence=0.8, grayscale = True)
            if int(xCards) != 0:
              # print("1")
              pyautogui.moveTo(xCards, yCards)
              pyautogui.dragTo(322, 131, mouseDelay, button='left')
              print("DRAG CARDS : ", filelist[x])
          except TypeError:
            pass

      # print("2")
      pyautogui.moveTo(xDontGrab, yDontGrab)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK ENDTURN")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass


  # VICTORY
  try:
    xVICTORY, yVICTORY  = pyautogui.locateCenterOnScreen('VICTORY.jpg',  confidence=0.8, grayscale = True)
    print("xVICTORY")
    if int(xVICTORY) != 0:
      pyautogui.moveTo(xVICTORY, yVICTORY)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK VICTORY")
      time.sleep(DelayVICTORY)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass


  # VICTORY
  try:
    xVICTORY1, yVICTORY1  = pyautogui.locateCenterOnScreen('VICTORY1.jpg',  confidence=0.8, grayscale = True)
    print("xVICTORY1")
    if int(xVICTORY1) != 0:
      pyautogui.moveTo(xVICTORY1, yVICTORY1)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK VICTORY1")
      time.sleep(DelayVICTORY)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass


  # DEFEATED
  try:
    xDEFEATED, yDEFEATED  = pyautogui.locateCenterOnScreen('DEFEATED.jpg',  confidence=0.8, grayscale = True)
    print("xDEFEATED")
    if int(xDEFEATED) != 0:
      pyautogui.moveTo(xDEFEATED, yDEFEATED)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK DEFEATED")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass

# DEFEATED
  try:
    xDEFEAT, yDEFEAT  = pyautogui.locateCenterOnScreen('DEFEAT.jpg',  confidence=0.8, grayscale = True)
    print("xDEFEAT")
    if int(xDEFEAT) != 0:
      pyautogui.moveTo(xDEFEAT, yDEFEAT)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK DEFEAT")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass

  # Winner
  try:
    xWINNER, yWINNER  = pyautogui.locateCenterOnScreen('WINNER.jpg',  confidence=0.8, grayscale = True)
    print("xWINNER")
    if int(xWINNER) != 0:
      pyautogui.moveTo(xWINNER, yWINNER)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK WINNER")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass

  


  # Adventure
  try:
    xADVENTURE, yADVENTURE  = pyautogui.locateCenterOnScreen('ADVENTURE.jpg',  confidence=0.8, grayscale = True)
    print("xADVENTURE")
    if int(xADVENTURE) != 0:
      pyautogui.moveTo(xADVENTURE, yADVENTURE)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK ADVENTURE")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass




  # Finding Stage
  try:
    xFIXRIGHTARROW, yFIXRIGHTARROW  = pyautogui.locateCenterOnScreen('FIXRIGHTARROW.jpg',  confidence=0.8, grayscale = True)
    if int(xFIXRIGHTARROW) != 0:
      pyautogui.moveTo(628, 128)
      pyautogui.click(clicks=1, interval=1)
      print("CLICK FIXRIGHTARROW")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass



  # Click Stage & Click Start
  try:
    xRIGHTPOSITION, yRIGHTPOSITION  = pyautogui.locateCenterOnScreen('RIGHTPOSITION.jpg',  confidence=0.8, grayscale = True)
    if int(xRIGHTPOSITION) != 0:
      xSTAGE19, ySTAGE19  = pyautogui.locateCenterOnScreen('STAGE19.jpg',  confidence=0.8, grayscale = True)
      if int(xSTAGE19) != 0:
        pyautogui.moveTo(xSTAGE19, ySTAGE19)
        pyautogui.click(clicks=1, interval=1)
        print("CLICK STAGE19")
        time.sleep(TimeStampDelay)
        pyautogui.moveTo(xMovLoc, yMovLoc)
        xSTART, ySTART  = pyautogui.locateCenterOnScreen('START.jpg',  confidence=0.8, grayscale = True)
        if int(xSTART) != 0:
          pyautogui.moveTo(xSTART, ySTART)
          pyautogui.click(clicks=1, interval=1)
          print("CLICK START")
          time.sleep(TimeStampDelay)
          pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass



  # Fix Stage
  try:
    xFIX1, yFIX1  = pyautogui.locateCenterOnScreen('FIX1.jpg',  confidence=0.8, grayscale = True)
    if int(xFIX1) != 0:
      pyautogui.click(button='right', clicks=1, interval=1)
      print("CLICK FIX1")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass

  try:
    xFIX2, yFIX2  = pyautogui.locateCenterOnScreen('FIX2.jpg',  confidence=0.8, grayscale = True)
    if int(xFIX2) != 0:
      pyautogui.click(button='right', clicks=1, interval=1)
      print("CLICK xFIX2")
      time.sleep(TimeStampDelay)
      pyautogui.moveTo(xMovLoc, yMovLoc)
  except TypeError:
    pass



  print("*************************")

 