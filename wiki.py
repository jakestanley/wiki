import argparse

from typing import List
from pathlib import Path

from py.wiki.config import Config
from py.wiki.pages import create_page

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

    # page subcommand
    page_parser: argparse.ArgumentParser = subparsers.add_parser('create-page', help='Create a page')
    page_parser.add_argument("--title", "-n", help="Title of the page")
    page_parser.add_argument("--tags", "-t", nargs='+', help="List of page tags")

    # page_subparsers = page_parser.add_subparsers(dest="page_action", help="Page actions")
    # page_subparsers.add_parser('create', help='Create or update a page')
    # page_subparsers.add_parser('delete', help='Delete a page')

    # page_list_parser = page_subparsers.add_parser('list', help='List pages')
    # page_list_parser.add_argument('--tags', nargs ='+', help='Filter pages by tags', default=[])

    # the design is reminding me a lot of my note taking tool idea
    #   in that really pages are just leaves
    return parser.parse_args()

def process(args):
    if args.action == 'create-page':
        return create_page(args.title, set(args.tags) if args.tags else set())
    elif args.action == 'tag':
        if args.tag_action == 'list':
            return handle_list_tags()
        elif args.tag_action == 'delete':
            return handle_delete_tag()

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
