#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO

## double danda
if font.info.familyName == 'Maurya':
    keep = font['u0965.ps']
    remove = font['u0965.tt']
else:
    keep = font['u0965.tt']
    remove = font['u0965.ps']

keep.name = 'u0965'
keep.unicode = 0x0965
keep.unicodes = [keep.unicode]

remove.name = 'dandas'

## Omega
greek = font['uni03A9']
greek.unicode = 0x03A9
greek.unicodes = [greek.unicode]

# Save UFO
font.changed()
font.save()
font.close()
