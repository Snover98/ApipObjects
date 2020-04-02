import Restrictions

from Restrictions.IntegerRestrictions import *
from Restrictions.RealNumbersRestrictions import FloatRestriction, DoubleRestriction
from Restrictions.StringRestriction import StringRestriction


class RestrictionsFactory:
    @staticmethod
    def __get_restriction_classes():
        return [obj for name, obj in vars(Restrictions).items() if name.endswith('Restriction')]

    @staticmethod
    def __get_restrictions_dict_from_classes(restriction_classes: list) -> dict:
        return {restriction_class.RESTRICTION_NAME_IN_XML: restriction_class for restriction_class in
                restriction_classes}

    @staticmethod
    def __get_restrictions_dict() -> dict:
        return RestrictionsFactory.__get_restrictions_dict_from_classes(RestrictionsFactory.__get_restriction_classes())

    restrictions_dict = __get_restrictions_dict()

    @staticmethod
    def get_restriction(restriction_name):
        restriction_class = RestrictionsFactory.restrictions_dict.get(restriction_name)

        if restriction_class is None:
            raise Exception("ERROR: no restriction named {}".format(restriction_name))

        return restriction_class
