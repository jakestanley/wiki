import argparse
from py.wiki.tags import create_or_update_tag
from py.wiki.pages import create_or_update_page

def handle_create_update_tag():
    return create_or_update_tag()

def handle_delete_tag():
    pass

def handle_create_update_page():
    return create_or_update_page()

def handle_page_delete():
    pass

def parse_arguments(parser):
    
    # add subparser for actions
    subparsers = parser.add_subparsers(dest="action", help="Actions")

    # tag subcommand
    tag_parser = subparsers.add_parser('tag', help='Manage tags')
    tag_subparsers = tag_parser.add_subparsers(dest="tag_action", help="Tag actions")
    tag_subparsers.add_parser('create', help='Create or update a tag')
    tag_subparsers.add_parser('delete', help='Delete a tag')
    tag_subparsers.add_parser('list', help='List tags')

    # page subcommand
    page_parser = subparsers.add_parser('page', help='Manage pages')
    page_subparsers = page_parser.add_subparsers(dest="page_action", help="Page actions")
    page_subparsers.add_parser('create', help='Create or update a page')
    page_subparsers.add_parser('delete', help='Delete a page')

    page_list_parser = page_subparsers.add_parser('list', help='List pages')
    page_list_parser.add_argument('--tags', nargs ='+', help='Filter pages by tags', default=[])

    return parser.parse_args()

def process(args):
    if args.action == 'tag':
        if args.tag_action == 'create':
            return handle_create_update_tag()
        elif args.tag_action == 'delete':
            return handle_delete_tag()
    elif args.action == 'page':
        if args.page_action == 'create':
            return handle_create_update_page()
        elif args.page_action == 'delete':
            return handle_page_delete()

    raise ValueError("Unrecognised command input")

def main():
    parser = argparse.ArgumentParser(description="Flat wiki management system.")
    args = parse_arguments(parser)

    # default to create for tag or page if not provided
    if args.action in ['tag', 'page'] and not args.__dict__.get(f'{args.action}_action'):
        setattr(args, f'{args.action}_action', 'create')

    # process arguments, capture exceptions and print usage if all goes wrong
    try:
        process(args)
    except Exception as e:
        print("Caught exception: ", e)
        parser.print_usage()

if __name__ == '__main__':
    main()
