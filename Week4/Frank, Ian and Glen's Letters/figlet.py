from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) < 2:
    x = input("Input: ")
    figlet.setFont(font = random.choice(fonts))
    print(f"Output: {figlet.renderText(x)}")
elif len(sys.argv) < 4 and sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
    x = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(f"Output: \n{figlet.renderText(x)}")
else:
    sys.exit("Invalid Text")




