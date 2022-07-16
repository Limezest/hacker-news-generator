import markovify
import random

from flask import render_template

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


def title_bot(request):
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
