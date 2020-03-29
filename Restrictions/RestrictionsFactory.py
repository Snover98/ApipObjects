from .IntegerRestrictions import *
from .RealNumbersRestrictions import FloatRestriction, DoubleRestriction
from .StringRestriction import StringRestriction


class RestrictionsFactory:
    restrictions_dict = {
        IntegerRestriction.RESTRICTION_NAME_IN_XML: IntegerRestriction,
        NonPositiveIntegerRestriction.RESTRICTION_NAME_IN_XML: NonPositiveIntegerRestriction,
        NegativeIntegerRestriction.RESTRICTION_NAME_IN_XML: NegativeIntegerRestriction,
        NonNegativeIntegerRestriction.RESTRICTION_NAME_IN_XML: NonNegativeIntegerRestriction,
        PositiveIntegerRestriction.RESTRICTION_NAME_IN_XML: PositiveIntegerRestriction,
        LongIntegerRestriction.RESTRICTION_NAME_IN_XML: LongIntegerRestriction,
        IntIntegerRestriction.RESTRICTION_NAME_IN_XML: IntIntegerRestriction,
        ShortIntegerRestriction.RESTRICTION_NAME_IN_XML: ShortIntegerRestriction,
        ByteIntegerRestriction.RESTRICTION_NAME_IN_XML: ByteIntegerRestriction,
        UnsignedLongIntegerRestriction.RESTRICTION_NAME_IN_XML: UnsignedLongIntegerRestriction,
        UnsignedIntIntegerRestriction.RESTRICTION_NAME_IN_XML: UnsignedIntIntegerRestriction,
        UnsignedShortIntegerRestriction.RESTRICTION_NAME_IN_XML: UnsignedShortIntegerRestriction,
        UnsignedByteIntegerRestriction.RESTRICTION_NAME_IN_XML: UnsignedByteIntegerRestriction,
        FloatRestriction.RESTRICTION_NAME_IN_XML: FloatRestriction,
        DoubleRestriction.RESTRICTION_NAME_IN_XML: DoubleRestriction,
        StringRestriction.RESTRICTION_NAME_IN_XML: StringRestriction
    }

    @staticmethod
    def get_restriction(restriction_name):
        restriction_class = RestrictionsFactory.restrictions_dict.get(restriction_name)

        if restriction_class is None:
            raise Exception("ERROR: no restriction named {}".format(restriction_name))

        return restriction_class

