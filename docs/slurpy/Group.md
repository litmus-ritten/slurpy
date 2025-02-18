# Group

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Group

> Auto-generated documentation for [slurpy.Group](../../slurpy/Group.py) module.

- [Group](#group)
  - [Group](#group-1)
    - [Group.from_key](#groupfrom_key)
    - [Group().normalised_title](#group()normalised_title)
    - [Group().tile](#group()tile)
    - [Group().update](#group()update)

## Group

[Show source in Group.py:23](../../slurpy/Group.py#L23)

Tlon Group, i.e. a community consisting of one or more Channels and one or more Subscribers.

#### Attributes

- `path` *str* - Address of group, forming stem of scry path.
- `host` *Point* - Ship hosting the Group.
- `secret` *bool* - Whether the group is publicly enumerable.
image (Color | Url | None): Group sidebar avatar.
- `title` *str* - Group name.
cover (Color | Url | None): Sidebar hero image.
- `description` *str* - Group description which pops up in search/join dialogs.
- `cabals` *list[Cabal]* - List of logical subscriber groups.
- `channels` *list[Channel]* - List of chats, diaries, heaps, etc.
- `cordon` *Cordon* - Banned ships and ranks (for a public group) or invited/asking ships (for a private group).
- `fleet` *Fleet* - Subscribers.

#### Signature

```python
class Group(BaseModel): ...
```

### Group.from_key

[Show source in Group.py:55](../../slurpy/Group.py#L55)

Parse a group from a key/value pair.

#### Arguments

- `k` *str* - The key.
- `d` *dict* - The dictionary containing group data.

#### Returns

- [Group](#group) - A new Group instance.

#### Signature

```python
@classmethod
async def from_key(cls, k: str, d: dict, pier_host: Point) -> "Group": ...
```

### Group().normalised_title

[Show source in Group.py:110](../../slurpy/Group.py#L110)

#### Signature

```python
@property
def normalised_title(self) -> str: ...
```

### Group().tile

[Show source in Group.py:97](../../slurpy/Group.py#L97)

#### Signature

```python
@property
def tile(self) -> Text: ...
```

### Group().update

[Show source in Group.py:117](../../slurpy/Group.py#L117)

#### Signature

```python
async def update(self, hush: bool = False, echo_messages=False) -> None: ...
```