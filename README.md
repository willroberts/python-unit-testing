# Python Unit Testing

Run unit tests with `python3 -m unittest myclass_test mydataclass_test`.

### New in Python 3.10

- Pattern matching:
```python3
match x:
    case 10: print(10)
    case _: print('default')
```
- Union type syntax: `X | Y` powered by `type.__or__()`:
```python3
isinstance(5, int | str)
isinstance(foo, MyClass | None)
``` 
- Type aliases:
```python3
MyType: TypeAlias: "ClassName"
def foo() -> MyType: ...
```

### New in Python 3.11

- TOML in standard library with `tomllib`
- `ExceptionGroup` and `except*` for simultanous exception handling
  - `eg = ExceptionGroup("mygroup", [TypeError(1), ValueError(2), OSError(3)])`
  - `except*` can handle multiple exceptions with one block
- `BaseException.add_note()` allows adding context
- `TypeVarTuple` generics:
```python3
from typing import TypeVarTuple
Shape = TypeVarTuple('Shape')
class Array(Generic[*Shape]): ...
Height = NewType('Height', int)
Width = NewType('Width', int)
x: Array[Height, Width] = Array()
```
- Optional fields in `TypedDict`:
```python3
class Movie(TypedDict):
    title: str
    year: NotRequired[int]
```
- The `Self` type:
```python3
class MyLock:
    def __enter__(self) -> Self:
        self.lock()
        return self
```
- The `LiteralString` type enforces non-arbitrary strings

### New in Python 3.12

- Simplified syntax for generics (compare to 3.11 example):
```python3
Shape = TypeVarTuple('Shape')
class Array[*Shape]: ...
```
- Using `TypedDict` to annotate `**kwargs`:
```python3
from typing import TypedDict, Unpack
class Movie(TypedDict):
    name: str
    year: int
def foo(**kwargs: Unpack[Movie]): ...
```
- New `@override` decorator for subclasses to improve type checking:
```python3
class Base:
    def get_color(self) -> str: return "red"
class Valid:
    @override
    def get_color(self) -> str: return "green"
class Invalid:
    @override
    def get_colour(self) -> str: return "blue"
```

### New in Python 3.13

- Type parameters (`TypeVar`, `ParamSpec`, `TypeVarTuple`) now support defaults
- New `warnings.deprecated()` decorator
- New `typing.ReadOnly` for use with `typing.TypedDict` values
- New `typing.TypeIs` for type narrowing
