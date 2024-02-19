import re
import csv
import os

from pathlib import Path

db_path = "data/database/tags.txt"
tags_wiki_dir = "wiki"

def load_tags():

    tags = {}

    if os.path.exists(db_path):
        with open(db_path, 'r', newline='') as db_file:
            reader = csv.reader(db_file, delimiter=',')
            for row in reader:
                if len(row) == 2:
                    tags[row[0]] = row[1]

    return tags    


def create_or_get_tag(tag_id):
    tags = load_tags()

    if tags[tag_id]:
        return tag_id
    else:
        return create_or_update_tag(tag_id)
    

def create_or_update_tag(tag_id, human_readable_name=None):
    """Add or update a tag in the database and create its Markdown page."""
    # Read the existing database
    tags = load_tags()

    # Update or add the tag
    tags[tag_id] = human_readable_name if human_readable_name else tag_id

    if not Path(md_filename).exists():
        with open(md_filename, 'w') as md_file:
            md_file.write(f"# {human_readable_name if human_readable_name else tag_id}\n\nThis tag page is a stub")

    # Write the updated database
    with open(db_path, 'w', newline='') as db_file:
        writer = csv.writer(db_file, delimiter=',')
        for tag_id, name in tags.items():
            writer.writerow([tag_id, name])

    # Create or update the Markdown file for the tag
    md_filename = os.path.join(tags_wiki_dir, f"{tag_id}.md")
    if not os.path.exists(tags_wiki_dir):
        os.makedirs(tags_wiki_dir)

    return tag_id
