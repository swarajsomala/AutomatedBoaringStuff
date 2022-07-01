#!/bin/python
import os
import re

HEADER_REGEX = re.compile(
    r"#ifndef +([a-zA-z0-9]+)\n *#define +([a-zA-z0-9]+)")
HEADER_EXTENSION = ".h"


def get_header_files(path):
    headers = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(HEADER_EXTENSION):
                headers.append(os.path.join(root, file))
    return headers


def filter_gaurds(file_list):
    for file_name in file_list:
        code = None
        with open(file_name) as f:
            code = f.read()
        if re.search(HEADER_REGEX, code) is not None:
            for match in re.finditer(HEADER_REGEX, code):
                if len(match.groups()) != 2:
                    print(file_name, " : Header Gaurds found but count should be 2")
                    return -1
                else:
                    if match.group(1) == match.group(2):
                        # print(match.group(1))
                        # print(match.group(2))
                        print("Headers are matched !!!")
                        return 0
                    else:
                        print(file_name, " : Header Gaurds are not matching")
                        return -1
        else:
            print(file_name, " : No Header Gaurds found")
            return 0


PATH = "/workspaces/AutomatedBoaringStuff/header_gaurd_validator"
header_files = get_header_files(PATH)
filter_gaurds(header_files)
