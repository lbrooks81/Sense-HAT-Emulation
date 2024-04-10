from sense_emu import SenseHat
from time import sleep

sense_emulator = SenseHat()


RGB : list = [5, 60, 60]

for i in range (9, -1, -1):
    sleep(1)    
    if i == 0:
        RGB[0] = 255
        RGB[2] = 255
    else:
        RGB[0] += 25
    sense_emulator.show_letter(f'{i}', RGB)

   