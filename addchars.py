#!/bin/python

import os
import os.path
import sys
from wscript import *

charis = '../../../latn/fonts/charis_local/5.000/zip/unhinted/CharisSIL'
gentium = '../../../latn/fonts/gentium_local/basic/1.102/zip/unhinted/GenBkBas'
annapurna = '../../../deva/fonts/annapurna_local/1.203/zip/unhinted/AnnapurnaSIL-'
badami = '../badami/source'

def runCommand(cmd, filenames):
    cmd = 'ffcopyglyphs' + ' -f ' + cmd + ' ' + filenames
    print cmd
    os.system(cmd)

def findFile(filename):
    return os.path.join(sys.argv[1], filename)

def modifyFile(cmd, filename):
    tmp = 'tmp.sfd'
    os.rename(findFile(filename), tmp)
    runCommand(cmd, tmp + ' ' + findFile(filename))
    os.remove(tmp)

def modifySource(sfd, f, s, sn):
    print sfd

    if f != 'Auvaiyar':
        cmd = '-i ' + findFile(os.path.join('..', '..', 'source', 'ThiruValluvar' + s + '.sfd')) + ' --name u0B95_u0BC2'
        modifyFile(cmd, sfd)

    cmd = '-i ' + findFile(os.path.join('..', '..', 'source', 'ThiruValluvar-R.sfd')) + ' --rangefile grantha.usv --namefile grantha.name'
    modifyFile(cmd, sfd)

    asn = sn
    asn = asn.replace('BoldItalic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = '-i ' + annapurna + asn + '.ttf' + ' --rangefile cs/annapurna/main.txt'
    modifyFile(cmd, sfd)

    if f == 'Auvaiyar':
        cmd = '-i ' + charis + s + '.ttf' + ' -n uni0334.Lrg -n uni03A9 --rangefile cs/charis/pre.txt --rangefile cs/charis/main.txt'
        modifyFile(cmd, sfd)
    else:
        gs = s.replace('-', '')
        cmd = '-i ' + gentium + gs + '.ttf' + ' --namefile cs/gentium/main_glyphs.txt --rangefile cs/gentium/pre.txt --rangefile cs/gentium/main.txt'
        modifyFile(cmd, sfd)
        cmd = '-i ' + charis + s + '.ttf' + ' --rangefile cs/charis/composite4gentium.txt --rangefile cs/charis/extra4gentium.txt'
        modifyFile(cmd, sfd)

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
