import frontmatter
import yaml
import os
import csv

from pathlib import Path

from py.wiki.common import sanitize_name
from py.wiki.tags import create_or_get_tag

pages_wiki_dir = "data/pages"

def get_page_tags():
    raw_tags = input("Enter tags (comma separated): ")

    # TODO validate
    tags = raw_tags.split(',')

    clean_tags = []
    for tag in tags:
        clean_tags.append(create_or_get_tag(tag))

    return clean_tags

def load_fm(md_filename):
    with open(md_filename, 'r') as file:
        content = frontmatter.load(file)
        return content.metadata

# TODO: adding images
def create_or_update_page():
    """Add or update a page in the database and create its Markdown page."""
    title = input("Enter page title: ")
    page_id = sanitize_name(title)

    if not os.path.exists(pages_wiki_dir):
        os.makedirs(pages_wiki_dir)

    # TODO: detect similar page names
    # TODO: detect similar tag names
    md_filename = os.path.join(pages_wiki_dir, f"{page_id}.md")

    content = f"# {title}\n\nThis page is a stub"
    front_matter_data = {
        "title": title,
        "tags": tags
    }

    if Path(md_filename).exists():
        frontmatter = load_fm(md_filename)

    tags = get_page_tags()

    print("Creating a new page...\n")

    page = frontmatter.Post(content, **front_matter_data)
    with open(md_filename, "w") as md_file:
        md_file.write(frontmatter.dumps(page))

    return
