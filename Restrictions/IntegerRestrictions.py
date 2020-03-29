import re
from abc import ABC

from typing import Optional

from .BaseRestriction import BaseRestriction
from .RangeInclusiveRestriction import RangeInclusiveRestriction


class IntegerRestriction(BaseRestriction):
    def __init__(self, restriction_name_in_xml: str = 'integer'):
        super().__init__(restriction_name_in_xml)

        self.pattern = re.compile("[\-+]?[0-9]+")

    def value_matches_restriction(self, value) -> bool:
        return self.pattern.match(value) is not None

    def to_type(self, value: str) -> int:
        return int(value)

    def __str__(self) -> str:
        return "INTEGER"


class BaseRangeIntegerRestriction(RangeInclusiveRestriction, ABC):
    def __init__(self, restriction_name_in_xml: str, minimum: Optional[int] = None, maximum: Optional[int] = None):
        super().__init__(IntegerRestriction(), restriction_name_in_xml, minimum, maximum)


class BaseInGivenRangeIntegerRestriction(BaseRangeIntegerRestriction, ABC):
    MinRangeEdge = None
    MaxRangeEdge = None

    def __init__(self, restriction_name_in_xml: str, minimum: Optional[int] = None, maximum: Optional[int] = None):
        min_range_edge = getattr(self, 'MinRangeEdge')
        if minimum is None:
            minimum = min_range_edge
        elif minimum < min_range_edge:
            raise Exception("minimum {} lower than the defined range's minimum {}".format(minimum, min_range_edge))

        max_edge_range = getattr(self, 'MaxRangeEdge')
        if maximum is None:
            maximum = max_edge_range
        elif maximum > max_edge_range:
            raise Exception("maximum {} higher than the defined range's maximum {}".format(maximum, max_edge_range))

        super().__init__(restriction_name_in_xml, minimum, maximum)


class NonPositiveIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MaxRangeEdge = 0

    def __init__(self, restriction_name_in_xml: str = "nonPositiveInteger", minimum: Optional[int] = None):
        super().__init__(minimum=minimum, restriction_name_in_xml=restriction_name_in_xml)


class NegativeIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MaxRangeEdge = -1

    def __init__(self, restriction_name_in_xml: str = "negativeInteger", minimum: Optional[int] = None):
        super().__init__(minimum=minimum, restriction_name_in_xml=restriction_name_in_xml)


class NonNegativeIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MinRangeEdge = 0

    def __init__(self, restriction_name_in_xml: str = "nonNegativeInteger", maximum: Optional[int] = None):
        super().__init__(maximum=maximum, restriction_name_in_xml=restriction_name_in_xml)


class PositiveIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MinRangeEdge = 1

    def __init__(self, restriction_name_in_xml: str = "positiveInteger", maximum: Optional[int] = None):
        super().__init__(maximum=maximum, restriction_name_in_xml=restriction_name_in_xml)


class LongIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MinRangeEdge = -9223372036854775808
    MaxRangeEdge = 9223372036854775807

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__("long", minimum, maximum)


class IntIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MinRangeEdge = -2147483648
    MaxRangeEdge = 2147483647

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__("int", minimum, maximum)


class ShortIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MinRangeEdge = -32768
    MaxRangeEdge = 32767

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__("short", minimum, maximum)


class ByteIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MinRangeEdge = -128
    MaxRangeEdge = 127

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__("byte", minimum, maximum)


class UnsignedLongIntegerRestriction(NonNegativeIntegerRestriction):
    MaxRangeEdge = 18446744073709551615

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__("unsignedLong", maximum)


class UnsignedIntIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    MaxRangeEdge = 4294967295

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__("unsignedInt", maximum)


class UnsignedShortIntegerRestriction(NonNegativeIntegerRestriction):
    MaxRangeEdge = 65535

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__("unsignedShort", maximum)


class UnsignedByteIntegerRestriction(NonNegativeIntegerRestriction):
    MaxRangeEdge = 255

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__("unsignedByte", maximum)
