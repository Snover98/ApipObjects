from typing import Optional

from Restrictions import BaseRestriction


class FieldRecord:
    def __init__(self, field_name: str, restriction: BaseRestriction, is_optional: bool):
        self.field_name = field_name
        self.restriction = restriction
        self.is_optional = is_optional

    def to_type(self, value: Optional[str] = None):
        if self.is_optional and value is None:
            return None

        return self.restriction(value)

