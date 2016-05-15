from __future__ import print_function

import os
from ConfigParser import SafeConfigParser
from config import cfg
from utils import ls
from note import Note


class Container:
    def __init__(self):
        self._clean()

    def _clean(self):
        for note in ls(cfg['path']):
            if note not in ls(os.path.join(cfg['path'], ".meta")):
                n = Note(note)
                n.create_meta()
        for meta in ls(os.path.join(cfg['path'], ".meta")):
            if meta not in ls(cfg['path']):
                os.remove(os.path.join(cfg['path'], ".meta", meta))

    def list(self, tags=None):
        for i, note in enumerate(ls(os.path.join(cfg['path'], ".meta"))):
            if not tags:
                print(note)
            else:
                _tags = Note(note)._get_tags()
                for t in tags.split(','):
                    if t in _tags:
                        print(note)
