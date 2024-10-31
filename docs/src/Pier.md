# Pier

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Pier

> Auto-generated documentation for [src.Pier](https://github.com/litmus-ritten/slurpy/blob/main/src/Pier.py) module.

- [Pier](#pier)
  - [Pier](#pier-1)
    - [Pier()._block_insecure](#pier()_block_insecure)
    - [Pier().hostpoint](#pier()hostpoint)
    - [Pier().logged_in](#pier()logged_in)
    - [Pier().login_url](#pier()login_url)
  - [main](#main)

## Pier

[Show source in Pier.py:26](https://github.com/litmus-ritten/slurpy/blob/main/src/Pier.py#L26)

Representation of a running Urbit.

#### Signature

```python
class Pier(BaseModel):
    def __init__(self, **kwargs): ...
```

### Pier()._block_insecure

[Show source in Pier.py:52](https://github.com/litmus-ritten/slurpy/blob/main/src/Pier.py#L52)

Block insecure connections if 'insecure' flag is not set.

This method checks if the connection is using HTTPS. If not, it either
raises an exception or prints a warning based on the 'insecure' flag.

#### Raises

- `InsecureError` - If the connection is not secure (HTTP) and 'insecure'
    mode is not enabled.

#### Returns

None

#### Signature

```python
def _block_insecure(self) -> None: ...
```

### Pier().hostpoint

[Show source in Pier.py:83](https://github.com/litmus-ritten/slurpy/blob/main/src/Pier.py#L83)

Get the Azimuth Point associated with a running Pier.

The Point is extracted from the login page.

#### Returns

- `Point` - The Azimuth Point associated with the Pier.

#### Raises

- `requests.RequestException` - If there's an error fetching the login page.
- `IndexError` - If the Point cannot be extracted from the login page.

#### Signature

```python
@computed_field
@property
def hostpoint(self) -> Point: ...
```

### Pier().logged_in

[Show source in Pier.py:110](https://github.com/litmus-ritten/slurpy/blob/main/src/Pier.py#L110)

#### Signature

```python
@property
def logged_in(self) -> bool: ...
```

### Pier().login_url

[Show source in Pier.py:72](https://github.com/litmus-ritten/slurpy/blob/main/src/Pier.py#L72)

Get the URL for the login page of an Urbit Pier.

#### Returns

- `Url` - The login URL for the Urbit Pier.

#### Signature

```python
@computed_field
@property
def login_url(self) -> Url: ...
```



## main

[Show source in Pier.py:115](https://github.com/litmus-ritten/slurpy/blob/main/src/Pier.py#L115)

#### Signature

```python
def main(): ...
```