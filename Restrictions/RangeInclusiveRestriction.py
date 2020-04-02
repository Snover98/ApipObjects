from typing import Optional

from .BaseRestriction import *


class RangeInclusiveRestriction(BaseRestriction):
    def __init__(self, parent_restriction: BaseRestriction, minimum: Optional = None,
                 maximum: Optional = None):
        self.parent_restriction = parent_restriction
        self.minimum = minimum
        self.maximum = maximum

        if minimum is None and maximum is None:
            raise Exception("ERROR: Illegal range, at least one of the minimum and maximum must be defined")

        if minimum is not None and maximum is not None and maximum < minimum:
            raise Exception("ERROR: Illegal range, maximum={} is less than minimum={}".format(maximum, minimum))

    def value_matches_restriction(self, value) -> bool:
        try:
            value_converted = self.parent_restriction(value)
        except RestrictionException as e:
            return False

        if self.minimum is None:
            return value_converted <= self.maximum
        elif self.maximum is None:
            return self.minimum <= value_converted
        else:
            return self.minimum <= value_converted <= self.maximum

    def __bounds_range(self) -> str:
        if self.minimum is None:
            min_str = '-∞'
        else:
            min_str = str(self.minimum)

        if self.maximum is None:
            max_str = '∞'
        else:
            max_str = str(self.maximum)

        return "[{}, {}]".format(min_str, max_str)

    def to_type(self, value):
        self.parent_restriction.to_type(value)

    def __str__(self) -> str:
        return '{{} in range {}}'.format(self.parent_restriction, self.__bounds_range())
