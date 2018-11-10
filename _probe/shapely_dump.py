import os
import _pickle as pkl


# load watching path
config_file_path = os.path.join(os.path.dirname(__file__), "config")
with open(config_file_path, "rb") as fp:
    info_dict = pkl.load(fp)

watching_path = info_dict.get("watching_path", "")

