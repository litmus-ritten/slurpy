# Slurpyexceptions

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Slurpyexceptions

> Auto-generated documentation for [src.SlurpyExceptions](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py) module.

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
  - [UnknownChannelTypeError](#unknownchanneltypeerror)
    - [UnknownChannelTypeError().message](#unknownchanneltypeerror()message)

## InsecureError

[Show source in SlurpyExceptions.py:128](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L128)

Exception raised when an insecure condition is entered.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class InsecureError(Exception):
    def __init__(self, message: str): ...
```

### InsecureError().message

[Show source in SlurpyExceptions.py:140](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L140)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## InvalidPatpError

[Show source in SlurpyExceptions.py:32](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L32)

Exception raised when the Patp of a Point is invalid.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class InvalidPatpError(Exception):
    def __init__(self, message: str): ...
```

### InvalidPatpError().message

[Show source in SlurpyExceptions.py:44](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L44)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## InvalidRankError

[Show source in SlurpyExceptions.py:8](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L8)

Exception raised when the Rank of a Point is invalid.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class InvalidRankError(Exception):
    def __init__(self, message: str): ...
```

### InvalidRankError().message

[Show source in SlurpyExceptions.py:20](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L20)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## LoginError

[Show source in SlurpyExceptions.py:104](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L104)

Exception raised when an Urbit login fails.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class LoginError(Exception):
    def __init__(self, message: str): ...
```

### LoginError().message

[Show source in SlurpyExceptions.py:116](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L116)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## MalformedCodeError

[Show source in SlurpyExceptions.py:80](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L80)

Exception raised when a login code is of the incorrect shape.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class MalformedCodeError(Exception):
    def __init__(self, message: str): ...
```

### MalformedCodeError().message

[Show source in SlurpyExceptions.py:92](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L92)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```



## UnknownChannelTypeError

[Show source in SlurpyExceptions.py:56](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L56)

Exception raised when the type of a Channel is invalid.

#### Attributes

- `message` *str* - The error message.

#### Signature

```python
class UnknownChannelTypeError(Exception):
    def __init__(self, message: str): ...
```

### UnknownChannelTypeError().message

[Show source in SlurpyExceptions.py:68](https://github.com/litmus-ritten/slurpy/blob/main/src/SlurpyExceptions.py#L68)

str: The error message.

#### Signature

```python
@property
def message(self) -> str: ...
```