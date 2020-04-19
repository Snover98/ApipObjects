from typing import Optional

from .BaseRestriction import BaseRestriction


class StringRestriction(BaseRestriction):
    RESTRICTION_NAME_IN_XML = "string"

    def __init__(self, length: Optional[int] = None):
        self.length = length

    def __string_matches_length(self, value: str):
        return self.length is None or len(value) <= self.length

    def value_matches_restriction(self, value: str) -> bool:
        return type(value) is str and self.__string_matches_length(value)

    def to_type(self, value: str) -> str:
        return value

    def __str__(self) -> str:
        if self.length is None:
            return 'string'
        else:
            return 'string with length <= {}'.format(self.length)
