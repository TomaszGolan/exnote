from __future__ import print_function

import click
import os
import sys
from config import cfg
from utils import get_multline
from ConfigParser import SafeConfigParser
from datetime import datetime
from subprocess import call


class Note:
    def __init__(self, title, new=False):
        self._title = title
        self._path = os.path.join(cfg['path'], title)
        self._meta = os.path.join(cfg['path'], ".meta", title)
        self._ctx = None
        new or self._confirm()

    def __str__(self):
        return self._title + '\n' + '='*len(self._title) + '\n\n' \
            + (self._ctx or "(empty line close note)")

    def new(self, ctx=None):
        if os.path.isfile(self._path):
            click.secho("%s already exists!" % self._title, fg='red')
            sys.exit(1)

        with open(self._path, 'w') as f:
            f.write(ctx or get_multline(self))

    def _confirm(self):
        if not os.path.isfile(self._path):
            click.secho("%s does not exists!" % self._title, fg='red')
            sys.exit(1)

    def load(self):
        with open(self._path, 'r') as f:
            self._ctx = f.read()

    def append(self, ctx=None):
        with open(self._path, 'a') as f:
            f.write('\n' + (ctx or get_multline(self)))

    def edit(self):
        try:
            click.edit(filename=self._path, editor=cfg['editor'])
        except:
            click.edit(filename=self._path)

    def fromfile(self, src):
        with open(src, 'r') as f:
            ctx = f.read()
        self.new(ctx)

    def add_tags(self, tags):
        _tags = self._get_tags()
        _tags.extend("".join(tags.split()).split(','))
        self._change_meta("tags", ','.join(set(_tags)))

    def remove_tags(self, tags):
        _tags = self._get_tags()
        for tag in tags.split(','):
            if tag in _tags:
                _tags.remove(tag)
        self._change_meta("tags", ','.join(set(_tags)))

    def _get_tags(self):
        meta = SafeConfigParser()
        meta.read(self._meta)
        if meta.get("note", "tags"):
            return meta.get("note", "tags").strip().split(',')
        else:
            return []

    def _is_archived(self):
        meta = SafeConfigParser()
        meta.read(self._meta)
        return meta.get("note", "archived") == "True"

    def _when_touched(self):
        meta = SafeConfigParser()
        meta.read(self._meta)
        return meta.get("note", "last_update")

    def get_meta(self):
        try:
            meta = {}
            meta['tags'] = self._get_tags()
            meta['archived'] = self._is_archived()
            meta['last_update'] = self._when_touched()
            return meta
        except:
            self.create_meta()
            self.get_meta()

    def create_meta(self, tags=None):
        meta = SafeConfigParser()
        meta.add_section("note")

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if tags:
            tags = "".join(tags.split())
        else:
            tags = ''

        meta.set("note", "birthday", time)
        meta.set("note", "last_update", time)
        meta.set("note", "tags", tags)
        meta.set("note", "archived", "False")

        with open(self._meta, 'w') as f:
            meta.write(f)

    def _change_meta(self, option, value):
        try:
            meta = SafeConfigParser()
            meta.read(self._meta)

            meta.set("note", option, value)

            with open(self._meta, 'w') as f:
                meta.write(f)
        except:
            self.create_meta()
            self._change_meta(option, value)

    def touch(self):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._change_meta("last_update", time)

    def archive(self):
        self._change_meta("archived", "True")

    def unarchive(self):
        self._change_meta("archived", "False")

    def run(self, env):
        call([env, self._path])
