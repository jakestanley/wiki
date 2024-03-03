import os

from py.wiki.common import load_fm
from py.wiki.config import Config

def get_tag_counts(tags):

    counts = { "untagged": 0 }

    directory = Config().pages_dir
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            fm_tags = load_fm(filepath)['tags']
            if len(fm_tags) < 1:
                counts['untagged'] = counts['untagged'] + 1
                continue
            for tag in tags.keys():
                if tag in fm_tags:
                    if tag in counts.keys():
                        counts[tag] = counts[tag] + 1
                    else:
                        counts[tag] = 1

    return counts

def load_tags():

    tags = {}

    directory = Config().pages_dir
    for filename in os.listdir(directory):
        if filename == "index.md":
            continue
        elif filename.endswith(".md"):
            # a page is also a tag
            filepath = os.path.join(directory, filename)

            tag = os.path.splitext(os.path.basename(filepath))[0]
            title = load_fm(filepath)['title']
            tags[tag] = title

    return tags

def load_pages():

    pages = {}

    directory = Config().pages_dir
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            page = {}
            filepath = os.path.join(directory, filename)
            tag = os.path.splitext(os.path.basename(filepath))[0]

            fm_data = load_fm(filepath)
            page['title'] = fm_data['title']
            page['tags'] = fm_data['tags']
            pages[tag] = page

    return pages