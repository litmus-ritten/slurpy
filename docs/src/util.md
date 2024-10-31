# Util

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Util

> Auto-generated documentation for [src.util](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py) module.

- [Util](#util)
  - [format_time](#format_time)
  - [fragment_syllables](#fragment_syllables)
  - [render_element](#render_element)
  - [rgb_to_hex](#rgb_to_hex)
  - [tlonts2dt](#tlonts2dt)
  - [unix2da](#unix2da)
  - [urbitdate](#urbitdate)
  - [urbts2datetime](#urbts2datetime)

## format_time

[Show source in util.py:80](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L80)

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

[Show source in util.py:164](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L164)

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

[Show source in util.py:93](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L93)

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

[Show source in util.py:148](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L148)

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

[Show source in util.py:67](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L67)

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

[Show source in util.py:14](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L14)

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

[Show source in util.py:46](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L46)

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

[Show source in util.py:30](https://github.com/litmus-ritten/slurpy/blob/main/src/util.py#L30)

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