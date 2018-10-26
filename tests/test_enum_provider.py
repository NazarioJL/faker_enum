# -*- coding: utf-8 -*-
from enum import Enum, IntEnum


class StubEnum(Enum):
    A = 1
    B = 2


class StrEnum(str, Enum):
    A = "a"
    B = "b"


class NumEnum(IntEnum):
    A = 1
    B = 2


class SingleMemberEnum(Enum):
    A = 1


def test_enum(fake):
    result = fake.enum(StubEnum)
    assert result == StubEnum.A or result == StubEnum.B


def test_str_enum(fake):
    result = fake.enum(StrEnum)
    assert result == StrEnum.A or result == StrEnum.B


def test_int_enum(fake):
    result = fake.enum(NumEnum)
    assert result == NumEnum.A or result == NumEnum.B


def test_single_member_enum(fake):
    result = fake.enum(SingleMemberEnum)
    assert result == SingleMemberEnum.A
