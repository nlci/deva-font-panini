#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO

## double danda
if font.info.familyName == 'Maurya':
    keep = font['dandadbl.ps']
    remove = font['dandadbl.tt']
else:
    keep = font['dandadbl.tt']
    remove = font['dandadbl.ps']

keep.name = 'dandadbl'
keep.unicodes = [0x0965]

remove.name = 'dandas'

# Save UFO
font.changed()
font.save()
font.close()
