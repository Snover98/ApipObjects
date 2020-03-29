from abc import ABC, abstractmethod


class BaseRestriction(ABC):
    def __init__(self, restriction_name_in_xml: str):
        self.restriction_name_in_xml = restriction_name_in_xml

    @abstractmethod
    def value_matches_restriction(self, value: str) -> bool:
        pass

    @abstractmethod
    def to_type(self, value: str):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __call__(self, value: str):
        if not self.value_matches_restriction(value):
            raise RestrictionException(value, self)


class RestrictionException(Exception):
    def __init__(self, value: str, restriction: BaseRestriction):
        super().__init__("ERROR: value {} does not match restriction {}".format(value, str(restriction)))
