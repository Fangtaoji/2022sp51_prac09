COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "	#f0f8ff", "Alizarin crimson": "	#e32636", "Amaranth": "#e52b50",
          "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "	#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff", "Aquamarine1": "#7fffd4"}
name = input("Please input the colour name")
while name != "":
    print('The colour {} you choose is {}'.format(name,COLOUR[name]))
    break
