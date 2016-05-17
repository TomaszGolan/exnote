from __future__ import print_function

import click
import os
from config import cfg, cfg_init
from note import Note
from containter import Container


@click.group()
def main():
    cfg_init()


@main.command()
@click.argument('title', type=str)
@click.option('--note', type=str, default=None)
@click.option('--tags', type=str, default=None)
def new(title, note, tags):
    n = Note(title.lstrip('.').replace('/', '.'))
    n.new(note)
    n.create_meta(tags)


@main.command()
@click.argument('title', type=str)
@click.option('--note', type=str, default=None)
def append(title, note):
    n = Note(title)
    n.load()
    n.append(note)
    n.touch()


@main.command()
@click.argument('title', type=str)
def archive(title):
    n = Note(title)
    n.confirm()
    n.archive()


@main.command()
@click.argument('title', type=str)
def unarchive(title):
    n = Note(title)
    n.confirm()
    n.unarchive()


@main.command()
@click.argument('title', type=str)
@click.option('--tags', type=str, required=True)
def tag(title, tags):
    n = Note(title)
    n.confirm()
    n.add_tags(tags)
    n.touch()


@main.command()
@click.argument('title', type=str)
@click.option('--tags', type=str, required=True)
def untag(title, tags):
    n = Note(title)
    n.confirm()
    n.remove_tags(tags)
    n.touch()


@main.command()
@click.argument('title', type=str)
def edit(title):
    n = Note(title)
    n.confirm()
    n.edit()
    n.touch()


@main.command()
@click.argument('title', type=str)
def show(title):
    n = Note(title)
    n.load()
    print(n)


@main.command()
@click.argument('has', type=str, nargs=-1)
@click.option('--tags', type=str, default=None)
def list(has, tags):
    ctr = Container()
    ctr.list(tags)
