from abc import ABC

from typing import List

from .BaseApipEntity import BaseApipEntity


class BaseApipMessage(ABC):
    def __init__(self, xs_type: str, entities: List[BaseApipEntity]):
        setattr(self, '@xs:type', xs_type)
        setattr(self, '@numOfEntities', len(entities))
        self.Entity = [e.to_dict() for e in entities]

    def to_dict(self) -> dict:
        return {key: value for key, value in vars(self) if not key.startswith('_') and value is not None}
