Executable Notes (planning stage)
=================================

Kind of "wife-away I am bored" project.

The idea is to have command line app to make notes:

* directly from command line, e.g.

```
exnote new title                           # get multi-line input
exnote new title --note "this is my note"  # note init with some text
exnote append title --note "extra text"    # add some text to existing note
```

* using chosen editor

```
exnote edit title  # open note in external editor (create new one if necessary)
```

* from bash history

```
exnote new title --bash N     # save last N commands
exnote append title --bash N  # or add last N commands into existing note
```

* or from file

```
exnote new title --file path/to/file
exnote append title --file path/to/file
```

Each note can be run as a script:

```
exnote run title
exnote run title --env python
```

and, obviously, printed:

```
exnote show title
```

or deleted:

```
exnote del title
```

Each note can be tagged:

```
exnote new title --tags 'tag1, tag2, tag3'  # when created
exnote tag title --tags 'tag4, tag5, tag6'  # or tagged existing note
```

or untagged:

``
exnote untag title --tags 'tag2, tag6'
```

Tags can be then used when listing notes:

```
exnote list
exnote list --tag 'tag1'
```

Notes can be archived (not shown on by default on the list):

```
exnote archive title
exnote unarchive title
```
