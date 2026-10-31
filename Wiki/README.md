# Wiki — CS50W Project 1
### Dyan Ahmadi

A Wikipedia-style online encyclopedia built with **Django**. Entries are stored as Markdown files and rendered to HTML in the browser.

Part of [CS50's Web Programming](https://cs50.harvard.edu/web/).

## Video Demo
[Click here to watch the demo](https://youtu.be/Cn_WHcFqM7Y)

## Features

- **Index page** – lists every encyclopedia entry, each linking to its page.
- **Entry page** – `/wiki/<TITLE>` renders the entry's Markdown as HTML; shows a friendly error page if the entry doesn't exist.
- **Search** – search from the sidebar. An exact match redirects to the entry; otherwise a results page lists all entries whose title contains the query as a substring.
- **New page** – create an entry with a title and Markdown content. Saving a title that already exists shows an error instead of overwriting.
- **Edit page** – edit an existing entry, with the Markdown pre-filled in a textarea.
- **Random page** – jump to a random entry.
- **Markdown → HTML** conversion using the `markdown2` package.

## Tech stack

- Python 3
- Django 3.0.x
- markdown2
- Bootstrap 4 (CDN) + custom CSS

## Project structure

```
wiki/
├── manage.py
├── wiki/                      # Project settings and root URL config
├── encyclopedia/              # Main app
│   ├── views.py               # index, entry, search, new page, edit, random
│   ├── urls.py
│   ├── util.py                # list_entries, get_entry, save_entry helpers
│   ├── templates/encyclopedia/
│   │   ├── layout.html
│   │   ├── index.html
│   │   ├── entry.html
│   │   ├── search.html
│   │   ├── new.html
│   │   ├── edit.html
│   │   └── error.html
│   └── static/encyclopedia/styles.css
└── entries/                   # Markdown files, one per entry
```

## Getting started

```bash
# 1. Clone the repository
git clone https://github.com/dianr6boy1386/Wiki.git


# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install "django<3.1" markdown2

# 4. Run the development server
python manage.py runserver
```

Then open <http://127.0.0.1:8000/>.

## Routes

| URL | Description |
| --- | --- |
| `/` | Index of all entries |
| `/wiki/<title>` | View an entry |
| `/search?q=<query>` | Search entries |
| `/new` | Create a new entry |
| `/edit/<title>` | Edit an entry |
| `/random` | Redirect to a random entry |

## Adding entries

Entries are plain Markdown files in `entries/`. You can add one through the site's **Create New Page** form or by dropping a `Title.md` file into that folder.

## Notes

- No database models are used; `util.py` reads and writes entries directly on disk.
- Entry titles are case-insensitive when searching.