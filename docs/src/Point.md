# Point

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Point

> Auto-generated documentation for [src.Point](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py) module.

- [Point](#point)
  - [Form](#form)
  - [Point](#point-1)
    - [Point().__ge__](#point()__ge__)
    - [Point().__gt__](#point()__gt__)
    - [Point().__hash__](#point()__hash__)
    - [Point().__le__](#point()__le__)
    - [Point().__lt__](#point()__lt__)
    - [Point().__str__](#point()__str__)
    - [Point().ancestors](#point()ancestors)
    - [Point().ancestors_patp_dict](#point()ancestors_patp_dict)
    - [Point().ancestors_patp_list](#point()ancestors_patp_list)
    - [Point().cartouche](#point()cartouche)
    - [Point().child_of](#point()child_of)
    - [Point().cousin_of](#point()cousin_of)
    - [Point.from_hex](#pointfrom_hex)
    - [Point.from_num](#pointfrom_num)
    - [Point.from_patq](#pointfrom_patq)
    - [Point().galaxy](#point()galaxy)
    - [Point().grandparent](#point()grandparent)
    - [Point().greatgrandparent](#point()greatgrandparent)
    - [Point().index](#point()index)
    - [Point().index_delimited](#point()index_delimited)
    - [Point().index_hex](#point()index_hex)
    - [Point().parent](#point()parent)
    - [Point().parent_of](#point()parent_of)
    - [Point().patp_indices](#point()patp_indices)
    - [Point().patp_syllables](#point()patp_syllables)
    - [Point().patq](#point()patq)
    - [Point().patq_indices](#point()patq_indices)
    - [Point().patq_syllables](#point()patq_syllables)
    - [Point().planet](#point()planet)
    - [Point().rank](#point()rank)
    - [Point().related](#point()related)
    - [Point().root](#point()root)
    - [Point().sibling_of](#point()sibling_of)
    - [Point().star](#point()star)
    - [Point().syllable_indices](#point()syllable_indices)
    - [Point().syllables](#point()syllables)
  - [ValidPatp](#validpatp)

## Form

[Show source in Point.py:27](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L27)

Enumeration of valid syllabic encodings of a Point. PAPT is 'scrambled' to obscure star/planet relations, PATQ is not.

#### Signature

```python
class Form(Enum): ...
```



## Point

[Show source in Point.py:98](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L98)

Represents a point in the Urbit network.

#### Attributes

- `patp` *str* - The @p address of the point.

#### Signature

```python
class Point(BaseModel): ...
```

### Point().__ge__

[Show source in Point.py:570](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L570)

Compares this Point with another for greater than or equal to.

#### Arguments

- `other` - Another Point object to compare with.

#### Returns

- `bool` - True if this Point's index is greater than or equal to the other's, False otherwise.

#### Signature

```python
def __ge__(self, other): ...
```

### Point().__gt__

[Show source in Point.py:559](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L559)

Compares this Point with another for greater than.

#### Arguments

- `other` - Another Point object to compare with.

#### Returns

- `bool` - True if this Point's index is greater than the other's, False otherwise.

#### Signature

```python
def __gt__(self, other): ...
```

### Point().__hash__

[Show source in Point.py:529](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L529)

Computes the hash value for the Point.

#### Returns

- `int` - The hash value of the string representation of the Point.

#### Signature

```python
def __hash__(self): ...
```

### Point().__le__

[Show source in Point.py:548](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L548)

Compares this Point with another for less than or equal to.

#### Arguments

- `other` - Another Point object to compare with.

#### Returns

- `bool` - True if this Point's index is less than or equal to the other's, False otherwise.

#### Signature

```python
def __le__(self, other): ...
```

### Point().__lt__

[Show source in Point.py:537](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L537)

Compares this Point with another for less than.

#### Arguments

- `other` - Another Point object to compare with.

#### Returns

- `bool` - True if this Point's index is less than the other's, False otherwise.

#### Signature

```python
def __lt__(self, other): ...
```

### Point().__str__

[Show source in Point.py:521](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L521)

Returns a string representation of the Point.

#### Returns

- `str` - A string containing the rank glyph and patp of the Point.

#### Signature

```python
def __str__(self) -> str: ...
```

### Point().ancestors

[Show source in Point.py:418](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L418)

Evaluate the chain of ancestors of a Point through recursive tree ascent.

#### Returns

- `List[Any]` - A list of the ancestors of a Point in ascending order.

#### Signature

```python
@property
def ancestors(self) -> list[Any]: ...
```

### Point().ancestors_patp_dict

[Show source in Point.py:363](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L363)

Returns the ancestor list of a Point as a dictionary.

#### Returns

- `dict` - The ancestor list of the Point as a dictionary where the keys are non-null relations.

#### Signature

```python
@computed_field
@property
def ancestors_patp_dict(self) -> dict: ...
```

### Point().ancestors_patp_list

[Show source in Point.py:354](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L354)

Returns the ancestor list of a Point in ascending order of @ps.

#### Returns

- `List[str]` - The ancestor list of the Point in ascending order of @ps.

#### Signature

```python
@property
def ancestors_patp_list(self) -> list[str]: ...
```

### Point().cartouche

[Show source in Point.py:581](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L581)

Cartouche representation of a Point, as a capsule with up to two colours.
Coefficients for determining correct light/dark text are from Max Chuhryaev (w3core on GitHub) but I'm not sure quite where they were mentioned.

#### Arguments

- `pq` *str, optional* - Determines whether to use 'patp' or 'patq' indexing. Defaults to "q".

#### Returns

- `Text` - A Rich Text object representing the cartouche.

TODO:
    Refactor this method, as it's currently complex and difficult to maintain.

#### Signature

```python
@property
def cartouche(self, pq="q") -> Text: ...
```

### Point().child_of

[Show source in Point.py:474](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L474)

Check if a Point is the child (direct descendent of other).

#### Arguments

- `other` *Point* - The Point to check against.

#### Returns

- `bool` - True if this Point is the child of other, False otherwise.

#### Signature

```python
def child_of(self, other): ...
```

### Point().cousin_of

[Show source in Point.py:485](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L485)

Check if two Points are cousins.

Two Points are considered cousins if they have the same parent.
A Point is not considered cousins with itself.

#### Arguments

- `other` *Point* - The Point to compare with.

#### Returns

- `bool` - True if the Points are cousins, False otherwise.

#### Signature

```python
def cousin_of(self, other) -> bool: ...
```

### Point.from_hex

[Show source in Point.py:107](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L107)

Attempts to parse a hexadecimal string to a Point.

#### Arguments

- `h` *str* - The hexadecimal string to parse.

#### Returns

- `Any` - A Point object.

#### Raises

- `InvalidPatpError` - If the hexadecimal string does not correspond to a valid @p.

#### Signature

```python
@classmethod
def from_hex(cls, h: str) -> Any: ...
```

### Point.from_num

[Show source in Point.py:125](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L125)

Attempts to parse an integer or thousands-delimited integer string to a Point.

#### Arguments

i (int | str): The integer or thousands-delimited integer string to parse.

#### Returns

- `Any` - A Point object.

#### Raises

- `ValueError` - If the input cannot be interpreted as an integer.
- `InvalidPatpError` - If the integer does not correspond to a valid @p.

#### Signature

```python
@classmethod
def from_num(cls, i: int | str) -> Any: ...
```

### Point.from_patq

[Show source in Point.py:149](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L149)

Attempts to parse a patq (@q) string to a Point.

#### Arguments

- `h` *str* - The patq string to parse.

#### Returns

- `Any` - A Point object.

#### Raises

- `InvalidPatpError` - If the patq string does not correspond to a valid @p.

#### Signature

```python
@classmethod
def from_patq(cls, h: str) -> Any: ...
```

### Point().galaxy

[Show source in Point.py:382](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L382)

Report parent galaxy if it exists.

#### Returns

Any | None: The parent galaxy object if it exists, None otherwise.

#### Signature

```python
@property
def galaxy(self) -> Any | None: ...
```

### Point().grandparent

[Show source in Point.py:327](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L327)

Returns the grandparent of the point.

#### Returns

Any | None: The grandparent of the point, or None if the point doesn't have a grandparent.

#### Notes

Comets do not have grandparents.

#### Signature

```python
@property
def grandparent(self) -> Any | None: ...
```

### Point().greatgrandparent

[Show source in Point.py:312](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L312)

Returns the great grandparent of the point.

#### Returns

Any | None: The great grandparent of the point, or None if the point doesn't have a great grandparent.

#### Notes

Only moons have great grandparents.

#### Signature

```python
@property
def greatgrandparent(self) -> Any | None: ...
```

### Point().index

[Show source in Point.py:248](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L248)

Represents the Point in integer format.

#### Returns

- `int` - The Point in integer format.

#### Notes

Provided by urbit-ob.

#### Signature

```python
@computed_field
@property
def index(self) -> int: ...
```

### Point().index_delimited

[Show source in Point.py:261](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L261)

Represents the Point in integer format with thousands dot delimiters.

#### Returns

- `str` - The Point in integer format with thousands dot delimiters.

#### Signature

```python
@computed_field
@property
def index_delimited(self) -> str: ...
```

### Point().index_hex

[Show source in Point.py:274](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L274)

Represents the Point in hexadecimal format.

#### Returns

- `str` - The Point in hexadecimal format.

#### Notes

Provided by urbit-ob.

#### Signature

```python
@computed_field
@property
def index_hex(self) -> str: ...
```

### Point().parent

[Show source in Point.py:342](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L342)

Returns the parent of the point.

#### Returns

Any | None: The parent of the point, or None if the point doesn't have a parent (galaxies don't have parents).

#### Signature

```python
@property
def parent(self) -> Any | None: ...
```

### Point().parent_of

[Show source in Point.py:463](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L463)

Check if a Point is the parent (direct ancestor of other).

#### Arguments

- `other` *Point* - The Point to check against.

#### Returns

- `bool` - True if this Point is the parent of other, False otherwise.

#### Signature

```python
def parent_of(self, other): ...
```

### Point().patp_indices

[Show source in Point.py:217](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L217)

Returns the syllable indices for the @p format.

#### Returns

- `list[int]` - A list of syllable indices for @p format.

#### Signature

```python
@property
def patp_indices(self) -> list[int]: ...
```

### Point().patp_syllables

[Show source in Point.py:185](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L185)

Returns the syllables for the @p format.

#### Returns

- `list[str]` - A list of syllables in @p format.

#### Signature

```python
@property
def patp_syllables(self) -> list[str]: ...
```

### Point().patq

[Show source in Point.py:235](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L235)

Represents the Point in @q format, which is a syllabic un-obfusated form.

#### Returns

- `str` - The Point in @q format.

#### Notes

Provided by urbit-ob.

#### Signature

```python
@computed_field
@property
def patq(self) -> str: ...
```

### Point().patq_indices

[Show source in Point.py:226](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L226)

Returns the syllable indices for the @q format.

#### Returns

- `list[int]` - A list of syllable indices for @q format.

#### Signature

```python
@property
def patq_indices(self) -> list[int]: ...
```

### Point().patq_syllables

[Show source in Point.py:194](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L194)

Returns the syllables for the @q format.

#### Returns

- `list[str]` - A list of syllables in @q format.

#### Signature

```python
@property
def patq_syllables(self) -> list[str]: ...
```

### Point().planet

[Show source in Point.py:406](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L406)

Report parent planet if it exists.

#### Returns

Any | None: The parent planet object if it exists, None otherwise.

#### Signature

```python
@property
def planet(self) -> Any | None: ...
```

### Point().rank

[Show source in Point.py:287](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L287)

Returns the Rank of the point.

#### Returns

- `Rank` - The Rank of the point.

#### Signature

```python
@computed_field
@property
def rank(self) -> Rank: ...
```

### Point().related

[Show source in Point.py:434](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L434)

Check if a Point is related to another.

No point is related to itself. If two non-comets (PAWNs) are related they
will share an ancestor galaxy. All comets (PAWNs) are related to one another.
We don't consider comets (PAWNs) to be related to any non-comets except for ~zod.

#### Arguments

- `other` *Point* - The Point to check against.

#### Returns

- `bool` - True if this Point is related to other, False otherwise.

#### Signature

```python
def related(self, other): ...
```

### Point().root

[Show source in Point.py:297](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L297)

Returns the root (highest ranked ancestor) of a Point.

#### Returns

- `Any` - The root Point object.

#### Notes

The root of a galaxy is itself.

#### Signature

```python
@property
def root(self) -> Any: ...
```

### Point().sibling_of

[Show source in Point.py:505](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L505)

Check if two Points are siblings.

Two Points are considered siblings if they have the same parent.
A Point is not considered siblings with itself.

#### Arguments

- `other` *Point* - The Point to compare with.

#### Returns

- `bool` - True if the Points are siblings, False otherwise.

#### Signature

```python
def sibling_of(self, other) -> bool: ...
```

### Point().star

[Show source in Point.py:394](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L394)

Report parent star if it exists.

#### Returns

Any | None: The parent star object if it exists, None otherwise.

#### Signature

```python
@property
def star(self) -> Any | None: ...
```

### Point().syllable_indices

[Show source in Point.py:203](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L203)

Calculates the syllable indices for the given form.

#### Arguments

- `form` *Form* - The form to calculate syllable indices for.

#### Returns

- `list[int]` - A list of syllable indices.

#### Signature

```python
def syllable_indices(self, form: Form) -> list[int]: ...
```

#### See also

- [Form](#form)

### Point().syllables

[Show source in Point.py:167](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L167)

Retrieves syllables for the given form (patp or patq).

#### Arguments

- `form` *Form* - The form to retrieve syllables for.

#### Returns

- `list[str]` - A list of syllables.

#### Raises

- `KeyError` - If the provided form is not supported.

#### Signature

```python
def syllables(self, form: Form) -> list[str]: ...
```

#### See also

- [Form](#form)



## ValidPatp

[Show source in Point.py:36](https://github.com/litmus-ritten/slurpy/blob/main/src/Point.py#L36)

Validate a @p string.

This function validates a @p string by removing hyphens and whitespace,
splitting it into syllables, and confirming that it has the correct number
of syllables and follows the correct pattern of alternating syllables. This
function is slightly stricter than the urbit-ob check, as it also confirms
that the @p string has the appropriate hyphenation pattern.

#### Arguments

- `patp` *str* - The @p string to validate.

#### Returns

- `str` - The original @p string if valid.

#### Raises

- `InvalidPatpError` - If the @p string is invalid.

#### Signature

```python
def ValidPatp(patp: str): ...
```