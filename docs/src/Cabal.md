# Cabal

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Cabal

> Auto-generated documentation for [src.Cabal](https://github.com/litmus-ritten/slurpy/blob/main/src/Cabal.py) module.

- [Cabal](#cabal)
  - [Cabal](#cabal-1)
    - [Cabal.from_dict](#cabalfrom_dict)

## Cabal

[Show source in Cabal.py:13](https://github.com/litmus-ritten/slurpy/blob/main/src/Cabal.py#L13)

Tlon group cabal (logical grouping of users)

#### Attributes

- `name` *str* - The internal name of the cabal.
- `image` *Optional[Url]* - The image URL of the cabal, if any (this doesn't appear to be used at the moment).
- `title` *str* - The external title of the cabal.
- `cover` *Optional[Url]* - The cover image URL of the cabal, if any (this doesn't appear to be used at the moment).
- `description` *str* - The description of the cabal.

#### Signature

```python
class Cabal(BaseModel):
    def __init__(self, **kwargs: Any) -> None: ...
```

### Cabal.from_dict

[Show source in Cabal.py:38](https://github.com/litmus-ritten/slurpy/blob/main/src/Cabal.py#L38)

Create a Cabal instance from a dictionary.

#### Arguments

- `k` *str* - The key representing the cabal name.
d (Dict[str, Any]): The dictionary containing cabal data.

#### Returns

- [Cabal](#cabal) - A new Cabal instance created from the provided data.

#### Signature

```python
@classmethod
def from_dict(cls, k: str, d: dict[str, Any]) -> "Cabal": ...
```