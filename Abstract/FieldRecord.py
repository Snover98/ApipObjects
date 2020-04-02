from typing import Optional, Dict

from Restrictions import *


class FieldRecord:
    def __init__(self, field_name: str, restriction: BaseRestriction, is_optional: bool):
        self.field_name = field_name
        self.restriction = restriction
        self.is_optional = is_optional

    def to_type(self, value: Optional[str] = None):
        if self.is_optional and value is None:
            return None

        return self.restriction(value)

    def __call__(self, value: Optional[str] = None):
        return self.to_type(value)


def field_records_dict(*records: FieldRecord) -> Dict[str, FieldRecord]:
    return {record.field_name: record for record in records}
