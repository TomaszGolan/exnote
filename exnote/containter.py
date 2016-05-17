from __future__ import print_function

import os
from ConfigParser import SafeConfigParser
from config import cfg
from utils import ls
from note import Note


def tag_or_no(tags):
    if not tags:
        return ''
    return "#" + ' #'.join(tags)


class Container:
    def __init__(self):
        self._clean()
        self._notes = {}
        for note in ls(cfg['path']):
            n = Note(note)
            self._notes[note] = n.get_meta()

    def _clean(self):
        for meta in ls(os.path.join(cfg['path'], ".meta")):
            if meta not in ls(cfg['path']):
                os.remove(os.path.join(cfg['path'], ".meta", meta))

    def list(self, tags=None, show_all=False, has=None):
        notes = sorted(self._notes.items(),
                       key=lambda x: x[1]['last_update'], reverse=True)

        if not show_all:
            notes = [n for n in notes if not n[1]['archived']]

        if tags:
            tags = tags.split(',')
            notes = [n for n in notes if bool(set(tags) & set(n[1]['tags']))]

        try:
            width = len(max([n[0] for n in notes], key=len)) + 2
        except:
            return

        for i, note in enumerate(notes):
            print("%.2d. %s %s" % (i+1, note[0].ljust(width),
                  tag_or_no(note[1]['tags'])))
