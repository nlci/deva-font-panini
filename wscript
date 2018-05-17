# panini

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-s'}  # only build a single font
    )

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='deva'
APPNAME='nlci-' + script
VERSION='0.100'
TTF_VERSION='0.100'
COPYRIGHT='Copyright (c) 2009-2015, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Devanagari Unicode font with OT and Graphite support'
DESC_LONG='''
Pan Devanagari font designed to support all the languages using the Devanagari script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0915'

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
archive = fontbase + 'archive/'
generated = 'generated/'
tag = script.upper()

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            gentium = '../../../../latn/fonts/gentium_local/basic/1.102/zip/unhinted/2048/GenBkBas' + s.replace('-', '') + '.ttf'
            charis = '../../../../latn/fonts/charis_local/5.000/zip/unhinted/2048/CharisSIL' + s + '.ttf'
            font(target = process('ufo/' + f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd('cp ${DEP} ${TGT}'),
                    name(f, lang='en-US', subfamily=(sn))
                    ),
                source = legacy(f + s + '.ttf',
                                source = archive + 'unhinted/' + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'panini_annapurna.xml',
                                params = '-f ' + charis,
                                noap = '')
                )

if '-l' in opts:
    faces = list()
for f in faces:
    for (s, sn) in zip(styles, stylesName):
        snf = '-' + sn.replace(' ', '')
        fontfilename = tag + f + snf
        font(target = process(fontfilename + '.ttf',
                cmd('psfix ${DEP} ${TGT}'),
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + snf + '.ufo',
            # opentype = fea(fontbase + 'master.fea', no_make = True),
            # opentype = fea(generated + f + s + '.fea',
            #     old_make_fea = True,
            #     master = fontbase + 'master.fea',
            #     make_params = ''
            #     ),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2 -l first',
            #    params = '-d -v2'
            #    ),
            #classes = fontbase + 'panini_classes.xml',
            ap = generated + f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Panini', 'Kautilya', 'Maurya', 'NLCI'),
            woff = woff(),
            script= 'deva',
            fret = fret(params = '')
            )
