import os
import string
from fnmatch import fnmatch
from natsort import natsorted
import csv


root = './cards'
pattern = "*.png"
url = "https://github.com/oscarechobravo/mealdealv1_cards/tree/main"

header = ["label","image","item-count","item-key"]

with open('cards_v1.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    spamwriter.writerow(header)

    for path, subdirs, files in os.walk(root):
        subdirs.sort()
        for name in natsorted(files):
            if fnmatch(name, pattern):
                fname = (os.path.join(url,os.path.join(path, name)).replace("/./","/"))
                
                spamwriter.writerow([name, fname, 0, name])

            