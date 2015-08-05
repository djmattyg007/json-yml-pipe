#!/usr/bin/python3

import os, sys
import json, yaml

def die(msg, err_code = 1):
    sys.stderr.write(msg)
    sys.exit(err_code)

if len(sys.argv) < 2:
    die("No file supplied", 1)
elif os.access(sys.argv[1], os.R_OK) == False:
    die("File does not exist or is not readable", 2)

json_filepath = sys.argv[1]
json_filename, json_fileext = os.path.splitext(json_filepath)
if not json_fileext == ".json":
    die("File is not JSON", 3)
elif os.access(json_filename + ".yml", os.R_OK) == True:
    die("YML file already exists for matching JSON file", 4)

with open(json_filepath, "r") as json_file:
    data = json.load(json_file)

yml_filename = json_filename + ".yml"
os.mkfifo(yml_filename)

with open(yml_filename, "w") as pipe_fd:
    yaml.dump(data, pipe_fd)

os.remove(yml_filename)
