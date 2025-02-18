# Cordon

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Cordon

> Auto-generated documentation for [slurpy.Cordon](../../slurpy/Cordon.py) module.

- [Cordon](#cordon)
  - [Cordon](#cordon-1)
    - [Cordon().__str__](#cordon()__str__)
    - [Cordon.from_dict](#cordonfrom_dict)
    - [Cordon().pp](#cordon()pp)

## Cordon

[Show source in Cordon.py:14](../../slurpy/Cordon.py#L14)

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

[Show source in Cordon.py:68](../../slurpy/Cordon.py#L68)

Returns a string representation of the Cordon object.

#### Returns

- `str` - A formatted string containing the Cordon object's attributes.

#### Signature

```python
def __str__(self) -> str: ...
```

### Cordon.from_dict

[Show source in Cordon.py:33](../../slurpy/Cordon.py#L33)

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

[Show source in Cordon.py:85](../../slurpy/Cordon.py#L85)

Returns a pretty-printed Panel representation of the Cordon object.

#### Returns

- `Panel` - A rich Panel summarising the Cordon object's attributes.

#### Signature

```python
@property
def pp(self) -> Panel: ...
```