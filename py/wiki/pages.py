import yaml
import os
import csv

from typing import List, Set

from pathlib import Path

from py.wiki.config import Config
from py.wiki.common import sanitize_name, load_fm, create
from py.wiki.tags import create_or_get_tag

def clean_tags(tags: Set[str]):

    clean_tags = []
    for tag in tags:
        clean_tags.append(create_or_get_tag(tag))

    return clean_tags
    

# TODO: adding images
def create_page(title: str, tags: Set[str]):
    """Add or update a page in the database and create its Markdown page."""
    # TODO: separate into page wizard

    if not title:
        title = input("Enter page title: ")

    if not tags:
        raw_tags = input("Enter tags (comma separated): ")
        tags = raw_tags.split(',')

    tags = clean_tags(tags)

    page_id = sanitize_name(title)

    create(title, page_id, tags)

    # TODO: detect similar page names
    # TODO: detect similar tag names

    return
