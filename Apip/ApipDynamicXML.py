import xmltodict

from typing import List

from Abstract import BaseApipMessage, BaseDictable


class ApipDynamicXML(BaseDictable):
    def __init__(self, *messages: BaseApipMessage):
        setattr(self, '@xmlns', 'apip')
        setattr(self, '@xmlns:xs', 'https://www.w3.org/2001/')

        self.__messages = messages
        self.Message = [m.to_dict() for m in messages]

    def to_xml(self) -> str:
        return xmltodict.parse(self.to_dict())

    def __str__(self) -> str:
        return self.to_xml()


