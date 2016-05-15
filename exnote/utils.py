from __future__ import print_function
import os


def get_multline(ctx=None):
    if ctx:
        print(ctx)
    lines = []
    while True:
        line = raw_input()
        if line:
            lines.append(line)
        else:
            return '\n'.join(lines)


def ls(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            yield f
