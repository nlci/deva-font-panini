#!/usr/bin/python3
# this is a smith configuration file

# panini

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-p'}, # do not run psfix on the final fonts
    {'opt' : '-s'}  # only build a single font
    )

import os2

# override the default folders
DOCDIR = ['documentation', 'web']

# set meta-information
script='deva'
APPNAME='nlci-' + script

DESC_SHORT='Devanagari Unicode font with OT and Graphite support'
DESC_NAME='NLCI-' + script
getufoinfo('source/Panini-Regular.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# set fonts to build
faces = ('Panini', 'Kautilya', 'Maurya')
facesLegacy = ('PANI', 'KAUT', 'MAUR')
styles = ('-R', '-B', '-I', '-BI')
stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')
stylesLegacy = ('', 'BD', 'I', 'BI')

if '-s' in opts:
    faces = (faces[0],)
    facesLegacy = (facesLegacy[0],)
    styles = (styles[0],)
    stylesName = (stylesName[0],)
    stylesLegacy = (stylesLegacy[0],)

# set build parameters
fontbase = 'source/'
archive = fontbase + 'archive/unhinted/'
generated = 'generated/'
tag = script.upper()

panose = [2, 0, 0, 3]
codePageRange = [0, 29]
unicodeRange = [0, 1, 2, 3, 4, 5, 6, 7, 15, 29, 31, 32, 33, 35, 38, 39, 40, 45, 60, 62, 67, 69, 91]
hackos2 = os2.hackos2(panose, codePageRange, unicodeRange)

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            font(target = process('ufo/' + f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd(hackos2 + ' ${DEP} ${TGT}'),
                    name(f, lang='en-US', subfamily=(sn))
                    ),
                source = legacy(f + s + '.ttf',
                                source = archive + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'panini_annapurna.xml',
                                params = '',
                                noap = '')
                )

if '-l' in opts:
    faces = list()
for f in faces:
    p = package(
        appname = APPNAME + '-' + f.lower(),
        version = VERSION,
        docdir = DOCDIR # 'documentation'
    )
    for dspace in ('Roman', 'Italic'):
        d = designspace('source/' + f + dspace + '.designspace',
            target = process('${DS:FILENAME_BASE}.ttf',
                cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo'])
            ),
            opentype=fea(generated + '${DS:FILENAME_BASE}.gdl',
                mapfile = generated + '${DS:FILENAME_BASE}.map',
                master = fontbase + 'master.feax',
                make_params = ''
                ),
            #graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2',
            #    params =  '-e ${DS:FILENAME_BASE}_gdlerr.txt'
            #    ),
            #classes = fontbase + 'panini_classes.xml',
            #ap = generated + '${DS:FILENAME_BASE}.xml',
            version = VERSION,
            woff = woff('woff/${DS:FILENAME_BASE}', type='woff2',
                metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
            script= 'dev2', # 'deva'
            package = p,
            pdf = fret(params = '-r -oi')
            )
