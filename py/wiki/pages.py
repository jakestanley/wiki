from py.wiki.common import sanitize_name, create_page


def create(title, tags):

    page_tags = set()

    
    for tag in {tag for tag in (tags or set()) if tag}:
        page_tags.add(create(tag, None))

    id = sanitize_name(title)

    create_page(title, id, page_tags)

    return id
