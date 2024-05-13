import os
import string
from fnmatch import fnmatch
from natsort import natsorted
import csv


root = './cards/'
pattern = "*.png"
url = "https://oscarechobravo.github.io/mealdealv1_cards/"

header = ["label","image","item-count","item-key"]

for path, subdirs, files in os.walk(root):
    subdirs.sort()
    subdeck = (path.replace("./cards/",""))
    with open((subdeck + 'cards_v1.csv'), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        spamwriter.writerow(header)
        for name in natsorted(files):
            if fnmatch(name, pattern):
                fname = (os.path.join(url,os.path.join(path, name)).replace("/./","/"))
                
                spamwriter.writerow([name, fname, 0, name])

            