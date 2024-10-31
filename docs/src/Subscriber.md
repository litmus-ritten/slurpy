# Subscriber

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Subscriber

> Auto-generated documentation for [src.Subscriber](https://github.com/litmus-ritten/slurpy/blob/main/src/Subscriber.py) module.

- [Subscriber](#subscriber)
  - [Subscriber](#subscriber-1)
    - [Subscriber.from_dict](#subscriberfrom_dict)

## Subscriber

[Show source in Subscriber.py:16](https://github.com/litmus-ritten/slurpy/blob/main/src/Subscriber.py#L16)

A Tlon Channel Subscriber.

#### Attributes

- `point` *Point* - The user's Point.
- `join_datetime` *datetime* - The datetime when the user joined, in Urbit timestamp format.
- `sects` *List[Any]* - An enumeration of sects.

#### Signature

```python
class Subscriber(BaseModel):
    def __init__(self, **kwargs) -> None: ...
```

### Subscriber.from_dict

[Show source in Subscriber.py:42](https://github.com/litmus-ritten/slurpy/blob/main/src/Subscriber.py#L42)

Parse a key, value pair representing a Subscriber from a Fleet record.

#### Arguments

- `k` *str* - The key representing the subscriber's patp.
- `d` *dict* - The dictionary containing subscriber data.

#### Returns

- [Subscriber](#subscriber) - A new Subscriber instance.

#### Signature

```python
@classmethod
def from_dict(cls, k: str, d: dict) -> "Subscriber": ...
```