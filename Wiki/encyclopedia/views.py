import random

import markdown2
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": "Entry Not Found",
            "message": f'The entry "{title}" does not exist.'
        })

    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def search(request):
    query = request.GET.get("q", "").strip()
    entries = util.list_entries()

    if query:
        for entry_title in entries:
            if entry_title.lower() == query.lower():
                return HttpResponseRedirect(reverse("entry", args=[entry_title]))

    matches = [title for title in entries if query.lower() in title.lower()] if query else []

    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "matches": matches
    })


def create_entry(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title:
            return render(request, "encyclopedia/create_entry.html", {
                "error": "Title is required.",
                "title_value": title,
                "content_value": content
            })

        existing = [t.lower() for t in util.list_entries()]
        if title.lower() in existing:
            return render(request, "encyclopedia/create_entry.html", {
                "error": f'An entry with the title "{title}" already exists.',
                "title_value": title,
                "content_value": content
            })

        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", args=[title]))

    return render(request, "encyclopedia/create_entry.html")


def edit_entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": "Entry Not Found",
            "message": f'The entry "{title}" does not exist.'
        })

    if request.method == "POST":
        new_content = request.POST.get("content", "").strip()
        util.save_entry(title, new_content)
        return HttpResponseRedirect(reverse("entry", args=[title]))

    return render(request, "encyclopedia/edit_entry.html", {
        "title": title,
        "content_value": content
    })


def random_entry(request):
    entries = util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html", {
            "title": "No Entries",
            "message": "There are no entries to choose from."
        })

    title = random.choice(entries)
    return HttpResponseRedirect(reverse("entry", args=[title]))
