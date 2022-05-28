import os
import os.path


def rm(file):
    if os.path.isfile(file):
        os.remove(file)
