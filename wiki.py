import argparse
from tabulate import tabulate

from typing import List
from pathlib import Path

from py.wiki.config import Config
from py.wiki.pages import create_page
from py.wiki.tags import load_tags, get_tag_counts

def handle_delete_page():
    pass

def handle_list_tags():
    pass

def handle_delete_tag():
    pass

def handle_list_pages(tags: List[str]=[]):
    pass

def parse_arguments(parser):
    
    # add subparser for actions
    subparsers = parser.add_subparsers(dest="action", help="Actions")

    # tag subcommand
    # tag_parser = subparsers.add_parser('create-page', help='Create page')
    # tag_subparsers = tag_parser.add_subparsers(dest="tag_action", help="Tag actions")
    # tag_subparsers.add_parser('list', help='List tags')
    # tag_subparsers.add_parser('delete', help='Delete a tag')

    # create-page subcommand
    page_parser: argparse.ArgumentParser = subparsers.add_parser('create-page', help='Create a page')
    page_parser.add_argument("--title", "-n", help="Title of the page")
    page_parser.add_argument("--tags", "-t", nargs='+', help="List of page tags")

    # list-tags subcommand
    list_tags_parser : argparse.ArgumentParser = subparsers.add_parser('list-tags', help='List tags')

    # page_subparsers = page_parser.add_subparsers(dest="page_action", help="Page actions")
    # page_subparsers.add_parser('create', help='Create or update a page')
    # page_subparsers.add_parser('delete', help='Delete a page')

    # page_list_parser = page_subparsers.add_parser('list', help='List pages')
    # page_list_parser.add_argument('--tags', nargs ='+', help='Filter pages by tags', default=[])

    # the design is reminding me a lot of my note taking tool idea
    #   in that really pages are just leaves
    return parser.parse_args()

def display_tags():
    tags = load_tags()
    counts = get_tag_counts(tags)
    headers = ["Tag ID", "Description", "Uses"]
    data = []
    for key in tags.keys():
        data.append([key, tags[key], counts[key] if key in counts.keys() else 0])

    table = tabulate(data, headers, tablefmt="grid")
    print(table)

def process(args):
    if args.action == 'create-page':
        return create_page(args.title, set(args.tags) if args.tags else set())
    elif args.action == 'list-tags':
        return display_tags()

    raise UserWarning("Unrecognised command input")


def main():
    parser = argparse.ArgumentParser(description="Flat wiki management system.")
    args = parse_arguments(parser)

    # # default to create for tag or page if not provided
    # if args.action in ['tag', 'page'] and not args.__dict__.get(f'{args.action}_action'):
    #     setattr(args, f'{args.action}_action', 'create')

    Config(Path("./"))

    # process arguments, capture exceptions and print usage if all goes wrong
    try:
        process(args)
    except UserWarning as e:
        print("Caught warning: ", e)
        parser.print_usage()

if __name__ == '__main__':
    main()
