# Imports
import os  # OS library
import json
import sys


# Functions
def set_default_project_path_in_conf():
    abs_path = os.path.abspath(str(__file__) + "/../..")
    conf_name = "/config/Project_conf.json"
    conf_path = os.path.join(abs_path + conf_name)

    try:
        with open(conf_path, 'r') as json_file:
            data = json.load(json_file)
            data["base_path"] = abs_path
            create_dir(data['dirs']['data_dir'])
            create_dir(data['dirs']['doc_dir'])

        with open(conf_path, 'w') as json_file:
            json.dump(data, json_file)

    except Exception as e:
        print(f"Error locating {conf_name}")


def create_dir(dir_path, debug=False):
    """
    Creates a directory if doesn't already exist in specified path

    Parameters
    ----------
    dir_path : Path
        path to the directory
    debug : bool
        flag that controls if the result is printed
    """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        if debug:
            print("Directory ", dir_path, " Created ")
    else:
        if debug:
            print("Directory ", dir_path, " already exists")


def read_conf(relative_path="config/Project_conf.json"):
    """
    Functions that reads a json configuration file

    Parameters
    ----------
    relative_path : Path
        path to the file

    Returns
    -------
    the data loaded

    Raises
    ------
    Exception if there is an error and exits the program
    """
    abs_path = os.path.abspath(str(__file__) + "../../../" + relative_path)
    try:
        with open(abs_path, 'r') as json_file:
            return json.load(json_file)
    except Exception:
        print(f"Failed to open the path: {abs_path}")
        sys.exit(-1)
