# Client

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Client

> Auto-generated documentation for [slurpy.Client](../../slurpy/Client.py) module.

- [Client](#client)
  - [Client](#client-1)
    - [Client.close](#clientclose)
    - [Client.get_session](#clientget_session)

## Client

[Show source in Client.py:10](../../slurpy/Client.py#L10)

A singleton HTTP client session manager.

This class manages a single aiohttp ClientSession instance and its associated cookie jar.

#### Attributes

- `_instance` *Optional[aiohttp.ClientSession]* - The singleton client session instance.
- `_cookiejar` *CookieJar* - Cookie storage for the session.

#### Signature

```python
class Client: ...
```

### Client.close

[Show source in Client.py:40](../../slurpy/Client.py#L40)

Closes the current client session if it exists and is open.

This method should be called when the session is no longer needed to properly
clean up resources.

#### Signature

```python
@classmethod
async def close(cls): ...
```

### Client.get_session

[Show source in Client.py:23](../../slurpy/Client.py#L23)

Creates or returns an existing aiohttp ClientSession instance.

#### Arguments

- `cookies` *dict, optional* - Dictionary of cookies to initialize or update the session with.
    Defaults to empty dict.

#### Returns

- `aiohttp.ClientSession` - The singleton client session instance.

#### Signature

```python
@classmethod
async def get_session(cls, cookies: dict = {}) -> aiohttp.ClientSession: ...
```