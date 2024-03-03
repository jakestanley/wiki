import re
import csv
import os

from py.wiki.common import load_fm, create
from pathlib import Path

from py.wiki.config import Config

def load_tags():

    tags = {}

    directory = Config().pages_dir
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            # a page is also a tag
            filepath = os.path.join(directory, filename)

            tag = os.path.splitext(os.path.basename(filepath))[0]
            title = load_fm(filepath)['title']
            tags[tag] = title


    # if os.path.exists(db_path):
    #     with open(db_path, 'r', newline='') as db_file:
    #         reader = csv.reader(db_file, delimiter=',')
    #         for row in reader:
    #             if len(row) == 2:
    #                 tags[row[0]] = row[1]

    return tags    


def create_or_get_tag(tag_id):
    tags = load_tags()

    if tag_id in tags.keys():
        return tag_id
    else:
        return create_or_update_tag(tag_id)
    

def create_or_update_tag(tag_id, human_readable_name=None):
    """Add or update a tag in the database and create its Markdown page."""
    # Read the existing database
    tags = load_tags()

    # Update or add the tag
    title = human_readable_name if human_readable_name else tag_id
    tags[tag_id] = title

    # Create or update the Markdown file for the tag
    create(title, tag_id, set())

    return tag_id
