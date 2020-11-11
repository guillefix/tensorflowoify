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
        "^nn$":"nwn",
        "logits":"lowogits",
        "softmax":"sowftmax",
        "softplus":"sowftplus",
        "softsign":"sowftsign",
        "bitwise_or":"bitwise_owo",
        "raw_ops":"rawr_oops",
        "foldr":"fowdr",
        "foldl":"fowdl",
        "Dot":"Boop",
        "dot":"boop",
        "Dense":"Thicc",
        "DenseNet169":"NiceNet",
        "dense":"thicc",
        "loss$":"iIiIIL",
        "Loss$":"IIiIIL",
        "min$":"smol",
        "max$":"big",
        "prod$":"poke",
        "sqrt$":"skrrr",
        "mean":"nice",
        "Mean":"Nice",
        "top_k":"top_kek",
        "TopK":"TopKeK",
        "swish":"swoosh",
        "feed":"feedme",
        "Feed":"FeedMe",
        "no_gradient":"no_fun_allowed",
        "stop":"stahp",
        "^pow$":"paw",
        "Cudnn$":"Cuddle",
        "aw":"aww",
        "box":"fox",
        "Box":"Fox",
        "erf":"arf",
        "Erf":"Arf",
        "^FFT$":"PFFT",
        "FLoor":"Floof",
        "fLoor":"floof",
        "^For$":"Fur",
        "^for$":"fur",
        "Fresnel":"Fennec",
        "^dropout$":"thiel_fellow",
        # "If":"Yiff",
        # "Diff":"Yiff",
        # "diff":"yiff",
        "Grad$":"GradStudent",
        "GradGrad$":"PostGradStudent",
        "^Logical":"Illogical",
        "^Matrix":"TheMatrix",
        "^Mod$":"DiscordMod",
        "^MulNoNan$":"Mulan",
        "normal":"normie",
        "poisson":"lefishe",
        "Poisson":"LeFishe",
        "stateless":"anarchist",
        "flatten":"flat_is_justice",
        "Flatten":"FlatIsJustice",
        "^reshape$":"im_not_flat",
        "^Reshape$":"ImNotFLAT",
        "^Job":"Joj",
        "transpose":"jojopose",
        "Transpose":"JoJopose",
        "convert_to_tensor":"wololo",
        "assert":"pls_be",
        "debugging":"bughunt",
        "distribute":"share",
        "Error$":"OwO",
        "PermissionDeniedError":"NoTouchOwO",
        "ResourceExhaustedError":"TooMuchOwO",
        "OutOfRangeError":"TooBigOwO",
        "UnknownError":"IDKLOL",
        "UnavailableError":"NotTodayUwU",
        "UnauthenticatedError":"WhoAreU",
        "InvalidArgumentError":"SillyDatDontGoTher",
        "CancelledError":"GotNopedSowwy",
        "AbortedError":"Stahpp",
        "AlreadyExistsError":"BeenThereDoneThat",
        "stop":"stahp",
        "experimental":"fun",
        "hessians":"hissians",
        "initializers":"starters",
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
        # r"!+": lambda _: " " + random.choice(kaomoji),
    }

    def __init__(self):
        self.special_patterns_list = list(enumerate(self._special_patterns.items()))

    def owoify(self, text: str) -> str:
        for i, (pattern, repl) in self.special_patterns_list:
            text = re.sub(pattern, chr(1000+i), text)

        for pattern, repl in self._patterns.items():
            text = re.sub(pattern, repl, text)

        for i, (pattern, repl) in self.special_patterns_list:
            text = re.sub(chr(1000+i), repl, text)

        return text
