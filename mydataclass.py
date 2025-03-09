#!/usr/bin/env python3.13
from dataclasses import dataclass

@dataclass  # Automatically generates `__init__()` method.
class MyDataClass:
    name: str
    value: int

    def add(self, v) -> int:
        self.value += v
        return self.value

if __name__ == '__main__':
    d = MyDataClass('example', 1)
    v = d.add(10)
