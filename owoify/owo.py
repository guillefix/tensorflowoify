import random
import re
from abc import ABC, abstractmethod

from owoify.constants import kaomoji


class BaseOwoifator(ABC):
    @abstractmethod
    def owoify(self, text: str) -> str:
        pass


class Owoifator(BaseOwoifator):
    _patterns = {
        r"[lr]": "w",
        r"[LR]": "W",
        r"n([aeiou])": lambda m: "ny" + m.group()[1:],
        r"N([aeiou])|N([AEIOU])": lambda m: "Ny" + m.group()[1:],
        "th": "d",
        "ove": "uv",
        "no": "nu",
        r"!+": lambda _: " " + random.choice(kaomoji)
    }

    def owoify(self, text: str) -> str:
        for pattern, repl in self._patterns.items():
            text = re.sub(pattern, repl, text)

        return text
