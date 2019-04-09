#!/usr/bin/python3

from addcharslib import *

for f in faces:

    workshop = 1.4
    if f == 'Maurya':
        upm = 1000.0/2048.0
    else:
        upm = 1.0
    scale = str(upm/workshop)

    for sn in stylesName:
        modifyFile(scale, 'charis', f, sn)
