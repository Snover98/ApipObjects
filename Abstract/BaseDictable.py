from abc import ABC


class BaseDictable(ABC):
    def to_dict(self):
        return {key: value for key, value in vars(self) if not key.startswith('_') and value is not None}
