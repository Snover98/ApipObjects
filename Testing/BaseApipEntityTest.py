from Abstract import BaseApipEntity, FieldRecord
from Restrictions import *
from typing import List

class NumIfApipEntity(BaseApipEntity):
    def __init__(self, field_records: List[FieldRecord.FieldRecord], value: int):
        self.numIf = value
        super().__init__(field_records)

class JhonApipEntity(BaseApipEntity):
    def __init__(self, field_records: List[FieldRecord.FieldRecord], value: int):
        self.Jhon = value
        super().__init__(field_records)

class MarkApipEntity(BaseApipEntity):
    def __init__(self, field_records: List[FieldRecord.FieldRecord], value: int):
        self.Mark = value
        super().__init__(field_records)

class JosephApipEntity(BaseApipEntity):
    def __init__(self, field_records: List[FieldRecord.FieldRecord], value: int):
        self.Joseph = value
        super().__init__(field_records)

unsigned_restriction = UnsignedIntIntegerRestriction()
byte_restriction = ByteIntegerRestriction()
string_restriction = StringRestriction()
double_restriction = DoubleRestriction()
field_records = [FieldRecord.FieldRecord("numIf", unsigned_restriction, True), FieldRecord.FieldRecord("Jhon", byte_restriction, True), FieldRecord.FieldRecord("Mark", string_restriction, True)
                 ,FieldRecord.FieldRecord("Joseph", double_restriction, True)]

print("Testing Integer Restrictions...")
num_if_apip = NumIfApipEntity(field_records, "10")
print("Testing unsigned restriction:")
print("Before converting: ", getattr(num_if_apip, "numIf"))
num_if_apip.check_and_convert_all_fields()
print("After converting: ", getattr(num_if_apip, "numIf"))

jhon_apip = JhonApipEntity(field_records, "10")
print("\nTesting byte restriction:")
print("Before converting: ", getattr(jhon_apip, "Jhon"))
jhon_apip.check_and_convert_all_fields()
print("After converting: ", getattr(jhon_apip, "Jhon"))

print("\nTesting Real Numbers Restrictions...")
joseph_apip = JosephApipEntity(field_records, "10")
print("Testing double restriction:")
print("Before converting: ", getattr(joseph_apip, "Joseph"))
joseph_apip.check_and_convert_all_fields()
print("After converting: ", getattr(joseph_apip, "Joseph"))

print("\nTesting String Restrictions...")
mark_apip = MarkApipEntity(field_records, "10")
print("Testing string restriction:")
print("Before converting: ", getattr(mark_apip, "Mark"))
mark_apip.check_and_convert_all_fields()
print("After converting: ", getattr(mark_apip, "Mark"))


