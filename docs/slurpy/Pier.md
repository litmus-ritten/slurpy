# Pier

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Pier

> Auto-generated documentation for [slurpy.Pier](../../slurpy/Pier.py) module.

- [Pier](#pier)
  - [Pier](#pier-1)
    - [Pier()._block_insecure](#pier()_block_insecure)
    - [Pier().attach_client](#pier()attach_client)
    - [Pier().connect](#pier()connect)
    - [Pier().cookie_dict](#pier()cookie_dict)
    - [Pier().get_hostpoint](#pier()get_hostpoint)
    - [Pier().groups_recency](#pier()groups_recency)
    - [Pier().logged_in](#pier()logged_in)
    - [Pier().login_url](#pier()login_url)
    - [Pier.reacquire](#pierreacquire)
    - [Pier().update_groups](#pier()update_groups)
    - [Pier().update_groups_pattern](#pier()update_groups_pattern)
  - [main](#main)

## Pier

[Show source in Pier.py:36](../../slurpy/Pier.py#L36)

Representation of a running Urbit.

#### Signature

```python
class Pier(BaseModel): ...
```

### Pier()._block_insecure

[Show source in Pier.py:69](../../slurpy/Pier.py#L69)

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

### Pier().attach_client

[Show source in Pier.py:203](../../slurpy/Pier.py#L203)

Attaches a client and authentication code to the Pier instance.

#### Arguments

- `client` - The client instance to attach.
- [code](#pier) *str* - The authentication code to use.

#### Signature

```python
def attach_client(self, client, code: str) -> None: ...
```

### Pier().connect

[Show source in Pier.py:52](../../slurpy/Pier.py#L52)

#### Signature

```python
async def connect(self): ...
```

### Pier().cookie_dict

[Show source in Pier.py:137](../../slurpy/Pier.py#L137)

Returns the cookie as a dictionary.

#### Returns

- `Union[dict,` *None]* - Dictionary containing cookie key-value pair,
    or None if no cookie is set.

#### Signature

```python
@property
def cookie_dict(self) -> Union[dict, None]: ...
```

### Pier().get_hostpoint

[Show source in Pier.py:100](../../slurpy/Pier.py#L100)

Get the Azimuth Point associated with a running Pier.

The Point is extracted from the login page.

#### Returns

- `Point` - The Azimuth Point associated with the Pier.

#### Raises

- `requests.RequestException` - If there's an error fetching the login page.
- `IndexError` - If the Point cannot be extracted from the login page.

#### Signature

```python
async def get_hostpoint(self) -> Point: ...
```

### Pier().groups_recency

[Show source in Pier.py:194](../../slurpy/Pier.py#L194)

Calculates the time elapsed since groups were last updated.

#### Returns

- `datetime.timedelta` - The duration since the last groups update.

#### Signature

```python
@property
def groups_recency(self) -> datetime.timedelta: ...
```

### Pier().logged_in

[Show source in Pier.py:128](../../slurpy/Pier.py#L128)

Returns whether the client is logged in.

#### Returns

- `bool` - True if client has a valid cookie, False otherwise.

#### Signature

```python
@property
def logged_in(self) -> bool: ...
```

### Pier().login_url

[Show source in Pier.py:89](../../slurpy/Pier.py#L89)

Get the URL for the login page of an Urbit Pier.

#### Returns

- `Url` - The login URL for the Urbit Pier.

#### Signature

```python
@computed_field
@property
def login_url(self) -> Url: ...
```

### Pier.reacquire

[Show source in Pier.py:213](../../slurpy/Pier.py#L213)

Reacquires a Pier instance from JSON data.

#### Arguments

- `json_data` *str* - JSON string containing serialized Pier data.
- `args` - Arguments object containing optional host override.

#### Returns

- [Pier](#pier) - A new Pier instance populated with the provided data.

#### Notes

If args.host is provided and differs from the cached host,
the specified host will be used instead of the cached one.

#### Signature

```python
@classmethod
def reacquire(cls, json_data: str, args) -> "Pier": ...
```

### Pier().update_groups

[Show source in Pier.py:151](../../slurpy/Pier.py#L151)

Updates all groups by calling update_groups_pattern with no pattern.

#### Returns

- `Dict[str,` *Group]* - Dictionary mapping group names to Group objects.

#### Signature

```python
async def update_groups(self) -> Dict[str, Group]: ...
```

### Pier().update_groups_pattern

[Show source in Pier.py:159](../../slurpy/Pier.py#L159)

Updates the groups dictionary by fetching from the scry endpoint and filtering by pattern.

#### Arguments

- `pattern` - A regex pattern string to filter group names, or None to include all groups.

#### Returns

- `Dict[str,` *Group]* - A dictionary mapping group names to Group objects that match the pattern.

#### Raises

- `aiohttp.ClientError` - If there is an error fetching the groups data.
- `re.error` - If the provided pattern is an invalid regex pattern.

#### Signature

```python
async def update_groups_pattern(self, pattern: Union[str, None]) -> Dict[str, Group]: ...
```



## main

[Show source in Pier.py:235](../../slurpy/Pier.py#L235)

#### Signature

```python
async def main(): ...
```