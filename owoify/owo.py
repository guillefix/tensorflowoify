import random
import re
from abc import ABC, abstractmethod

from owoify.constants import kaomoji


class BaseOwoifator(ABC):
    @abstractmethod
    def owoify(self, text: str) -> str:
        pass

class Owoifator(BaseOwoifator):
    _special_patterns = {
        "math":"mawth",
        "nn":"nwn",
        "logits":"lowogits",
        "softmax":"sowftmax",
        "bitwise_or":"bitwise_owo",
        "raw_ops":"rawr_oops",
        "foldr":"fowdr",
        "foldl":"fowdl",
        "Dot":"Boop",
        "dot":"boop",
        "Dense":"Thicc",
        "dense":"thicc",
        "loss$":"iIiIIL",
        "Loss$":"IIiIIL",
    }
    _patterns = {
        r"[lr]": "w",
        r"[LR]": "W",
        r"n([aeiou])": "ny\\1",
        r"N([aeiou])": "Ny\\1",
        r"N([AEIOU])": "NY\\1",
        "th": "d",
        "ove": "uv",
        "no": "nu",
        r"!+": lambda _: " " + random.choice(kaomoji),
    }



    def owoify(self, text: str) -> str:
        special_patterns = list(enumerate(self._special_patterns.items()))
        for i, (pattern, repl) in special_patterns:
            text = re.sub(pattern, chr(i), text)

        for pattern, repl in self._patterns.items():
            text = re.sub(pattern, repl, text)

        for i, (pattern, repl) in special_patterns:
            text = re.sub(chr(i), repl, text)

        return text
