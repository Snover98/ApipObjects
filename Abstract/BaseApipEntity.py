from abc import ABC

from typing import List

from .BaseDictable import BaseDictable
from .FieldRecord import FieldRecord


class BaseApipEntity(BaseDictable):
    def __init__(self, field_records: List[FieldRecord]):
        self._field_records = field_records

    def __set_all_missing_to_none(self):
        for field_record in self._field_records:
            if not hasattr(self, field_record.field_name):
                setattr(self, field_record.field_name, None)

    def check_and_convert_all_fields(self):
        self.__set_all_missing_to_none()

        for field_record in self._field_records:
            field_value = getattr(self, field_record.field_name)
            setattr(self, field_record.field_name, field_record.to_type(field_value))
