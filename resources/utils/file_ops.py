import os
import json
from time import time
from yaml import safe_load


def get_yaml(curr_file, relative_file_path):
    file_path = (os.path.join(os.path.dirname(curr_file), relative_file_path))
    with open(file_path) as f:
        data = dict(json.loads(json.dumps(safe_load(f))))
    return data


def generate_customer(customer_template):
    timestamp = str(int(time()))
    test_customer = customer_template
    test_customer['email'] = test_customer['email'].replace('{placeholder}', timestamp)
    test_customer['password'] = test_customer['password'].replace('{placeholder}', timestamp)
    return test_customer
