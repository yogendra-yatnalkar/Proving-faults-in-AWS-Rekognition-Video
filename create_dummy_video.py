import cv2
import numpy
import numpy as np

# constants
width, height = 512, 512
fps = 4

# list of numbers
numbers_li = []
for i in range(9,-1,-1):
    numbers_li.append(i)
print(numbers_li)

# creating a video
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('reverse_numbers_5_fps.mp4', fourcc, fps, (width, height))

for i in range(7):
    for num in numbers_li:

        img = np.zeros((width, height,3), dtype = np.uint8) + (255, 255, 255)
        img = img.astype(np.uint8)

        # adding number
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(num), (50, 300), font, 3, (0,0,255), 5, cv2.LINE_AA)

        # adding it to the video
        video.write(img)
video.release()

# rekognition-video/ => ffmpeg -i .\reverse_numbers_4_fps.mp4 -c:v libx264 reverse_numbers_4_fps_h264.mp4

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

