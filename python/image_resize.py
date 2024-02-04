# %%

from PIL import Image, ImageOps
import os 

# %%

# pathos = '/Users/josh/Downloads/to_resize/'
# out_path = '/Users/josh/Downloads/resized/'

pathos = 'static/'
out_path = 'static/'

# pathos = 'new_imgs/'
# out_path = 'new_imgs/'

backup_pathos = 'image_backups/'
already_done = os.listdir(backup_pathos)

include = ['.jpg', '.jpeg', 'png', '.heic']

fillos = os.listdir(pathos)
fillos = [x for x in fillos if x != '.DS_Store']

to_process = []

for thing in fillos:
    for endo in include:
        if endo in thing:
            to_process.append(thing)


for file in to_process:
    inter = f"{pathos}{file}"
    stats = os.stat(inter)

    if ".heic" in file:
        # Open HEIF or HEIC file
        im = Image.open(inter)

        # Convert to JPEG
        im.convert('RGB')  

    else:
        im = Image.open(inter)
        
    im = ImageOps.exif_transpose(im)

    if file not in already_done:

        im.save(f'{backup_pathos}{file}')
        print("Copied: ", file)

    if (stats.st_size / (1024 * 1024)) > 1:
        print(f"{file} MB:", (stats.st_size / (1024 * 1024)))       

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
