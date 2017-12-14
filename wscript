# panini

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
#faces = ('Panini', 'Kautilya', 'Maurya')
#styles = ('-R', '-B', '-I', '-BI')
#stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')

faces = ('Panini',)
styles = ('-R',)
stylesName = ('Regular',)

# set build parameters
fontbase = 'source/'
generated = 'generated/'
tag = script.upper()
tuned = 'Nepali'

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        font(target = process(tag + f + '-' + sn.replace(' ', '') + '.ttf',
                cmd('psfix ${DEP} ${TGT}'),
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + s + '.sfd',
            sfd_master = fontbase + 'master.sfd',
            opentype = internal(),
            # opentype = fea(fontbase + 'master.fea', no_make = True),
            # opentype = fea(generated + f + s + '.fea',
            #     old_make_fea = True,
            #     master = fontbase + 'master.fea',
            #     make_params = '' # might need -z 8 to work around a FontForge bug
            #     ),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2 -l first',
            #    params = '-d -v2'
            #    ),
            #classes = fontbase + 'panini_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Panini', 'Kautilya', 'Maurya', 'NLCI'),
            woff = woff(),
            script= 'deva',
            fret = fret(params = '-r')
            )

        # Generate the Nepali (NEP) version from the newly created font
        font(target = process(tag + f + tuned + '-' + sn.replace(' ', '') + '.ttf',
                cmd('ttfdeflang -d NEP ${DEP} ${TGT}'),
                cmd('ttfremap -r -c ${SRC[0].bldpath()} ${DEP} ${TGT}', [fontbase + 'nepali_chars.lst']),
                name(tag + ' ' + f + ' ' + tuned, lang='en-US', subfamily=(sn))
                ),
            source = tag + f + '-' + sn + '.ttf',
            opentype = internal(),
            #graphite = internal(),
            woff = woff(),
            script = 'deva',
            fret = fret(params = '-r')
            )
