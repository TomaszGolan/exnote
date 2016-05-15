import click
import os
import sys
from config import cfg
from utils import get_multline
from ConfigParser import SafeConfigParser
from datetime import datetime


class Note:
    def __init__(self, title):
        self._title = title
        self._path = os.path.join(cfg['path'], title)
        self._meta = self._path + ".meta"
        self._ctx = ''

    def __str__(self):
        return self._title + '\n' + '='*len(self._title) + '\n\n' + self._ctx

    def new(self, ctx=None):
        if os.path.isfile(self._path):
            click.secho("%s already exists!" % self._path, fg='red')
            sys.exit(1)

        with open(self._path, 'w') as f:
            f.write(ctx or get_multline(self))

    def load(self):
        if not os.path.isfile(self._path):
            click.secho("%s does not exists!" % self._path, fg='red')
            sys.exit(1)

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

    def add_tags(self, tags):
        _tags = self._get_tags()
        _tags.extend(tags.split(','))
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
        try:
            return meta.get("note", "tags").split(',')
        except:
            return []

    def create_meta(self, tags=None):
        meta = SafeConfigParser()
        meta.add_section("note")

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        meta.set("note", "birthday", time)
        meta.set("note", "last_update", time)
        meta.set("note", "tags", tags or '')
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
