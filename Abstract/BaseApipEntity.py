from abc import ABC

from .utils import get_dict_for_defined_vars


class BaseApipEntity(ABC):
    def to_dict(self):
        return get_dict_for_defined_vars(self)
