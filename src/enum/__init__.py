# -*- coding: utf-8 -*-
from enum import Enum
from typing import TypeVar, Type, List, Iterable, cast

from faker.providers import BaseProvider

TEnum = TypeVar("TEnum", bound=Enum)


class EnumProvider(BaseProvider):
    """
    A Provider for enums.
    """

    def enum(self, enum_cls: Type[TEnum]) -> TEnum:

        members: List[TEnum] = list(cast(Iterable[TEnum], enum_cls))
        return self.random_element(members)
