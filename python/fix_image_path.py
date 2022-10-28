import os 
import markdown
import re 

path = '/Users/josh/Dropbox/Coding/Github/sk-blog/scribbles'

exclude = ['out-of-the-woods.md']
files = os.listdir(path)

for fillo in files:
    if (".md" in fillo) and (fillo not in exclude):
        stem = fillo
        fillo_path = path + '/' + stem

        f = open(fillo_path, 'r')
        fileString = f.read()

        fileString = fileString.replace("image/", "/")

        # print(fileString)

        with open(f'{path}/{stem}', 'w') as f:
            f.write(fileString)

        # print(stem)


    # print(files)