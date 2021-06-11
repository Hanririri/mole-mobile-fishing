from PIL import ImageGrab
import pyautogui
import win32api
import win32gui
import time


def getDesiredWindow():
    """Returns the top-left and bottom-right of the desired window."""
    print('Click the top left of the desired region.')
    pt1 = detectClick()
    print('First position set!')
    time.sleep(1)
    print('Click the bottom right of the desired region.') 
    pt2 = detectClick()
    print('Got the window!')
    return pt1,pt2

def detectClick():
    """Detects and returns the click position"""
    state_left = win32api.GetKeyState(0x01)
    print("Waiting for click...")
    while True:
        a = win32api.GetKeyState(0x01)
        if a != state_left: #button state changed
            state_left = a
            if a < 0:
                print('Detected left click')
                return win32gui.GetCursorPos()
        time.sleep(0.1)


def getRedPixVal(pt1,pt2):
    """Gets the reference pixel value with the water bob above water."""
    # From the two input points, define the desired box
    box = (pt1[0],pt1[1],pt2[0],pt2[1])
    # Get the image of the desired section
    image = ImageGrab.grab(box)
    # List the red band values of the image (1-d vector) 
    l = list(image.getdata(0))
    # Return the average red band value
    return sum(l)/len(l) 

def fishingLoop():
    """Main fishing loop: gets the desired window and start running the thing."""
    pass

def main():
    """Main function of the MinecraftFisher."""
    print('Running...')

    # Get the window
    pt1, pt2 = getDesiredWindow() # detcet the "!"

    pt3, pt4 = getDesiredWindow() # detect is fishing now?

    # Give user grace period of 3 seconds before starting game
    print('Starting mole fisher in 3 seconds...')
    time.sleep(3)
    # Set the reference red pixel value
    refPixVal = getRedPixVal(pt1,pt2)

    refPixVal2 = getRedPixVal(pt3,pt4)

    print('Ref Pix Val: {}'.format(refPixVal))
    time.sleep(1)
    print('click')
    pyautogui.click() # 开始钓鱼
    print('Start fishing...')
    # Main fishing loop
    while True:
        time.sleep(2)
        while (getRedPixVal(pt3,pt4)>refPixVal2 *1.2):
            currentRedVal = getRedPixVal(pt1,pt2)
            print('Fishing... PixValue: {}'.format(round(currentRedVal/refPixVal,2)))
            if currentRedVal > refPixVal *1.2: 
            # If the bob goes below the water
                print('Fish on reel!')
            # Right-click to reel-in fish
                pyautogui.click() # 确定钓鱼
            # Wait for fishing bob to resume its position
                time.sleep(2)
                pyautogui.click() # 收杆
                time.sleep(3) 
                pyautogui.click() # 返回主界面
                time.sleep(3)
                # Right click again to start fishing once again
                print('Resetting...')
                pyautogui.click() # 开始钓鱼
                # Wait for fishing bob to resume its position
                time.sleep(0.1) 

            time.sleep(0.35)
    
        pyautogui.click()
        print('Restarting fishing...')

if __name__ == '__main__':
    main()
    