from os import walk
mypath = "cards"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break