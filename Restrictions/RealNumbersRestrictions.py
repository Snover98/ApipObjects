import re
from abc import ABC

from .BaseRestriction import BaseRestriction


class RealNumberRestriction(BaseRestriction, ABC):
    def __init__(self, restriction_name: str):
        super().__init__(restriction_name)

        self.pattern = re.compile("[0-9]+[\.]?[0-9]*")

    def value_matches_restriction(self, value: str) -> bool:
        return self.pattern.match(value) is not None

    def to_type(self, value: str):
        return float(value)

    def __str__(self) -> str:
        return self.restriction_name_in_xml


class FloatRestriction(RealNumberRestriction):
    def __init__(self):
        super().__init__("float")


class DoubleRestriction(RealNumberRestriction):
    def __init__(self):
        super().__init__("double")
