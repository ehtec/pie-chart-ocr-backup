import logging
import os
import platform


# get root path
def get_root_path():

    return os.path.dirname(os.path.dirname(__file__))


# convert complex to real, throw error if imaginary part is not 0. Return orignial number if it is not a complex.
def complex_to_real(c):

    if not isinstance(c, complex):
        return c

    assert c.imag == 0

    return c.real


# find lib by keyword in search path
def find_lib(search_path, keyword):

    if not os.path.isdir(search_path):
        logging.warning("Path {0} is not a directory".format(search_path))
        return None

    files = os.listdir(search_path)

    if platform.system().upper() == "WINDOWS":
        fileext = ".dll"

    else:
        fileext = ".so"

    files = [el for el in files if el.lower().endswith(fileext)]

    files = [el for el in files if keyword in el]

    if not bool(files):
        return None

    if len(files) > 1:
        logging.warning("Multiple matches found: {0}".format(files))

    logging.info("Matching library found: {0}".format(files[0]))

    return files[0]
