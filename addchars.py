#!/bin/python

import os
import os.path
import sys

from wscript import *

charis = '../../../latn/fonts/charis_local/5.000/zip/unhinted/CharisSIL'
gentium = '../../../latn/fonts/gentium_local/basic/1.102/zip/unhinted/GenBkBas'
annapurna = '../../../deva/fonts/annapurna_local/1.203/zip/unhinted/AnnapurnaSIL-'
panini = '../../../deva/fonts/panini-master/source/Panini'
exo = '../../../latn/fonts/exo/1.500/zip/unhinted/1000/Exo-'

def runCommand(cmd, ifont, ofont):
    cmd = 'ffcopyglyphs' + ' -f ' + cmd + ' ' + ifont + ' ' + ofont
    print cmd
    os.system(cmd)

def findFile(filename):
    return os.path.join(sys.argv[1], filename)

def modifyFile(cmd, filename):
    tmp = 'tmp.sfd'
    os.rename(findFile(filename), tmp)
    runCommand(cmd, tmp, findFile(filename))
    os.remove(tmp)

def modifySource(sfd, f, s, sn):
    print sfd

    latin = 1.4
    if f == 'Maurya':
        upm = 1000.0/2048.0
    else:
        upm = 1.0
    scale = '-s ' + str(upm/latin) + ' '

    ps = s
    ps = ps.replace('-BI', '-B')
    cmd = scale + '-i ' + panini + ps + '.sfd' + ' --rangefile cs/panini/main4knda.txt'
    modifyFile(cmd, sfd)

    asn = sn
    asn = asn.replace('BoldItalic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = scale + '-i ' + annapurna + asn + '.ttf' + ' --rangefile cs/annapurna/main.txt'
    modifyFile(cmd, sfd)

    cmd = scale + '-i ' + charis + s + '.ttf' + ' -n uni0334.Lrg -n uni03A9 --rangefile cs/charis/pre.txt --rangefile cs/charis/main.txt'
    modifyFile(cmd, sfd)

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
