# bounce.py
import os

count = 0
height = 100

while count < 10:
    height = (height*3)/5
    count = count + 1
    print(count, round(height, 4))

