import math 
import random

f = open('intro.ppm', 'w')

lines = "P3 500 500 255 "

for i in range(500):
    for j in range(500):
        red = (random.randint(1,100) * 256) % (int(math.sqrt(i*j)/3)+10)
        blue = (random.randint(1,100) * 256) % (int(math.sqrt(i*j)/3)+10)
        green = (random.randint(1,100) * 256) % (int(math.sqrt(i*j)/3)+10)
        lines += str(red) + ' ' + str(blue) + ' ' + str(green) + ' '
    lines += '\n'

f.write(lines)
f.close()
