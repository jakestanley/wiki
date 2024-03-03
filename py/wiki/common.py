import re
import os
import frontmatter

from typing import Set
from pathlib import Path

from py.wiki.config import Config

def load_fm(md_filename):
    with open(md_filename, 'r') as file:
        content = frontmatter.load(file)
        return content.metadata

def sanitize_name(name):
    """Convert a human-readable name to a sanitized ID."""
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def create(title, id, tags):
    md_filename = os.path.join(Config().pages_dir, f"{id}.md")

    content = f"# {title}\n\nThis page is a stub"

    # force tags into a set for consistent handling
    tags = set(tags)

    if Path(md_filename).exists():
        print("Updated existing page...\n")
        fm_data = load_fm(md_filename)
        fm_tags = set(fm_data['tags'])
        fm_data['tags'] = list(fm_tags.union(tags))
    else:
        print("Creating a new page...\n")
        fm_data = {
        "title": title,
        "tags": list(tags)
    }

    page = frontmatter.Post(content, **fm_data)
    with open(md_filename, "w") as md_file:
        md_file.write(frontmatter.dumps(page))