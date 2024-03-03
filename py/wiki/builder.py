import os
import pypandoc

from pathlib import Path

from py.wiki.config import Config
from py.wiki.tags import load_tags


def create_index_page(content):

    md_filename = os.path.join(Config().pages_dir, f"index.md")

    with open(md_filename, "w") as md_file:
        md_file.write(content)


def build_index():
    tags = load_tags()
    markdown_text = "# Tags"
    for tag in tags.keys():
        markdown_text += f"\n- [{tags[tag]} ({tag})](./{tag}.html)"

    markdown_text += "\n"
    create_index_page(markdown_text)
    return


def render():
    config = Config()
    html_directory = config.html_dir

    # clear html directory
    for filename in os.listdir(html_directory):
        if filename.endswith(".html"):
            file_path = os.path.join(html_directory, filename)
            os.remove(file_path)

    # render files
    pages_directory = config.pages_dir
    for filename in os.listdir(pages_directory):
        if filename.endswith(".md"):
            filepath = os.path.join(pages_directory, filename)
            tag = os.path.splitext(os.path.basename(filepath))[0]
            html_text = pypandoc.convert_file(filepath, "html", format="md")
            html_filename = os.path.join(html_directory, f"{tag}.html")
            with open(html_filename, "w") as html_file:
                html_file.write(html_text)

