# Cabal

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Cabal

> Auto-generated documentation for [slurpy.Cabal](../../slurpy/Cabal.py) module.

- [Cabal](#cabal)
  - [Cabal](#cabal-1)
    - [Cabal.from_dict](#cabalfrom_dict)

## Cabal

[Show source in Cabal.py:9](../../slurpy/Cabal.py#L9)

Tlon group cabal (logical grouping of users)

#### Attributes

- `name` *str* - The internal name of the cabal.
- `image` *Optional[Url]* - The image URL of the cabal, if any (this doesn't appear to be used at the moment).
- `title` *str* - The external title of the cabal.
- `cover` *Optional[Url]* - The cover image URL of the cabal, if any (this doesn't appear to be used at the moment)..
- `description` *str* - The description of the cabal.

#### Signature

```python
class Cabal(BaseModel):
    def __init__(self, **kwargs: Any) -> None: ...
```

### Cabal.from_dict

[Show source in Cabal.py:34](../../slurpy/Cabal.py#L34)

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