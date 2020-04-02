import re
from abc import ABC

from typing import Optional, Union

from .BaseRestriction import BaseRestriction
from .RangeInclusiveRestriction import RangeInclusiveRestriction


class IntegerRestriction(BaseRestriction):
    RESTRICTION_NAME_IN_XML = 'integer'

    def __init__(self):
        self.pattern = re.compile("[-+]?[0-9]+")

    def value_matches_restriction(self, value: Union[str, int]) -> bool:
        return type(value) is int or self.pattern.match(value) is not None

    def to_type(self, value: str) -> int:
        return int(value)

    def __str__(self) -> str:
        return "INTEGER"


class BaseRangeIntegerRestriction(RangeInclusiveRestriction, ABC):
    def __init__(self, minimum: Optional[int] = None, maximum: Optional[int] = None):
        super().__init__(IntegerRestriction(), minimum, maximum)


class BaseInGivenRangeIntegerRestriction(BaseRangeIntegerRestriction, ABC):
    MinRangeEdge = None
    MaxRangeEdge = None

    def __init__(self, minimum: Optional[int] = None, maximum: Optional[int] = None):
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

        super().__init__(minimum, maximum)


class NonPositiveIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "nonPositiveInteger"
    MaxRangeEdge = 0

    def __init__(self, minimum: Optional[int] = None):
        super().__init__(minimum=minimum)


class NegativeIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "negativeInteger"
    MaxRangeEdge = -1

    def __init__(self, minimum: Optional[int] = None):
        super().__init__(minimum=minimum)


class NonNegativeIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "nonNegativeInteger"
    MinRangeEdge = 0

    def __init__(self, maximum: Optional[int] = None):
        super().__init__(maximum=maximum)


class PositiveIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "positiveInteger"
    MinRangeEdge = 1

    def __init__(self, maximum: Optional[int] = None):
        super().__init__(maximum=maximum)


class LongIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "long"
    MinRangeEdge = -9223372036854775808
    MaxRangeEdge = 9223372036854775807

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__(minimum, maximum)


class IntIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "int"
    MinRangeEdge = -2147483648
    MaxRangeEdge = 2147483647

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__(minimum, maximum)


class ShortIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "short"
    MinRangeEdge = -32768
    MaxRangeEdge = 32767

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__(minimum, maximum)


class ByteIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "byte"
    MinRangeEdge = -128
    MaxRangeEdge = 127

    def __init__(self, minimum: int = MinRangeEdge, maximum: int = MaxRangeEdge):
        super().__init__(minimum, maximum)


class UnsignedLongIntegerRestriction(NonNegativeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedLong"
    MaxRangeEdge = 18446744073709551615

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__(maximum)


class UnsignedIntIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedInt"
    MaxRangeEdge = 4294967295

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__(maximum)


class UnsignedShortIntegerRestriction(NonNegativeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedShort"
    MaxRangeEdge = 65535

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__(maximum)


class UnsignedByteIntegerRestriction(NonNegativeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedByte"
    MaxRangeEdge = 255

    def __init__(self, maximum: int = MaxRangeEdge):
        super().__init__(maximum)
