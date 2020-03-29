from abc import ABC

from typing import List

from .utils import get_dict_for_defined_vars
from .BaseApipEntity import BaseApipEntity


class BaseApipMessage(ABC):
    def __init__(self, xs_type: str, entities: List[BaseApipEntity]):
        setattr(self, '@xs:type', xs_type)
        setattr(self, '@numOfEntities', len(entities))
        self.__entities = entities
        self.Entity = [e.to_dict() for e in entities]

    def to_dict(self) -> dict:
        return get_dict_for_defined_vars(self)
