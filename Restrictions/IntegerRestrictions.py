import re
from abc import abstractmethod

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
    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(IntegerRestriction(), minInclusive=minInclusive, maxInclusive=maxInclusive)


class BaseInGivenRangeIntegerRestriction(BaseRangeIntegerRestriction):
    MinRangeEdge = None
    MaxRangeEdge = None

    @abstractmethod
    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        minimum, maximum = minInclusive, maxInclusive
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

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class NegativeIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "negativeInteger"
    MaxRangeEdge = -1

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class NonNegativeIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "nonNegativeInteger"
    MinRangeEdge = 0

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class PositiveIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "positiveInteger"
    MinRangeEdge = 1

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class LongIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "long"
    MinRangeEdge = -9223372036854775808
    MaxRangeEdge = 9223372036854775807

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class IntIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "int"
    MinRangeEdge = -2147483648
    MaxRangeEdge = 2147483647

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class ShortIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "short"
    MinRangeEdge = -32768
    MaxRangeEdge = 32767

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class ByteIntegerRestriction(BaseInGivenRangeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "byte"
    MinRangeEdge = -128
    MaxRangeEdge = 127

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class UnsignedLongIntegerRestriction(NonNegativeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedLong"
    MaxRangeEdge = 18446744073709551615

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class UnsignedIntIntegerRestriction(NonNegativeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedInt"
    MaxRangeEdge = 4294967295

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class UnsignedShortIntegerRestriction(NonNegativeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedShort"
    MaxRangeEdge = 65535

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)


class UnsignedByteIntegerRestriction(NonNegativeIntegerRestriction):
    RESTRICTION_NAME_IN_XML = "unsignedByte"
    MaxRangeEdge = 255

    def __init__(self, minInclusive: Optional[int] = None, maxInclusive: Optional[int] = None):
        super().__init__(minInclusive=minInclusive, maxInclusive=maxInclusive)
