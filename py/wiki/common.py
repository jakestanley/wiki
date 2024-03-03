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
    id = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    if id in ['untagged', 'index']:
        # TODO: warning - this could result in a partially completed transaction
        raise UserWarning(f"Error: Cannot use name '{name}' as '{id}' is reserved")
    return id

# TODO: defer to make transactional
def create_page(title, id, tags):

    md_filename = os.path.join(Config().pages_dir, f"{id}.md")

    content = f"# {title}\n\nThis page is a stub"

    if Path(md_filename).exists():
        print(f"Updating existing page '{title}' ({id})")
        fm_data = load_fm(md_filename)
        fm_tags = set(fm_data['tags'])
        fm_data['tags'] = list(fm_tags.union(tags if tags else set()))
    else:
        print(f"Creating a new page '{title}' ({id})")
        fm_data = {
        "title": title,
        "tags": list(tags) if tags else []
    }

    page = frontmatter.Post(content, **fm_data)
    with open(md_filename, "w") as md_file:
        md_file.write(frontmatter.dumps(page))