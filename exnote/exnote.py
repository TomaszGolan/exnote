from __future__ import print_function

import click
import os
from config import cfg, cfg_init
from note import Note
from containter import Container


@click.group()
def main():
    cfg_init()


@main.command(help='Create a new note.')
@click.argument('title', type=str)
@click.option('-n', '--note', type=str, default=None, help='Note subject.')
@click.option('-s', '--src', type=str, default=None, help='Path to file.')
@click.option('-t', '--tags', type=str, default=None, help='Note tags.')
def new(title, note, src, tags):
    n = Note(title.lstrip('.').replace('/', '.'), new=True)
    try:
        n.fromfile(src)
    except IOError:
        click.secho("%s could not be opened!" % src, fg='red')
    except:
        n.new(note)
    n.create_meta(tags)


@main.command(help="Append some text to existing note.")
@click.argument('title', type=str)
@click.option('-n', '--note', type=str, default=None, help='Note subject.')
def append(title, note):
    n = Note(title)
    n.load()
    n.append(note)
    n.touch()


@main.command(help="Archive a note.")
@click.argument('title', type=str)
def archive(title):
    n = Note(title)
    n.archive()


@main.command(help="Unarchive a note.")
@click.argument('title', type=str)
def unarchive(title):
    n = Note(title)
    n.unarchive()


@main.command(help="Add tags to a note.")
@click.argument('title', type=str)
@click.option('-t', '--tags', type=str, required=True, help='Note tags.')
def tag(title, tags):
    n = Note(title)
    n.add_tags(tags)
    n.touch()


@main.command(help="Remove tags from a note.")
@click.argument('title', type=str)
@click.option('-t', '--tags', type=str, required=True, help='Note tags.')
def untag(title, tags):
    n = Note(title)
    n.remove_tags(tags)
    n.touch()


@main.command(help="Edit a note with external editor.")
@click.argument('title', type=str)
def edit(title):
    n = Note(title)
    n.edit()
    n.touch()


@main.command(help="Print a note.")
@click.argument('title', type=str)
def show(title):
    n = Note(title)
    n.load()
    print(n)


@main.command(help="Run a note.")
@click.argument('title', type=str)
@click.option('-e', '--env', type=str, default='bash',
              help='What should be note run by')
def run(title, env):
    n = Note(title)
    n.run(env)


@main.command('ls', help='List of notes.')
@click.option('-t', '--tags', type=str, default=None, help='Filter by tags.')
@click.option('-a', '--all', type=str, is_flag=True, help='Show archived.')
def list(tags, all):
    ctr = Container()
    ctr.list(tags, all)
