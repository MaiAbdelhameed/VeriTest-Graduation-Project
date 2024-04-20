import pyautogui

def get_mouse_click():
        while 1:
            if pyautogui.mouseDown(button='left'):
                click_x, click_y = pyautogui.position()
                print(f"Left mouse clicked at: ({click_x}, {click_y})")
                break
            

    
   

get_mouse_click()







