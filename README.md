Executable Notes
================

ExNote is a simple app to manage notes from command line, with possibility
to run them as scripts.

```
Usage: exnote [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  append     Append some text to existing note.
  archive    Archive a note.
  edit       Edit a note with external editor.
  ls         List of notes.
  new        Create a new note.
  rm         Delete a note.
  run        Run a note.
  show       Print a note.
  tag        Add tags to a note.
  unarchive  Unarchive a note.
  untag      Remove tags from a note.
```

* [Basic usage](#basic_usage)
* [Archiving](#archiving)
* [Tagging](#tagging)
* [Inline operations](#inline_operations)
* [Running notes](#running_notes)
* [Tips and Tricks](#tips_and_tricks)
* [Installation](#installation)

# Basic usage

* Create a note

```
$ exnote new my_note

my_note
=======

(empty line close note)
Hello World!
```

* List notes

```
$ exnote ls

01. my_note   
```

* Show a note

```
$ exnote show my_note

my_note
=======

Hello World!
```

* Append to a note

```
$ exnote append my_note

my_note
=======

Hello World!
Goodbye World!   
```

* Edit a note in external editor

```
$ exnote edit my_note
```

* Remove a note

```
$ exnote rm my_note
```

# Archiving

Each note can be archived, so it will not be shown by default on the list.

```
$ exnote new my_note_to_archive
$ exnote ls

01. my_note_to_archive   
02. my_note              

$ exnote archive my_note_to_archive
$ exnote ls

01. my_note

$ exnote ls -a

01. my_note_to_archive   
02. my_note              

$ exnote unarchive my_note_to_archive
$ exnote ls

01. my_note_to_archive   
02. my_note      
```

# Tagging

Each note can be tagged, which can be used for selective listing.

```
$ exnote tag my_note -t general
$ exnote ls

01. my_note              #general
02. my_note_to_archive   

$ exnote ls -t general

01. my_note   #general

$ exnote untag my_note -t general
$ exnote ls

01. my_note              
02. my_note_to_archive  
```

# Inline operations

* Use `-n / --note` to pass a subject

```
$ exnote new another_note -n 'inline note'
$ exnote show another_note

another_note
============

inline note

$ exnote append another_note -n 'inline append'
$ exnote show another_note

another_note
============

inline note
inline append
```

* Use `-t / --tags` to add tags when note is created

```
$ exnote new tagged_note -n 'this is awesome note' -t 'general, pointless'
$ exnote ls

01. tagged_note          #general #pointless
02. another_note         
03. my_note              
04. my_note_to_archive
```

* Use `-s / --src` to create a note from existing file

```
$ exnote new config -s ~/.exnote.ini
$ exnote show config

config
======

[SETTINGS]
path = /home/goran/.exnote
editor = gedit
```

# Running notes

Each note can be run as a script (bash by default).

```
$ exnote new do_echo -n 'echo "Hi $USER"' -t bash
$ exnote run do_echo

Hi goran
```

`-a / --arg` flag can be used to pass arguments to a script

```
$ exnote new print -n 'echo $1' -t bash
$ exnote run print -a 'I am a fancy note'

I am a fancy note
```

`-e / --env` flag can be used to define how note should be run

```
$ exnote new pyprint -t python

pyprint
=======

(empty line close note)
import os
print "Hi %s" % os.getenv('USER')

$ exnote run pyprint -e python

Hi goran
```

# Tips and Tricks

* I could not find a workaround to create a note from last used bash commands,
but this works fine:

```
$ exnote new what_i_did -n "`history 5`"
$ exnote show what_i_did

what_i_did
==========

 2062  exnote new print -n 'echo $1' -t bash
 2063  exnote run print -a 'I am a fancy note'
 2064  exnote new pyprint -t python
 2065  exnote run pyprint -e python
 2066  exnote new what_i_did -n "`history 5`"
```

* Use `exnote --help` to get a list of commands and `exnote COMMAND --help`
to get more info about each command.

# Installation

To install exnote simply clone this repository and run setup.py
(requires `setuptools`):

```
git clone https://github.com/TomaszGolan/exnote.git
cd exnote
python setup.py build install
```

> Configuration file is located at ~/.exnote.ini and it is created on first run.
