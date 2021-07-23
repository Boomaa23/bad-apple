import cv2
import time
import pyautogui
import os
import subprocess


def main():
    gradient_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    video = cv2.VideoCapture('../ba-src.mp4')
    out_file = open('process.txt', 'w+')
    total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # for i in range(200):
    #     video.read()

    print('Waiting 5s to start. Open notepad now.')
    time.sleep(5)
    
    retcode, image = video.read()
    ctr = 1
    while retcode:
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (110, 48))
        width, height = image.shape
        
        for x in range(width):
            for y in range(height):
                idx = int((len(gradient_map) - 1) * float(image[x, y]) / 255.0)
                out_file.write(gradient_map[idx])
            out_file.write('\n')
        out_file.flush()

        pyautogui.hotkey('ctrl', 'o')
        pyautogui.typewrite('process.txt')
        pyautogui.press('enter')
        
        cv2.imshow("ms-notepad", image)
        cv2.moveWindow("ms-notepad", 1000,30)
        cv2.waitKey(1)
        
        out_file.truncate(0)
        out_file.seek(0)
        
        ctr += 1
        print("Frame: %s / %s" % (ctr, total))

        retcode, image = video.read()
        


if __name__ == "__main__":
    main()