import _pickle as pkl
import json
import os

# load watching path
config_file_path = os.path.join(os.path.dirname(__file__), "_config")
with open(config_file_path, "rb") as fp:
    info_dict = pkl.load(fp)

collect_path = info_dict.get("collect_path", "")


def collect_as_json(obj, filename: str):
    with open(filename, "w") as fp:
        json.dump(obj, fp)
