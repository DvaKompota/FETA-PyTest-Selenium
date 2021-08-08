import os
import json
from yaml import safe_load


def get_yaml(curr_file, relative_file_path):
    file_path = (os.path.join(os.path.dirname(curr_file), relative_file_path))
    with open(file_path) as f:
        data = dict(json.loads(json.dumps(safe_load(f))))
    return data
