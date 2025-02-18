# Slurpyexceptions

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Slurpyexceptions

> Auto-generated documentation for [slurpy.SlurpyExceptions](../../slurpy/SlurpyExceptions.py) module.

- [Slurpyexceptions](#slurpyexceptions)
  - [InsecureError](#insecureerror)
    - [InsecureError().message](#insecureerror()message)
  - [InvalidPatpError](#invalidpatperror)
    - [InvalidPatpError().message](#invalidpatperror()message)
  - [InvalidRankError](#invalidrankerror)
    - [InvalidRankError().message](#invalidrankerror()message)
  - [LoginError](#loginerror)
    - [LoginError().message](#loginerror()message)
  - [MalformedCodeError](#malformedcodeerror)
    - [MalformedCodeError().message](#malformedcodeerror()message)
  - [UnexpectedMarkError](#unexpectedmarkerror)
    - [UnexpectedMarkError().message](#unexpectedmarkerror()message)
  - [UnknownChannelTypeError](#unknownchanneltypeerror)
    - [UnknownChannelTypeError().message](#unknownchanneltypeerror()message)

## InsecureError

[Show source in SlurpyExceptions.py:152](../../slurpy/SlurpyExceptions.py#L152)

Exception raised when an insecure condition is entered.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class InsecureError(Exception):
    def __init__(self, message: str): ...
```

### InsecureError().message

[Show source in SlurpyExceptions.py:164](../../slurpy/SlurpyExceptions.py#L164)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## InvalidPatpError

[Show source in SlurpyExceptions.py:32](../../slurpy/SlurpyExceptions.py#L32)

Exception raised when the Patp of a Point is invalid.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class InvalidPatpError(Exception):
    def __init__(self, message: str): ...
```

### InvalidPatpError().message

[Show source in SlurpyExceptions.py:44](../../slurpy/SlurpyExceptions.py#L44)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## InvalidRankError

[Show source in SlurpyExceptions.py:8](../../slurpy/SlurpyExceptions.py#L8)

Exception raised when the Rank of a Point is invalid.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class InvalidRankError(Exception):
    def __init__(self, message: str): ...
```

### InvalidRankError().message

[Show source in SlurpyExceptions.py:20](../../slurpy/SlurpyExceptions.py#L20)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## LoginError

[Show source in SlurpyExceptions.py:128](../../slurpy/SlurpyExceptions.py#L128)

Exception raised when an Urbit login fails.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class LoginError(Exception):
    def __init__(self, message: str): ...
```

### LoginError().message

[Show source in SlurpyExceptions.py:140](../../slurpy/SlurpyExceptions.py#L140)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## MalformedCodeError

[Show source in SlurpyExceptions.py:80](../../slurpy/SlurpyExceptions.py#L80)

Exception raised when a login code is of the incorrect shape.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class MalformedCodeError(Exception):
    def __init__(self, message: str): ...
```

### MalformedCodeError().message

[Show source in SlurpyExceptions.py:92](../../slurpy/SlurpyExceptions.py#L92)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## UnexpectedMarkError

[Show source in SlurpyExceptions.py:104](../../slurpy/SlurpyExceptions.py#L104)

Exception raised when a scry result does not have the expected mark.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class UnexpectedMarkError(Exception):
    def __init__(self, message: str): ...
```

### UnexpectedMarkError().message

[Show source in SlurpyExceptions.py:116](../../slurpy/SlurpyExceptions.py#L116)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## UnknownChannelTypeError

[Show source in SlurpyExceptions.py:56](../../slurpy/SlurpyExceptions.py#L56)

Exception raised when the type of a Channel is invalid.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class UnknownChannelTypeError(Exception):
    def __init__(self, message: str): ...
```

### UnknownChannelTypeError().message

[Show source in SlurpyExceptions.py:68](../../slurpy/SlurpyExceptions.py#L68)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```