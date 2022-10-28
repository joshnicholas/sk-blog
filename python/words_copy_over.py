import os 
import markdown
import re 

# path = '/Users/josh/Dropbox/Coding/Github/blog/micro-scribble'
# path = '/Users/josh/Dropbox/Coding/Github/blog/scribbles'
path = '/Users/josh/Dropbox/Coding/Github/blog/words'

exclude = ['out-of-the-woods.md']
files = os.listdir(path)

for fillo in files:
    if (".md" in fillo) and (fillo not in exclude):
        stem = fillo
        fillo_path = path + '/' + stem

        f = open(fillo_path, 'r')
        fileString = f.read()

        fileString = fileString.replace("<br>", "")

        # print(fileString)

        with open(f'/Users/josh/Dropbox/Coding/Github/sk-blog/words/{stem}', 'w') as f:
            f.write(fileString)

        # print(stem)


    # print(files)