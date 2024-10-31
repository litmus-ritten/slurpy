# Fleet

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Fleet

> Auto-generated documentation for [src.Fleet](https://github.com/litmus-ritten/slurpy/blob/main/src/Fleet.py) module.

- [Fleet](#fleet)
  - [Fleet](#fleet-1)
    - [Fleet.from_dict](#fleetfrom_dict)

## Fleet

[Show source in Fleet.py:14](https://github.com/litmus-ritten/slurpy/blob/main/src/Fleet.py#L14)

A Tlon Fleet, i.e. a enumeration of subscribed users to a Channel.

#### Attributes

- `contents` *List[Subscriber]* - List of subscribers in the fleet.

#### Signature

```python
class Fleet(BaseModel):
    def __init__(self, **kwargs): ...
```

### Fleet.from_dict

[Show source in Fleet.py:31](https://github.com/litmus-ritten/slurpy/blob/main/src/Fleet.py#L31)

Create a Fleet instance from a dictionary.

#### Arguments

- `d` *dict* - Dictionary containing subscriber information.

#### Returns

- [Fleet](#fleet) - A new Fleet instance.

#### Signature

```python
@classmethod
def from_dict(cls, d: dict) -> "Fleet": ...
```