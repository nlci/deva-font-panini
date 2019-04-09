#!/bin/bash

face="$1"
style="$2"
ufo="$3"

deva="../../../../deva/fonts/panini-master/source/"

psfcopyglyphs -f --rename rename --unicode usv -i ../cs/panini/main4deva.csv -s "${deva}/${face}-${style}.ufo" ${ufo}
