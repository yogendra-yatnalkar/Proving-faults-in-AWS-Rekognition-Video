## I don't like AWS Rekognition for videos because.... 

Before bashing AWS Rekognition, **let me set the record straight**, Rekognition for images is pretty amazing. The OCR for real-world non-document images is amazing and I have used it extensively in the past. Cool then, lets start with BASH: 

TL;DR: 
Rekognition Text-Detection is also supported for videos out of box. Once in the past, when I was on very tight time-constraint, my team decided to use it for mission critical task and we had few shocking findings which are **NOT WRITTEN IN THE DOCUMENTATION OR THE PRODUCT PAGE OR ON THE CONSOLE**.

1. It does not execute the assigned task on all the frames within the video (**which I accept but should have been written or notified somewhere !!**)

2. It does not allow users to select how many frames the user has to process per second in the input video 

3. If it is only processing 1 frame per sec, it does not even allow users to select algorithmically, which frame to process (**In my case, I wanted the least blur frame to be processed by the service**)

4. **MOST IMPORTANT** : It does not even process every second and we dont even know which frame and second will be processed and which will be not (WHY? HOW?)

To prove my above complaint, lets quickly run a small experiment: 

1. 
- 