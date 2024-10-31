# Channel

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Channel

> Auto-generated documentation for [src.Channel](https://github.com/litmus-ritten/slurpy/blob/main/src/Channel.py) module.

- [Channel](#channel)
  - [Channel](#channel-1)
    - [Channel.from_dict](#channelfrom_dict)
    - [Channel().scry_path](#channel()scry_path)
    - [Channel().tile](#channel()tile)

## Channel

[Show source in Channel.py:25](https://github.com/litmus-ritten/slurpy/blob/main/src/Channel.py#L25)

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
class Channel(BaseModel):
    def __init__(self, **kwargs: Any) -> None: ...
```

### Channel.from_dict

[Show source in Channel.py:77](https://github.com/litmus-ritten/slurpy/blob/main/src/Channel.py#L77)

Create a Channel instance from a dictionary.

#### Arguments

- `k` *str* - The key representing the channel.
d (Dict[str, Any]): The dictionary containing channel data.

#### Returns

- [Channel](#channel) - A new Channel instance.

#### Signature

```python
@classmethod
def from_dict(cls, k: str, d: Dict[str, dict]) -> "Channel": ...
```

### Channel().scry_path

[Show source in Channel.py:115](https://github.com/litmus-ritten/slurpy/blob/main/src/Channel.py#L115)

#### Signature

```python
@computed_field
def scry_path(self) -> str: ...
```

### Channel().tile

[Show source in Channel.py:63](https://github.com/litmus-ritten/slurpy/blob/main/src/Channel.py#L63)

A tile representing the Channel for pretty-printing in a CLI/TUI context.

#### Signature

```python
@property
def tile(self) -> text.Text: ...
```