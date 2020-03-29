from typing import Optional

from .BaseRestriction import BaseRestriction


class StringRestriction(BaseRestriction):
    def __init__(self, length: Optional[int] = None):
        super().__init__("string")

        self.length = length

    def value_matches_restriction(self, value: str) -> bool:
        return self.length is None or len(value) <= self.length

    def to_type(self, value: str):
        return value

    def __str__(self) -> str:
        if self.length is None:
            return 'str'
        else:
            return 'str not longer than {}'.format(self.length)
