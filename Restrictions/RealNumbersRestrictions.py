import re
from abc import ABC

from .BaseRestriction import BaseRestriction


class RealNumberRestriction(BaseRestriction, ABC):
    def __init__(self):
        self.pattern = re.compile("[0-9]+[\.]?[0-9]*")

    def value_matches_restriction(self, value: str) -> bool:
        return self.pattern.match(value) is not None

    def to_type(self, value: str):
        return float(value)

    def __str__(self) -> str:
        return getattr(self, "RESTRICTION_NAME_IN_XML")


class FloatRestriction(RealNumberRestriction):
    RESTRICTION_NAME_IN_XML = "float"

    def __init__(self):
        super().__init__()


class DoubleRestriction(RealNumberRestriction):
    RESTRICTION_NAME_IN_XML = "double"

    def __init__(self):
        super().__init__()
