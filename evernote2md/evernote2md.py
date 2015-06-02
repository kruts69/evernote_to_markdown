#!/usr/bin/env python3
"""Convert Evernote .enex exports to Markdown documents with YAML metadata."""


# Standard library dependencies
import argparse
from pathlib import Path
import sys

# Third-party dependencies
import lxml
import yaml


def main():
    pass


def _parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('enex_file')
    parser.add_argument('destination_directory', type=Path)

    args = parser.parse_args()

    if args.destination_directory.exists():
        warning = ("The destination directory exists. If you continue, its "
                   "contents will be overwritten completely.\nDo you wish to "
                   "proceed? [y/N]  ")
        user_response = input(warning)

        if user_response != 'y':
            print("Okay! Try again with a different directory!")
            sys.exit()


if __name__ == '__main__':
    main()
