# Wiki

A Wiki/CMS based around tags. Rendered with Markdown.

# Concept

- Creating a page creates a tag
- A page can have other tags
- Each page will have a list of pages that are associated with that tag
- Root will be dynamically generated but can contain custom markdown

# Usage

- `wiki.py create-tag` will create a tag page
    - `--name` will give it that name. will automatically be converted into a tag
    - `--tags <tags>` will apply following tags to that tag page
- `wiki.py create-page` will create an untagged page unless tags provided
    - `--name <pagename>` will be sanitised
    - `--tags <tags>` these tags will be created if they do not already exist
- `wiki.py build` will build the wiki
- `wiki.py list-tags` will list tags
- `wiki.py list-pages` will 
- `wiki.py tag-pages` will tag pages with provided tag
    - `--pages <pages>`
    - `--tags <tags>`

# Example

// Design consideration. Do we want to bother creating tags manually? I doubt it.

- `wiki.py create-page --name "Counter Strike 2" --tags "Linkup"`
    - Creates page titled "Counter Strike 2"
        - Page will have url `{root}/counter-strike-2`
        - Page will have front matter referencing tags
    - Creates tag page `linkup`
        - Tag page will have url `{root}/linkup`
        - Pages implicitly have a tag link to themselves
- `wiki.py create-page --name "Insurgency" --tags "Lan party"`
    - Similar to above
- Oh crap. We have a similar tag, maybe we want to merge these tags and tag pages?
- `wiki.py merge-tags --name linkup --tags linkup,lan-party`
    - Will merge the content of both pages and all tag references to `linkup`
- `wiki.py check` will create missing tag pages if tags have been manually added, etc