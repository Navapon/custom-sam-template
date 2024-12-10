#!/usr/bin/env python3
from __future__ import print_function

import os
import subprocess

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"

def main():

    project_name = '{{ cookiecutter.project_slug }}'

    print(SUCCESS +
          "Project initialized successfully! You can now jump to {} folder".
          format(project_name) + TERMINATOR)
    print(INFO +
          "{}/README.md contains instructions on how to proceed.".
          format(project_name) + TERMINATOR)


if __name__ == '__main__':

    main()
    command = "git init && git branch -M main && git add . && git commit -m \"chore: initiaive project lambda\""
    response = subprocess.run(command, capture_output=True, shell=True)
    print(response.stdout.decode())
