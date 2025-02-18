# Channel

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Channel

> Auto-generated documentation for [slurpy.Channel](../../slurpy/Channel.py) module.

- [Channel](#channel)
  - [Channel](#channel-1)
    - [Channel().append_content](#channel()append_content)
    - [Channel.from_dict](#channelfrom_dict)
    - [Channel().pull_channel](#channel()pull_channel)
    - [Channel().scry_path](#channel()scry_path)
    - [Channel().tile](#channel()tile)
    - [Channel().update_channel](#channel()update_channel)

## Channel

[Show source in Channel.py:39](../../slurpy/Channel.py#L39)

A Tlon group channel

#### Attributes

- `name` *str* - The name of the channel.
- `chantype` *str* - The type of the channel.
- `join` *bool* - Whether the channel is joinable.
- `added` *datetime.datetime* - The date and time when the channel was added.
- `readers` *List[str]* - List of cabal names which can read the channel.
- `zone` *str* - The zone of the channel.
- `image` *Optional[Url]* - The image URL of the channel, if any.
- `title` *str* - The title of the channel.
- `cover` *Color|Url* - The cover color or url of the channel.
- `description` *str* - The description of the channel.

#### Signature

```python
class Channel(BaseModel): ...
```

### Channel().append_content

[Show source in Channel.py:73](../../slurpy/Channel.py#L73)

#### Signature

```python
def append_content(self, c: Chat) -> None: ...
```

### Channel.from_dict

[Show source in Channel.py:88](../../slurpy/Channel.py#L88)

Create a Channel instance from a dictionary.

#### Arguments

- `k` *str* - The key representing the channel.
d (Dict[str, Any]): The dictionary containing channel data.

#### Returns

- [Channel](#channel) - A new Channel instance.

#### Signature

```python
@classmethod
async def from_dict(cls, k: str, d: Dict[str, dict], pier_host: Point) -> "Channel": ...
```

### Channel().pull_channel

[Show source in Channel.py:132](../../slurpy/Channel.py#L132)

#### Signature

```python
async def pull_channel(self): ...
```

### Channel().scry_path

[Show source in Channel.py:199](../../slurpy/Channel.py#L199)

#### Signature

```python
def scry_path(self) -> str: ...
```

### Channel().tile

[Show source in Channel.py:76](../../slurpy/Channel.py#L76)

A tile representing the Channel for pretty-printing in a CLI/TUI context.

#### Signature

```python
@property
def tile(self) -> text.Text: ...
```

### Channel().update_channel

[Show source in Channel.py:157](../../slurpy/Channel.py#L157)

#### Signature

```python
async def update_channel(self, hush=False, echo_messages=False): ...
```