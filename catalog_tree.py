import os

"""Generate dir tree"""


def dir_tree(*args):
    if len(args) == 0: #without arg app check local dir
        path = os.getcwd()
    else:
        path = args[0]
    path_deep = path.count('\\') + 1

    for relpath, dirs, files in os.walk(path):
        if relpath == ".": #to show root dir name
            relpath = path.split("\\")[-1]

        how_deep = relpath.count('\\') + 2 - path_deep #indentation to clear view
        name_of_dir = relpath.split("\\")
        print("\t" * (how_deep - 1), name_of_dir[-1] + "/")
        for f in files:
            print("\t" * how_deep, f)


dir_tree()
