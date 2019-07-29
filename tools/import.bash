#!/bin/bash

face="$1"
style="$2"
ufo="$3"

deva="../../../../deva/fonts/panini-master/source/"
if [ "${face}" = "Maurya" ]
then
    tamlf="Vaigai"
else
    tamlf="ThiruValluvar"
fi

psfcopyglyphs -f --rename rename --unicode usv -i ../cs/panini/main4deva.csv -s "${deva}/${face}-${style}.ufo" ${ufo}
psfcopyglyphs -f --rename rename --unicode usv -i ../cs/thiruvalluvar/main.csv -s "${taml}/${tamlf}-${style}.ufo" ${ufo}
