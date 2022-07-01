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
        matches = re.findall(HEADER_REGEX, code)
        if not bool(matches):
            print(file_name, " : No Header Gaurds found")
            return
        if len(matches) != 3:
            print(file_name, " : Header Gaurds found but count should be 3")
            return
        for match in re.finditer(HEADER_REGEX, code):
            if match.group(1) == match.group(2) == match.group(3):
            # d[match.group(1)] = re.sub(r"(?:^|[\r\n]+)\s*\*\s*", "", match.group(2)[:-2].strip())
                print(match.group(1))
                print(match.group(2))
            else:
                print(file_name, " : Header Gaurds are not matching")


PATH = "/workspaces/AutomatedBoaringStuff/header_gaurd_validator"
header_files = get_header_files(PATH)
filter_gaurds(header_files)
