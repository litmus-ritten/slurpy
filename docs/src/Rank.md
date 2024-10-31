# Rank

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Rank

> Auto-generated documentation for [src.Rank](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py) module.

- [Rank](#rank)
  - [Rank](#rank-1)
    - [Rank().__str__](#rank()__str__)
    - [Rank().byte_width](#rank()byte_width)
    - [Rank().external_name](#rank()external_name)
    - [Rank().external_name_plural](#rank()external_name_plural)
    - [Rank.from_str](#rankfrom_str)
    - [Rank().glyph](#rank()glyph)
    - [Rank().internal_name](#rank()internal_name)
    - [Rank().nautical_name](#rank()nautical_name)
    - [Rank().noble_name](#rank()noble_name)
    - [Rank().noble_name_alt](#rank()noble_name_alt)

## Rank

[Show source in Rank.py:61](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L61)

Enumeration of valid Azimuth ranks.

#### Signature

```python
class Rank(Enum): ...
```

### Rank().__str__

[Show source in Rank.py:70](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L70)

Human-readable summary of Rank.

#### Returns

- `str` - A string representation of the Rank.

#### Signature

```python
def __str__(self) -> str: ...
```

### Rank().byte_width

[Show source in Rank.py:144](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L144)

How many bytes (and by extension how many syllables) are used to represent the rank.

#### Returns

- `int` - The byte width of the rank.

#### Signature

```python
@property
def byte_width(self) -> int: ...
```

### Rank().external_name

[Show source in Rank.py:117](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L117)

User-facing name of the rank, following Azimuth's astronomical theme.

#### Returns

- `str` - The external name of the rank.

#### Signature

```python
@property
def external_name(self) -> str: ...
```

### Rank().external_name_plural

[Show source in Rank.py:126](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L126)

User-facing name of the rank, following Azimuth's astronomical theme, pluralised.

#### Returns

- `str` - The external name of the rank, pluralised.

#### Signature

```python
@property
def external_name_plural(self) -> str: ...
```

### Rank.from_str

[Show source in Rank.py:153](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L153)

Parse a string to generate a Rank, or else raise an exception.

#### Arguments

- `s` *str* - String naming the rank according to any of the known conventions.

#### Returns

Any | Exception: A Rank object or an exception if the string is not a known rank name.

#### Raises

- `InvalidRankError` - If the input string is not a known rank name.

#### Signature

```python
@classmethod
def from_str(cls, s: str) -> Any | Exception: ...
```

### Rank().glyph

[Show source in Rank.py:135](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L135)

A cute(?) emoji representation of the rank.

#### Returns

- `str` - Single emoji depicting the rank.

#### Signature

```python
@property
def glyph(self) -> str: ...
```

### Rank().internal_name

[Show source in Rank.py:78](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L78)

Developer-facing name of the rank, following the four-letter noble theme.

#### Returns

- `str` - The internal name of the rank.

#### Signature

```python
@property
def internal_name(self) -> str: ...
```

### Rank().nautical_name

[Show source in Rank.py:105](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L105)

(Ancient) nautical name of the rank.

Sourced from https://alexkrupp.typepad.com/sensemaking/2013/12/a-brief-introduction-to-urbit.html,
of largely historical interest.

#### Returns

- `str` - The nautical name of the rank.

#### Signature

```python
@property
def nautical_name(self) -> str: ...
```

### Rank().noble_name

[Show source in Rank.py:96](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L96)

Noble name of the Rank.

#### Returns

- `str` - The noble name of the rank.

#### Signature

```python
@property
def noble_name(self) -> str: ...
```

### Rank().noble_name_alt

[Show source in Rank.py:87](https://github.com/litmus-ritten/slurpy/blob/main/src/Rank.py#L87)

Alternative noble name of the Rank, based on some lore shared by ~lidreg-dillut.

#### Returns

- `str` - The alternative noble name of the rank.

#### Signature

```python
@property
def noble_name_alt(self) -> str: ...
```