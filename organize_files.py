import os
import sys
import shutil

"""Organize files by their extentsion"""

predefined_dirs = ["DOCUMENTS", "PICTURES", "SOURCECODES", "OTHER_FILES"]
ext_pic = ['jpg', 'png', 'bmp', 'gif']
ext_doc = ['pdf', 'doc', 'xls', 'ppt']
ext_source = ['c', 'py', 'xls']


def organize(*args):
    if len(args) == 0: #without arg app check local dir
        path = os.getcwd()
    else:
        path = args[0]

    for dir in predefined_dirs: #creating predefined dirs DOCUMENTS, ....
        os.makedirs(os.path.join(path, dir), exist_ok=True)

    folders = []
    source_file_name = os.path.basename(sys.argv[0])
    for r, d, f in os.walk(path):
        folders.append(d)
        for file in f:
            ext = file.split(".")[-1]
            print(file)
            if ext in ext_pic:
                shutil.move(os.path.join(r, file), os.path.join(path, r"PICTURES\\" + file))
            elif ext in ext_doc:
                shutil.move(os.path.join(r, file), os.path.join(path, r"DOCUMENTS\\" + file))
            elif ext in ext_source:
                if file == source_file_name: #to prevent move executing file
                    pass
                else:
                    shutil.move(os.path.join(r, file), os.path.join(path, r"SOURCECODES\\" + file))
            else:
                shutil.move(os.path.join(r, file), os.path.join(path, r"OTHER_FILES\\" + file))

    for dir in folders[0]: #delete unnecessary dirs
        if dir not in predefined_dirs:
            shutil.rmtree(os.path.join(path, dir))


organize()
