import markovify
import random

from flask import render_template, send_from_directory

BACKGROUND_COLORS = [
    "cyan",
    "emerald",
    "fuchsia",
    "green",
    "indigo",
    "orange",
    "pink",
    "purple",
    "rose",
    "sky",
    "teal",
    "zinc",
]


with open("hn_title.csv") as f:
    text = f.read()

text_model = markovify.NewlineText(text, state_size=3)


def route_request(request):
    if "favicon" in request.path:
        return serve_favicon()

    return serve_root(request)


def serve_favicon():
    return send_from_directory(
        "templates",
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


def serve_root(request):
    color1, color2 = random.sample(
        BACKGROUND_COLORS,
        2,
    )

    return render_template(
        "index.html", hn_title=_get_title(), color1=color1, color2=color2
    )


def _get_title():
    sentence = None
    while not sentence:
        sentence = text_model.make_short_sentence(280)
    print(sentence)
    return sentence


if __name__ == "__main__":
    _get_title()
