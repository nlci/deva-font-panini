#!/usr/bin/python3

Vowels = [
    0x0904,  # DEVANAGARI LETTER SHORT A
    0x0905,  # DEVANAGARI LETTER A
    0x0906,  # DEVANAGARI LETTER AA
    0x0907,  # DEVANAGARI LETTER I
    0x0908,  # DEVANAGARI LETTER II
    0x0909,  # DEVANAGARI LETTER U
    0x090A,  # DEVANAGARI LETTER UU
    0x090B,  # DEVANAGARI LETTER VOCALIC R
    0x090C,  # DEVANAGARI LETTER VOCALIC L
    0x090D,  # DEVANAGARI LETTER CANDRA E
    0x090E,  # DEVANAGARI LETTER SHORT E
    0x090F,  # DEVANAGARI LETTER E
    0x0910,  # DEVANAGARI LETTER AI
    0x0911,  # DEVANAGARI LETTER CANDRA O
    0x0912,  # DEVANAGARI LETTER SHORT O
    0x0913,  # DEVANAGARI LETTER O
    0x0914,  # DEVANAGARI LETTER AU
    0x0960,  # DEVANAGARI LETTER VOCALIC RR
    0x0961,  # DEVANAGARI LETTER VOCALIC LL
    0x0972,  # DEVANAGARI LETTER CANDRA A
    0x0973,  # DEVANAGARI LETTER OE
    0x0974,  # DEVANAGARI LETTER OOE
    0x0975,  # DEVANAGARI LETTER AW
    0x0976,  # DEVANAGARI LETTER UE
    0x0977,  # DEVANAGARI LETTER UUE
    ]

Matras = [
    0x093A,  # DEVANAGARI VOWEL SIGN OE
    0x093B,  # DEVANAGARI VOWEL SIGN OOE
    0x093E,  # DEVANAGARI VOWEL SIGN AA
    0x093F,  # DEVANAGARI VOWEL SIGN I
    0x0940,  # DEVANAGARI VOWEL SIGN II
    0x0941,  # DEVANAGARI VOWEL SIGN U
    0x0942,  # DEVANAGARI VOWEL SIGN UU
    0x0943,  # DEVANAGARI VOWEL SIGN VOCALIC R
    0x0944,  # DEVANAGARI VOWEL SIGN VOCALIC RR
    0x0945,  # DEVANAGARI VOWEL SIGN CANDRA E
    0x0946,  # DEVANAGARI VOWEL SIGN SHORT E
    0x0947,  # DEVANAGARI VOWEL SIGN E
    0x0948,  # DEVANAGARI VOWEL SIGN AI
    0x0949,  # DEVANAGARI VOWEL SIGN CANDRA O
    0x094A,  # DEVANAGARI VOWEL SIGN SHORT O
    0x094B,  # DEVANAGARI VOWEL SIGN O
    0x094C,  # DEVANAGARI VOWEL SIGN AU
    0x094E,  # DEVANAGARI VOWEL SIGN PRISHTHAMATRA E
    0x094F,  # DEVANAGARI VOWEL SIGN AW
    0x0955,  # DEVANAGARI VOWEL SIGN CANDRA LONG E
    0x0956,  # DEVANAGARI VOWEL SIGN UE
    0x0957,  # DEVANAGARI VOWEL SIGN UUE
    0x0962,  # DEVANAGARI VOWEL SIGN VOCALIC L
    0x0963,  # DEVANAGARI VOWEL SIGN VOCALIC LL
    ]

Consonants = [
    0x0915,  # DEVANAGARI LETTER KA
    0x0916,  # DEVANAGARI LETTER KHA
    0x0917,  # DEVANAGARI LETTER GA
    0x0918,  # DEVANAGARI LETTER GHA
    0x0919,  # DEVANAGARI LETTER NGA
    0x091A,  # DEVANAGARI LETTER CA
    0x091B,  # DEVANAGARI LETTER CHA
    0x091C,  # DEVANAGARI LETTER JA
    0x091D,  # DEVANAGARI LETTER JHA
    0x091E,  # DEVANAGARI LETTER NYA
    0x091F,  # DEVANAGARI LETTER TTA
    0x0920,  # DEVANAGARI LETTER TTHA
    0x0921,  # DEVANAGARI LETTER DDA
    0x0922,  # DEVANAGARI LETTER DDHA
    0x0923,  # DEVANAGARI LETTER NNA
    0x0924,  # DEVANAGARI LETTER TA
    0x0925,  # DEVANAGARI LETTER THA
    0x0926,  # DEVANAGARI LETTER DA
    0x0927,  # DEVANAGARI LETTER DHA
    0x0928,  # DEVANAGARI LETTER NA
    0x0929,  # DEVANAGARI LETTER NNNA
    0x092A,  # DEVANAGARI LETTER PA
    0x092B,  # DEVANAGARI LETTER PHA
    0x092C,  # DEVANAGARI LETTER BA
    0x092D,  # DEVANAGARI LETTER BHA
    0x092E,  # DEVANAGARI LETTER MA
    0x092F,  # DEVANAGARI LETTER YA
    0x0930,  # DEVANAGARI LETTER RA
    0x0931,  # DEVANAGARI LETTER RRA
    0x0932,  # DEVANAGARI LETTER LA
    0x0933,  # DEVANAGARI LETTER LLA
    0x0934,  # DEVANAGARI LETTER LLLA
    0x0935,  # DEVANAGARI LETTER VA
    0x0936,  # DEVANAGARI LETTER SHA
    0x0937,  # DEVANAGARI LETTER SSA
    0x0938,  # DEVANAGARI LETTER SA
    0x0939,  # DEVANAGARI LETTER HA
    0x0958,  # DEVANAGARI LETTER QA
    0x0959,  # DEVANAGARI LETTER KHHA
    0x095A,  # DEVANAGARI LETTER GHHA
    0x095B,  # DEVANAGARI LETTER ZA
    0x095C,  # DEVANAGARI LETTER DDDHA
    0x095D,  # DEVANAGARI LETTER RHA
    0x095E,  # DEVANAGARI LETTER FA
    0x095F,  # DEVANAGARI LETTER YYA
    0x0978,  # DEVANAGARI LETTER MARWARI DDA
    0x0979,  # DEVANAGARI LETTER ZHA
    0x097A,  # DEVANAGARI LETTER HEAVY YA
    0x097B,  # DEVANAGARI LETTER GGA
    0x097C,  # DEVANAGARI LETTER JJA
    0x097E,  # DEVANAGARI LETTER DDDA
    0x097F,  # DEVANAGARI LETTER BBA
    ]

Nukta = [
    0x093C,  # DEVANAGARI SIGN NUKTA
    ]

Virama = [
    0x094D,  # DEVANAGARI SIGN VIRAMA
    ]

Digits = [
    0x0966,  # DEVANAGARI DIGIT ZERO
    0x0967,  # DEVANAGARI DIGIT ONE
    0x0968,  # DEVANAGARI DIGIT TWO
    0x0969,  # DEVANAGARI DIGIT THREE
    0x096A,  # DEVANAGARI DIGIT FOUR
    0x096B,  # DEVANAGARI DIGIT FIVE
    0x096C,  # DEVANAGARI DIGIT SIX
    0x096D,  # DEVANAGARI DIGIT SEVEN
    0x096E,  # DEVANAGARI DIGIT EIGHT
    0x096F,  # DEVANAGARI DIGIT NINE
    ]

vowels = list(map(chr, Vowels))
matras = list(map(chr, Matras))
consonants = list(map(chr, Consonants))
n = nukta = list(map(chr, Nukta))[0]
h = virama = list(map(chr, Virama))[0]
digits = list(map(chr, Digits))
