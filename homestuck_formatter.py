# Homestuck Character Formatter by Paravellex
# Last modified 1/31/2020
# Feel free to use for your own projects

# INSTRUCTIONS FOR USE:
# Install Python.
# Save this file in the same directory as a text file containing your fic.
# Open a command terminal in that directory.
# Type the following command:
#	python homestuck_formatter.py FIC_FILE.txt
# where "FIC_FILE.txt" is replaced by whatever name your fic file is.
# The formatted fic will be located in "formatted_FIC_FILE.txt or similar.

import sys

char_dict = {
    # Humans
    'JOHN': 'john',
    'JUNE': 'john',
    'ROSE': 'rose',
    'DAVE': 'dave',
    'JADE': 'jade',
    'JANE': 'jane',
    'ROXY': 'roxy',
    'DIRK': 'dirk',
    'JAKE': 'jake',
    # Beta trolls
    'ARADIA': 'aradia',
    'TAVROS': 'tavros',
    'SOLLUX': 'sollux',
    'KARKAT': 'karkat',
    'NEPETA': 'nepeta',
    'KANAYA': 'kanaya',
    'TEREZI': 'terezi',
    'VRISKA': 'vriska',
    'EQUIUS': 'equius',
    'GAMZEE': 'gamzee',
    'ERIDAN': 'eridan',
    'FEFERI': 'feferi',
    # Alpha trolls
    'DAMARA': 'aradia',
    'RUFIOH': 'tavros',
    'MITUNA': 'sollux',
    'KANKRI': 'kankri',  # The only different one
    'MEULIN': 'nepeta',
    'PORRIM': 'kanaya',
    'LATULA': 'terezi',
    'ARANEA': 'vriska',
    'HORUSS': 'equius',
    'KURLOZ': 'gamzee',
    'CRONUS': 'eridan',
    'MEENAH': 'feferi',
    # Cherubs
    'CALLIOPE': 'calliope',  # If alt!Calliope, change to kankri
    'CALIBORN': 'caliborn',
    # Sprites (not incl. sprite^2's)
    'NANNASPRITE': 'jane',
    'JASPERSPRITE': 'jaspersprite',  # Not the same as Roxy's color!
    'DAVESPRITE': 'dirk',
    'JADESPRITE': 'jake',
    'GCATAVROSPRITE': 'john',
    'FEFETASPRITE': 'rose',
    'ARQUIUSPRITE': 'dave',
    'ERISOLSPRITE': 'jade',
    # Epilogue and HS2 characters
    '(VRISKA)': 'vriska',
    'SWIFER': 'kanaya',
    'CLIPER': 'kanaya',
    'VRISSY': 'vriska',
    'HARRY ANDERSON': 'harry',
    'HARRY': 'harry',
    # doc scratch isn't supported by this program
}

spritesquared_dict = {
    # Spritesquareds
    # Number = characters after the name to color the same
    # First string: color of the name
    # Second string: color of the speech
    'JASPROSESPRITE^2': [1, 'jaspersprite', 'rose'],
    'DAVEPETASPRITE^2': [7, 'jade', 'dirk']  # Meat 15 uses nepeta, not jade
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
    prec = line.split(':', 1)[0]  # Pre-Colon
    if prec in char_dict.keys():
        if not in_block:
            output.write("<p class=\"block\">")
            in_block = True
        else:
            output.write("<br />\n")
        output.write("<span class=\"")
        output.write(char_dict[prec])
        output.write("\">")
        output.write(line)
        output.write("</span>")
    elif prec in spritesquared_dict.keys():
        if not in_block:
            output.write("<p class=\"block\">")
            in_block = True
        else:
            output.write("<br />\n")
        output.write("<span class=\"")
        output.write(spritesquared_dict[prec][1])
        output.write("\">")
        output.write(line[:len(prec) + spritesquared_dict[prec][0]])
        output.write("</span><span class=\"")
        output.write(spritesquared_dict[prec][2])
        output.write("\">")
        output.write(line[len(prec) + spritesquared_dict[prec][0]:])
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
