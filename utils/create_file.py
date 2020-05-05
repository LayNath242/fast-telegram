import mimetypes
import os


def create_filename(direName, fileName, minetype):
    type = mimetypes.guess_extension(minetype)
    if type:
        filename = f'{direName}{fileName}{type}'
    else:
        filename = f'{direName}{fileName}.unknow'
    return filename


def create_new_dir(dirName):
    dir = './Chat'
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass
    try:
        os.mkdir(dirName)
    except FileExistsError:
        pass
