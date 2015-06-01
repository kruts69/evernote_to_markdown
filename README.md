# Evernote to Markdown

`evernote_to_markdown` is a simple Python tool to convert Evernote data exported
in an `.enex` file to Markdown files with YAML metadata headers. It depends on
[lxml] and [pandoc].

[lxml]: http://lxml.de
[pandoc]: http://pandoc.org

## Overview

Each note will correspond to a single Markdown file. Each note will be placed in
a folder corresponding to its categorization. The created structure will be at
most two layers deep: one directory for a "stack", and one for the notebook
itself.

The file name for each document will be a normalized version of the title of the
note, and the title will also be included in the metadata for the file, along
with all available metadata, including:

  - the original notebook name (yes, this duplicates the information in the
    folder structure, but it allows you to perform programmatic operations based
    on the YAML data if so desired)
  - creation date
  - last modified date
  - location, if any
  - a list of the note's tags if any.
  - URL, if any

The YAML metadata will be formatted so:

```yaml
title: <note title>
author: <note author>
created: <timestamp>
updated: <timestamp>
URL: <value>
location:
  latitude: <value>
  longitude: <value>
  elevation: <value>
tags:
  - <tag name>
  - <tag name>
  - <etc.>
```

## Installation

Download this project (either as a zip file or by running `git clone`), and
in the root of the project, run `python setup.py install`.

(Regarding `pip`, see below under [TODO](#todo).)

## Usage

Run `evernote_to_markdown` or `evernote2md` from the command line. (The
`evernote2md` command is just an alias for the longer `evernote_to_markdown`
command; use whichever one you prefer.) The only required arguments are an input
`.enex` file and an output directory. For example:

```shell
$ evernote2md ~/Desktop/my_exported_notes.enex ~/notes
```

The program will complain loudly if there are existing files in the destination
directory, since they will be overwritten if they exist. You can choose to
proceed, however, by typing `yes`.

## TODO

  - Deploy the package to PyPi so that `pip install evernote_to_markdown` works.
  - I do not presently have any plan for how to download attachments. Perhaps
    they should live in a subdirectory for the note, and be linked with a
    relative path?
  - It might be nice for general usage to allow people to supply a mapping to
    specify destination notebooks, or tag remappings, etc.
