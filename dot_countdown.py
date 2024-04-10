from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
X = [0, 0, 0]
s : int = 10

timer : list = []

for i in range (0, 64):
    timer.append(X)
    
    
# Green
for i in range (0, s):
    timer[i] = G
    sense.set_pixels(timer)

# Red
for i in range (0, s):
    timer[i] = R
    sleep(1)
    sense.set_pixels(timer)

for i in range(0, 10):
    sense.clear()
    sleep(0.1)
    sense.set_pixels(timer)
    sleep(0.1)   