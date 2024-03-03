import argparse

from tabulate import tabulate
from typing import List
from pathlib import Path

from py.wiki.arguments import parse_arguments
from py.wiki.config import Config
from py.wiki.pages import create
from py.wiki.tags import load_tags, get_tag_counts


def do_create_action(args):

    title = args.title
    tags = set(args.tags) if args.tags else set()

    if not title:
        title = input("Enter title: ")

    if len(tags) < 1:
        raw_tags = input("Enter tags (comma separated): ")
        tags = raw_tags.split(',')

    create(title, tags)


def do_list_action():
    tags = load_tags()
    tags['untagged'] = "Untagged"
    counts = get_tag_counts(tags)
    headers = ["Tag ID", "Description", "Uses"]
    data = []
    for key in tags.keys():
        data.append([key, tags[key], counts[key] if key in counts.keys() else 0])

    table = tabulate(data, headers, tablefmt="grid")
    print(table)


def do_merge_action(args):
    if len(args.items) != 2:
        raise UserWarning("Error: Exactly two items are required for merge")
    elif args.items[0] == args.items[1]:
        raise UserWarning("Error: Items to merge cannot be identical")
    return merge_items(args.title, args.items)


def merge_items(title, items):

    raise NotImplementedError()

    # TODO merge tags, merge content
    return


def do_build_action():
    tags = load_tags()
    return


def handle_actions(args):
    if args.action == 'create':
        return do_create_action(args)
    elif args.action == 'list':
        return do_list_action()
    elif args.action == 'merge':
        return do_merge_action(args)
    elif args.action == 'build':
        return do_build_action()

    raise UserWarning("Error: Unrecognised command input")


def main():
    parser = argparse.ArgumentParser(description="Flat wiki management system.")
    args = parse_arguments(parser)

    Config(Path("./"))

    # process arguments, capture exceptions and print usage if all goes wrong
    try:
        handle_actions(args)
    except UserWarning as e:
        print("Caught:", e)
        parser.print_usage()

if __name__ == '__main__':
    main()
