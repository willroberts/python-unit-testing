from dataclasses import dataclass

@dataclass  # Automatically generates `__init__()` method.
class MyDataClass:
    name: str
    value: int

    def add(self, v) -> int:
        self.value += v
        return self.value
