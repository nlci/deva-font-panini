#!/bin/python

from addcharslib import *

def modifySource(sfd, f, s, sn):
    print sfd

    workshop = 1.4
    if f == 'Maurya':
        upm = 1000.0/2048.0
    else:
        upm = 1.0
    scale = '-s ' + str(upm/workshop) + ' '
    scaleSrc = scale

    ps = s
    ps = ps.replace('-BI', '-B')
    cmd = scaleSrc + '-i ' + panini + ps + '.sfd' + ' --rangefile cs/panini/main4knda.txt'
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
