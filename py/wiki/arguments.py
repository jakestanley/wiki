import argparse

def build_page_parser(subparsers):
    page_parser: argparse.ArgumentParser = subparsers.add_parser('create')
    page_parser.add_argument("--title", "-n")
    page_parser.add_argument("--tags", "-t", nargs='+')

def build_merge_parser(subparsers):
    merge_parser: argparse.ArgumentParser = subparsers.add_parser('merge')
    merge_parser.add_argument("--title", "-n")
    merge_parser.add_argument("items", nargs='+', metavar=("item1", "item2"))

def build_build_parser(subparsers):
    build_parser: argparse.ArgumentParser = subparsers.add_parser('build')

def build_list_parser(subparsers):
    list_parser: argparse.ArgumentParser = subparsers.add_parser('list')

def parse_arguments(parser):
    
    parser = argparse.ArgumentParser(description="Flat wiki management system")
    subparsers = parser.add_subparsers(dest="action", help="Actions")

    build_page_parser(subparsers)
    build_merge_parser(subparsers)
    build_build_parser(subparsers)
    build_list_parser(subparsers)

    return parser.parse_args()
