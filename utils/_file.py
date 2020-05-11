import glob
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
    try:
        profile = f'{dirName}profile'
        os.mkdir(profile)
    except FileExistsError:
        pass


def exit_files(dirName, filename, mimetype):
    type = mimetypes.guess_extension(mimetype)
    if type:
        type
    else:
        type = '.unknow'
    path_to_file_list = glob.glob(dirName + '*' + type)
    for path_to_file in path_to_file_list:
        if path_to_file == filename:
            return False
    return True
