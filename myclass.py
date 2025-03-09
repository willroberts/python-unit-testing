#!/usr/bin/env python3.13
from typing import NewType, Optional, Self

Vector = list[int]  # Type alias
SpecialValue = NewType('SpecialValue', int)  # Distinct type


class MyClass(object):
    # Class-private variable
    # Becomes _classname__value to avoid collision with subclasses
    __value: int = 0

    def __init__(self, v: int) -> Self:
        self.value: int = v  # Instance variable
        self._value: int = v  # Private variable
        self.vector: Vector = [v]
        self.special_value: Optional[SpecialValue] = SpecialValue(v)

    def throw() -> None:
        raise Exception()


class MySubClass(MyClass):
    def __init__(self, v: int) -> Self:
        super().__init__(v)

if __name__ == '__main__':
    c: MyClass = MyClass(1)
    print(c.value)  # 1
    c.other_value: int = 2  # Instance object data attribute
    print(c.other_value)  # 2

    s: MySubClass = MySubClass(3)
    print(s.value)  # 3
