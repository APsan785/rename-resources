import os
import sys

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

illegal_char = list(r"[:<>|\"'/*?]()-@!+= ")


def rename_file(path_):
    path_ = path_.replace("\t", "/t")
    path_ = path_.replace("\n", "/n")
    path_ = path_.replace("\\", "/")

    path = path_
    dot_loc = path.rfind(".")
    backslash_loc = path.rfind("/")
    name = path[backslash_loc + 1: dot_loc]

    new_name = name.lower()

    if num_list.__contains__(name[0]):
        new_name = "r_" + new_name[1:]

    for i in new_name:
        if i in illegal_char:
            new_name = replace_character(i, new_name, "_")

    replace_path = path.replace(name, new_name)

    os.replace(path, replace_path)

    if(name!=new_name):
        print("File name changed from %s to %s" % (name, new_name))
    else:
        print("The name %s was well and good" % name)


def replace_character(char, string, new_char):
    return string.replace(char, new_char)


# code to run
for filePath in sys.argv[1:]:
    rename_file(filePath)

print("\nOperation Done!!\n")
