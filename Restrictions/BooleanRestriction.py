from .BaseRestriction import *


class BooleanRestriction(BaseRestriction):
    RESTRICTION_NAME_IN_XML = 'boolean'

    def __init__(self):
        super().__init__()

    def value_matches_restriction(self, value: str) -> bool:
        return value.lower() == 'true' or value.lower() == 'false'

    def to_type(self, value: str):
        return value.lower() == 'true'

    def __str__(self) -> str:
        return self.RESTRICTION_NAME_IN_XML
