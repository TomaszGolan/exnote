import click
import os
from config import cfg, cfg_init
from note import Note


@click.group()
def main():
    cfg_init()


@main.command()
@click.argument('title', type=str)
@click.option('--note', type=str, default=None)
@click.option('--tags', type=str, default=None)
def new(title, note, tags):
    n = Note(title)
    n.new(note)
    n.create_meta(tags)


@main.command()
@click.argument('title', type=str)
@click.option('--note', type=str, default=None)
def append(title, note, tags):
    n = Note(title)
    n.load()
    n.append(note)
    n.touch()


@main.command()
@click.argument('title', type=str)
def archive(title):
    n = Note(title)
    n.load()
    n.archive()


@main.command()
@click.argument('title', type=str)
def unarchive(title):
    n = Note(title)
    n.load()
    n.unarchive()


@main.command()
@click.argument('title', type=str)
@click.option('--tags', type=str, required=True)
def tag(title, tags):
    n = Note(title)
    n.add_tags(tags)
    n.touch()


@main.command()
@click.argument('title', type=str)
@click.option('--tags', type=str, required=True)
def untag(title, tags):
    n = Note(title)
    n.remove_tags(tags)
    n.touch()
    

@main.command()
@click.argument('title', type=str)
def show(title):
    n = Note(title)
    n.load()
    print(n)
