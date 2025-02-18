# Util

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Util

> Auto-generated documentation for [slurpy.util](../../slurpy/util.py) module.

- [Util](#util)
  - [condense_postid](#condense_postid)
  - [da2datetime](#da2datetime)
  - [delimit_postid](#delimit_postid)
  - [format_time](#format_time)
  - [fragment_syllables](#fragment_syllables)
  - [render_element](#render_element)
  - [rgb_to_hex](#rgb_to_hex)
  - [tlonts2dt](#tlonts2dt)
  - [unix2da](#unix2da)
  - [urbitdate](#urbitdate)
  - [urbts2datetime](#urbts2datetime)

## condense_postid

[Show source in util.py:201](../../slurpy/util.py#L201)

Removes all dots from a string.

#### Arguments

- `s` - Input string containing dots to be removed.

#### Returns

- `str` - String with all dots removed.

#### Examples

```python
>>> condense_postid("123.456.789")
"123456789"
```

#### Signature

```python
def condense_postid(s: str) -> str: ...
```



## da2datetime

[Show source in util.py:30](../../slurpy/util.py#L30)

#### Signature

```python
def da2datetime(time: int) -> datetime.datetime: ...
```



## delimit_postid

[Show source in util.py:185](../../slurpy/util.py#L185)

Formats a string by inserting dots every 3 characters.

#### Arguments

- `s` - Input string to be delimited.

#### Returns

- `str` - Delimited string with dots inserted every 3 characters.

#### Examples

```python
>>> delimit_postid("123456789")
"123.456.789"
```

#### Signature

```python
def delimit_postid(s: str) -> str: ...
```



## format_time

[Show source in util.py:85](../../slurpy/util.py#L85)

Format datetime for terminal display.

#### Arguments

- `dt` *datetime.datetime* - Datetime object to be formatted.

#### Returns

- `str` - Formatted datetime string in the format "YYYY-MM-DD HH:MM".

#### Signature

```python
def format_time(dt: datetime.datetime) -> str: ...
```



## fragment_syllables

[Show source in util.py:169](../../slurpy/util.py#L169)

Fragments a string into a list of 3-character substrings.

#### Arguments

- `s` *str* - A string to be fragmented.

#### Returns

- `list[str]` - A list of 3-character substrings.

#### Raises

- `ValueError` - If the input string is empty.

#### Signature

```python
def fragment_syllables(s: str) -> list[str]: ...
```



## render_element

[Show source in util.py:98](../../slurpy/util.py#L98)

Recursively render a dict encoding Tlon rich text to a string which can be parsed by Rich.

#### Arguments

d (Union[str, Dict[str, Any]]): The input element to render, either a string or a dictionary.

#### Returns

- `str` - The rendered string that can be parsed by Rich.

#### Raises

- `ValueError` - If an unsupported element type is encountered.

#### Examples

```python
>>> render_element("Hello")
'Hello'
>>> render_element({"italics": "Hello"})
'[italic]Hello[/italic]'
>>> render_element({"bold": {"italics": "Hello"}})
'[bold][italic]Hello[/italic][/bold]'
```

#### Signature

```python
def render_element(d: Union[str, Dict[str, Any]]) -> str: ...
```



## rgb_to_hex

[Show source in util.py:153](../../slurpy/util.py#L153)

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



## tlonts2dt

[Show source in util.py:72](../../slurpy/util.py#L72)

Convert Tlon timestamp into datetime object.

#### Arguments

t (str | int): Tlon timestamp in milliseconds past Unix epoch.

#### Returns

- `datetime.datetime` - Converted datetime object.

#### Signature

```python
def tlonts2dt(t: str | int) -> datetime.datetime: ...
```



## unix2da

[Show source in util.py:14](../../slurpy/util.py#L14)

Convert unix time to urbit time.

#### Arguments

- `time` *int* - Unix timestamp in seconds.

#### Returns

- `str` - Urbit time as a string.

#### Raises

- `ValueError` - If the input time is negative or too large.

#### Signature

```python
def unix2da(time: int) -> str: ...
```



## urbitdate

[Show source in util.py:51](../../slurpy/util.py#L51)

Convert Urbit date string to datetime object.

#### Arguments

- `d` *str* - Urbit date string in the format "/YYYY.MM.DD..HH.MM.SS".

#### Returns

- `datetime.datetime` - Datetime object representing the Urbit date.

#### Raises

- `ValueError` - If the input string is not in the correct format.

#### Signature

```python
def urbitdate(d: str) -> datetime.datetime: ...
```



## urbts2datetime

[Show source in util.py:35](../../slurpy/util.py#L35)

Convert urbit time to datetime.

#### Arguments

- `urbts` *int* - Urbit timestamp in milliseconds.

#### Returns

- `datetime.datetime` - Datetime object representing the Urbit time.

#### Raises

- `ValueError` - If the input urbts is negative or too large.

#### Signature

```python
def urbts2datetime(urbts: int) -> datetime.datetime: ...
```