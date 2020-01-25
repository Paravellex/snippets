# Homestuck Character Formatter by Paravellex
# Last modified 1/24/2020
# Feel free to use for your own projects

import sys

char_dict = {
    # Humans
    'JOHN:': 'john',
    'ROSE:': 'rose',
    'DAVE:': 'dave',
    'JADE:': 'jade',
    'JANE:': 'jane',
    'ROXY:': 'roxy',
    'DIRK:': 'dirk',
    'JAKE:': 'jake',
    # Beta trolls
    'ARADIA:': 'aradia',
    'TAVROS:': 'tavros',
    'SOLLUX:': 'sollux',
    'KARKAT:': 'karkat',
    'NEPETA:': 'nepeta',
    'KANAYA:': 'kanaya',
    'TEREZI:': 'terezi',
    'VRISKA:': 'vriska',
    'EQUIUS:': 'equius',
    'GAMZEE:': 'gamzee',
    'ERIDAN:': 'eridan',
    'FEFERI:': 'feferi',
    # Alpha trolls
    'DAMARA:': 'aradia',
    'RUFIOH:': 'tavros',
    'MITUNA:': 'sollux',
    'KANKRI:': 'kankri',  # The only different one
    'MEULIN:': 'nepeta',
    'PORRIM:': 'kanaya',
    'LATULA:': 'terezi',
    'ARANEA:': 'vriska',
    'HORUSS:': 'equius',
    'KURLOZ:': 'gamzee',
    'CRONUS:': 'eridan',
    'MEENAH:': 'feferi',
    # Cherubs
    'CALLIOPE:': 'calliope',  # If alt!Calliope, change to Kankri
    'CALIBORN:': 'caliborn',
    # Sprites (not incl. sprite^2's)
    'NANNASPRITE:': 'jane',
    'JASPERSPRITE:': 'jaspersprite',  # Not the same as Roxy's color!
    'DAVESPRITE:': 'dirk',
    'JADESPRITE:': 'jake',
    'GCATAVROSPRITE:': 'john',
    'FEFETASPRITE:': 'rose',
    'ARQUIUSPRITE:': 'dave',
    'ERISOLSPRITE:': 'jade',
    # Epilogue and HS2 characters
    '(VRISKA):': 'vriska',
    'SWIFER:': 'kanaya',
    'CLIPER:': 'kanaya',
    'VRISSY:': 'vriska',
    'HARRY ANDERSON:': 'harry',
    'HARRY:': 'harry',
    # doc scratch isn't supported by this program
}

spritesquared_dict = {
    # Spritesquareds
    # Number = characters after the colon to color the same as the name
    # First string: color of the name
    # Second string: color of the speech
    'JASPROSESPRITE^2:': [0, 'jaspersprite', 'rose'],
    'DAVEPETASPRITE^2:': [6, 'jade', 'dirk']
}

input = open(sys.argv[1], 'r', encoding="utf8")
output = open("formatted_" + sys.argv[1], 'w')

in_block = False

for line_raw in input:
    if line_raw == '\n':
        output.write("</p>\n\n")
        in_block = False
        continue
    line = line_raw.rstrip()
    word = line.split(' ', 1)[0]
    if word in char_dict.keys():
        if not in_block:
            output.write("<p class=\"block\">")
            in_block = True
        else:
            output.write("<br />\n")
        output.write("<span class=\"")
        output.write(char_dict[word])
        output.write("\">")
        output.write(line)
        output.write("</span>")
    elif word in spritesquared_dict.keys():
        if not in_block:
            output.write("<p class=\"block\">")
            in_block = True
        else:
            output.write("<br />\n")
        output.write("<span class=\"")
        output.write(spritesquared_dict[word][1])
        output.write("\">")
        output.write(line[:len(word) + spritesquared_dict[word][0]])
        output.write("</span><span class=\"")
        output.write(spritesquared_dict[word][2])
        output.write("\">")
        output.write(line[len(word) + spritesquared_dict[word][0]:])
        output.write("</span>")
    else:
        if in_block:
            output.write("ERROR on line:" + line)
            break
        output.write("<p class=\"narrative\">")
        output.write(line)
output.write("</p>")
input.close()
output.close()
