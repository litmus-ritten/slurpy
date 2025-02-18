# Point

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Point

> Auto-generated documentation for [slurpy.Point](../../slurpy/Point.py) module.

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
  - [frag](#frag)
  - [rgb_to_hex](#rgb_to_hex)

## Form

[Show source in Point.py:35](../../slurpy/Point.py#L35)

#### Signature

```python
class Form(Enum): ...
```



## Point

[Show source in Point.py:137](../../slurpy/Point.py#L137)

Represents a point in the Urbit network.

#### Attributes

- `patp` *str* - The @p address of the point.

#### Signature

```python
class Point(BaseModel): ...
```

### Point().__ge__

[Show source in Point.py:603](../../slurpy/Point.py#L603)

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

[Show source in Point.py:592](../../slurpy/Point.py#L592)

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

[Show source in Point.py:562](../../slurpy/Point.py#L562)

Computes the hash value for the Point.

#### Returns

- `int` - The hash value of the string representation of the Point.

#### Signature

```python
def __hash__(self): ...
```

### Point().__le__

[Show source in Point.py:581](../../slurpy/Point.py#L581)

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

[Show source in Point.py:570](../../slurpy/Point.py#L570)

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

[Show source in Point.py:554](../../slurpy/Point.py#L554)

Returns a string representation of the Point.

#### Returns

- `str` - A string containing the rank glyph and patp of the Point.

#### Signature

```python
def __str__(self) -> str: ...
```

### Point().ancestors

[Show source in Point.py:451](../../slurpy/Point.py#L451)

Evaluate the chain of ancestors of a Point through recursive tree ascent.

#### Returns

- `List[Any]` - A list of the ancestors of a Point in ascending order.

#### Signature

```python
@property
def ancestors(self) -> list[Any]: ...
```

### Point().ancestors_patp_dict

[Show source in Point.py:397](../../slurpy/Point.py#L397)

Returns the ancestor list of a Point as a dictionary.

#### Returns

- `dict` - The ancestor list of the Point as a dictionary where the keys are non-null relations.

#### Signature

```python
@property
def ancestors_patp_dict(self) -> dict: ...
```

### Point().ancestors_patp_list

[Show source in Point.py:388](../../slurpy/Point.py#L388)

Returns the ancestor list of a Point in ascending order of @ps.

#### Returns

- `List[str]` - The ancestor list of the Point in ascending order of @ps.

#### Signature

```python
@property
def ancestors_patp_list(self) -> list[str]: ...
```

### Point().cartouche

[Show source in Point.py:614](../../slurpy/Point.py#L614)

TODO: refactor

#### Signature

```python
@property
def cartouche(self, pq="q") -> Text: ...
```

### Point().child_of

[Show source in Point.py:507](../../slurpy/Point.py#L507)

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

[Show source in Point.py:518](../../slurpy/Point.py#L518)

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

[Show source in Point.py:146](../../slurpy/Point.py#L146)

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

[Show source in Point.py:164](../../slurpy/Point.py#L164)

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

[Show source in Point.py:188](../../slurpy/Point.py#L188)

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

[Show source in Point.py:415](../../slurpy/Point.py#L415)

Report parent galaxy if it exists.

#### Returns

Any | None: The parent galaxy object if it exists, None otherwise.

#### Signature

```python
@property
def galaxy(self) -> Any | None: ...
```

### Point().grandparent

[Show source in Point.py:361](../../slurpy/Point.py#L361)

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

[Show source in Point.py:346](../../slurpy/Point.py#L346)

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

[Show source in Point.py:286](../../slurpy/Point.py#L286)

Represents the Point in integer format.

#### Returns

- `int` - The Point in integer format.

#### Notes

Provided by urbit-ob.

#### Signature

```python
@property
def index(self) -> int: ...
```

### Point().index_delimited

[Show source in Point.py:298](../../slurpy/Point.py#L298)

Represents the Point in integer format with thousands dot delimiters.

#### Returns

- `str` - The Point in integer format with thousands dot delimiters.

#### Signature

```python
@property
def index_delimited(self) -> str: ...
```

### Point().index_hex

[Show source in Point.py:310](../../slurpy/Point.py#L310)

Represents the Point in hexadecimal format.

#### Returns

- `str` - The Point in hexadecimal format.

#### Notes

Provided by urbit-ob.

#### Signature

```python
@property
def index_hex(self) -> str: ...
```

### Point().parent

[Show source in Point.py:376](../../slurpy/Point.py#L376)

Returns the parent of the point.

#### Returns

Any | None: The parent of the point, or None if the point doesn't have a parent (galaxies don't have parents).

#### Signature

```python
@property
def parent(self) -> Any | None: ...
```

### Point().parent_of

[Show source in Point.py:496](../../slurpy/Point.py#L496)

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

[Show source in Point.py:256](../../slurpy/Point.py#L256)

Returns the syllable indices for the @p format.

#### Returns

- `list[int]` - A list of syllable indices for @p format.

#### Signature

```python
@property
def patp_indices(self) -> list[int]: ...
```

### Point().patp_syllables

[Show source in Point.py:224](../../slurpy/Point.py#L224)

Returns the syllables for the @p format.

#### Returns

- `list[str]` - A list of syllables in @p format.

#### Signature

```python
@property
def patp_syllables(self) -> list[str]: ...
```

### Point().patq

[Show source in Point.py:274](../../slurpy/Point.py#L274)

Represents the Point in @q format, which is a syllabic un-obfusated form.

#### Returns

- `str` - The Point in @q format.

#### Notes

Provided by urbit-ob.

#### Signature

```python
@property
def patq(self) -> str: ...
```

### Point().patq_indices

[Show source in Point.py:265](../../slurpy/Point.py#L265)

Returns the syllable indices for the @q format.

#### Returns

- `list[int]` - A list of syllable indices for @q format.

#### Signature

```python
@property
def patq_indices(self) -> list[int]: ...
```

### Point().patq_syllables

[Show source in Point.py:233](../../slurpy/Point.py#L233)

Returns the syllables for the @q format.

#### Returns

- `list[str]` - A list of syllables in @q format.

#### Signature

```python
@property
def patq_syllables(self) -> list[str]: ...
```

### Point().planet

[Show source in Point.py:439](../../slurpy/Point.py#L439)

Report parent planet if it exists.

#### Returns

Any | None: The parent planet object if it exists, None otherwise.

#### Signature

```python
@property
def planet(self) -> Any | None: ...
```

### Point().rank

[Show source in Point.py:322](../../slurpy/Point.py#L322)

Returns the Rank of the point.

#### Returns

- `Rank` - The Rank of the point.

#### Signature

```python
@property
def rank(self) -> Rank: ...
```

### Point().related

[Show source in Point.py:467](../../slurpy/Point.py#L467)

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

[Show source in Point.py:331](../../slurpy/Point.py#L331)

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

[Show source in Point.py:538](../../slurpy/Point.py#L538)

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

[Show source in Point.py:427](../../slurpy/Point.py#L427)

Report parent star if it exists.

#### Returns

Any | None: The parent star object if it exists, None otherwise.

#### Signature

```python
@property
def star(self) -> Any | None: ...
```

### Point().syllable_indices

[Show source in Point.py:242](../../slurpy/Point.py#L242)

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

[Show source in Point.py:206](../../slurpy/Point.py#L206)

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

[Show source in Point.py:75](../../slurpy/Point.py#L75)

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



## frag

[Show source in Point.py:56](../../slurpy/Point.py#L56)

Fragments a string into a list of 3-character substrings.

#### Arguments

- `s` *str* - A string to be fragmented.

#### Returns

- `list[str]` - A list of 3-character substrings.

#### Raises

- `ValueError` - If the input string is empty.

#### Signature

```python
def frag(s: str) -> list[str]: ...
```



## rgb_to_hex

[Show source in Point.py:40](../../slurpy/Point.py#L40)

Converts RGB color values to hexadecimal color code.

#### Arguments

t (tuple[float, float, float]): A tuple of three float values representing RGB colors.
    Each value should be between 0 and 1.

#### Returns

- `str` - A string representing the hexadecimal color code.

#### Raises

- `ValueError` - If the input tuple contains values outside the range [0, 1].

#### Signature

```python
def rgb_to_hex(t: tuple[float, float, float]) -> str: ...
```