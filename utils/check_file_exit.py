import mimetypes
import glob


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
