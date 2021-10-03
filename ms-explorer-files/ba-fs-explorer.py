import cv2
import os
import shutil
import time

delay_time_sec = 2
disp_size = (17, 11)
skip_frames = 0

def main():
    if not os.path.exists('../ba-src.mp4'):
        raise FileNotFoundError('Source video not found')
    video = cv2.VideoCapture('../ba-src.mp4')
    for i in range(skip_frames):
        video.read()

    total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    retcode, image = video.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, disp_size)

    width, height = image.shape
    for x in range(width):
            for y in range(height):
                shutil.copyfile("black.png", "process/%i-%i.png" % (x, y))
    
    lastimg = image
    retcode, image = video.read()

    ctr = 2

    print("Total: %s" % total)
    print("Time to completion: %s hours %s minutes %s seconds\n" % (int((total * delay_time_sec) / 3600), 
        int((total * delay_time_sec) / 60) % 60, (total * delay_time_sec) % 60))
    starttime = time.time_ns()

    while retcode:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, disp_size)
        width, height = image.shape
        
        for x in range(width):
            for y in range(height):
                copy = str()
                if image[x, y] < 128 and lastimg[x, y] >= 128:
                    copy = "white.png"
                elif lastimg[x, y] < 128:
                    copy = "black.png"

                if copy:
                    try:
                        shutil.copyfile(copy, "process/%i-%i.png" % (x, y))
                    except PermissionError:
                        shutil.copyfile(copy, "process/%i-%i.png" % (x, y))

        time.sleep(delay_time_sec)

        # for fn in os.listdir("process"):
        #     path = os.path.join("process", fn)
        #     if os.path.isfile(path):
        #         os.unlink(path)

        lastimg = image
        retcode, image = video.read()
        ctr += 1
        print("Frame: %s" % ctr)
    
    tdiff = (time.time_ns - starttime) / pow(10, 9)
    print("Total time: %s hours %s minutes %s seconds\n" % (int(tdiff) / 3600, int(tdiff / 60) % 60, tdiff % 60))

if __name__ == "__main__":
    main()