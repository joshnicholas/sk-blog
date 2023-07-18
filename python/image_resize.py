# %%

from PIL import Image, ImageOps
import os 

# %%

pathos = '/Users/josh/Downloads/to_resize/'
out_path = '/Users/josh/Downloads/resized/'

fillos = os.listdir(pathos)
fillos = [x for x in fillos if x != '.DS_Store']
print(fillos)

for file in fillos:
    inter = f"{pathos}{file}"
    stats = os.stat(inter)

    print(f"{file} MB:", (stats.st_size / (1024 * 1024)))

    im = Image.open(inter)
    im = ImageOps.exif_transpose(im)
    w, h = im.size
    print('width: ', w)
    print('height:', h)

    new_w = int(w/3)
    new_h = int(h/3)

    new_image = im.resize((new_w, new_h))

    w, h = new_image.size
    print('new width: ', w)
    print('new height:', h)

    new_image.save(f'{out_path}{file}')

    new_stats = os.stat(f'{out_path}{file}')

    print(f"{file} MB:", (new_stats.st_size / (1024 * 1024)))



# %%
