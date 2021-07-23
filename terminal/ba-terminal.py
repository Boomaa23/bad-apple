import cv2
import time

def main():
    gradient_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    video = cv2.VideoCapture('../ba-src.mp4')
    
    retcode, image = video.read()
    while retcode:
        # frametime = time.time_ns()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (80, 32))
        width, height = image.shape
        
        for x in range(width):
            for y in range(height):
                idx = int((len(gradient_map) - 1) * float(image[x, y]) / 255.0)
                print(gradient_map[idx], end="")
            print()
        
        cv2.imshow("bad-apple", image)
        cv2.moveWindow("bad-apple", 1000,30)
        cv2.waitKey(1)

        # frametime = abs(frametime - time.time_ns()) / pow(10, 6)
        # time.sleep((33.33 - frametime) / 1000)

        retcode, image = video.read()
        


if __name__ == "__main__":
    main()