import random
import re

from owoify.constants import kaomoji


def owoify(text: str) -> str:
    text = re.sub(r"[lr]", "w", text)
    text = re.sub(r"[LR]", "W", text)
    text = re.sub(r"n([aeiou])", lambda m: "ny" + m.group()[1:], text)
    text = re.sub(r"N([aeiou])|N([AEIOU])", lambda m: "Ny" + m.group()[1:], text)
    text = re.sub("th", "d", text)
    text = re.sub("ove", "uv", text)
    text = re.sub(r"!+", lambda _: " " + random.choice(kaomoji), text)

    return text
