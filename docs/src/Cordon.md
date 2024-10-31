# Cordon

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Cordon

> Auto-generated documentation for [src.Cordon](https://github.com/litmus-ritten/slurpy/blob/main/src/Cordon.py) module.

- [Cordon](#cordon)
  - [Cordon](#cordon-1)
    - [Cordon().__str__](#cordon()__str__)
    - [Cordon.from_dict](#cordonfrom_dict)
    - [Cordon().pp](#cordon()pp)

## Cordon

[Show source in Cordon.py:17](https://github.com/litmus-ritten/slurpy/blob/main/src/Cordon.py#L17)

Tlon group cordon (bans, invites and permissions).

#### Attributes

- `banned_ships` - Named @ps which are banned.
- `banned_ranks` - Ranks which are be banned.
- `invited_ships` - Named @ps which have been invited to a private or secret group (but have not joined?).
- `asking_ships` - @ps which have asked to enter a private (or secret?) group but have not yet been permitted.

#### Signature

```python
class Cordon(BaseModel):
    def __init__(self, **kwarg): ...
```

### Cordon().__str__

[Show source in Cordon.py:71](https://github.com/litmus-ritten/slurpy/blob/main/src/Cordon.py#L71)

Returns a string representation of the Cordon object.

#### Returns

- `str` - A formatted string containing the Cordon object's attributes.

#### Signature

```python
def __str__(self) -> str: ...
```

### Cordon.from_dict

[Show source in Cordon.py:36](https://github.com/litmus-ritten/slurpy/blob/main/src/Cordon.py#L36)

Create a Cordon instance from a dictionary.

#### Arguments

- `d` *dict* - A dictionary containing cordon data.

#### Returns

- [Cordon](#cordon) - A new Cordon instance.

#### Raises

- `ValueError` - If the input dictionary is invalid.

#### Signature

```python
@classmethod
def from_dict(cls, d: dict) -> "Cordon": ...
```

### Cordon().pp

[Show source in Cordon.py:88](https://github.com/litmus-ritten/slurpy/blob/main/src/Cordon.py#L88)

Returns a pretty-printed Panel representation of the Cordon object.

#### Returns

- `Panel` - A rich Panel summarising the Cordon object's attributes.

#### Signature

```python
@property
def pp(self) -> Panel: ...
```