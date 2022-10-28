import os 
import markdown
import re 

# path = '/Users/josh/Dropbox/Coding/Github/blog/micro-scribble'
path = '/Users/josh/Dropbox/Coding/Github/blog/scribbles'

exclude = ['out-of-the-woods.md']
files = os.listdir(path)

for fillo in files:
    if (".md" in fillo) and (fillo not in exclude):
        stem = fillo
        fillo_path = path + '/' + stem

        f = open(fillo_path, 'r')
        fileString = f.read()
        # htmlmarkdown= markdown.markdown( fileString )



        # print(htmlmarkdown)
        title_pattern = r'title:.+\s'
        title = re.search(title_pattern, fileString)[0].replace('title: ', '').strip()
        print(stem)
        print(title)

        fileString = fileString.replace("'Scribble image'", title)

        urlo_pattern = r'\'\/img.+\''
        urlo = re.search(urlo_pattern, fileString)[0].replace("'/img/", 'image/').replace("'", '')


        fileString = re.sub(r'{{.+}}\s{0,1}', urlo, fileString)

        fileString = fileString.replace("<br>", "")

        # print(fileString)

        with open(f'/Users/josh/Dropbox/Coding/Github/sk-blog/scribbles/{stem}', 'w') as f:
            f.write(fileString)

        # print(stem)


    # print(files)