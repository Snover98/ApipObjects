from abc import ABC

from typing import List

from .BaseDictable import BaseDictable
from .BaseApipEntity import BaseApipEntity


class BaseApipMessage(ABC, BaseDictable):
    def __init__(self, xs_type: str, entities: List[BaseApipEntity]):
        setattr(self, '@xs:type', xs_type)
        setattr(self, '@numOfEntities', len(entities))
        self.__entities = entities
        self.Entity = [e.to_dict() for e in entities]
