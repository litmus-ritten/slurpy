# Group

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Group

> Auto-generated documentation for [src.Group](https://github.com/litmus-ritten/slurpy/blob/main/src/Group.py) module.

- [Group](#group)
  - [Group](#group-1)
    - [Group.from_key](#groupfrom_key)

## Group

[Show source in Group.py:21](https://github.com/litmus-ritten/slurpy/blob/main/src/Group.py#L21)

Tlon Group, i.e. a community consisting of one or more Channels and one or more Subscribers.

#### Attributes

- `path` *str* - Address of group, forming stem of scry path.
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
class Group(BaseModel):
    def __init__(self, **kwarg): ...
```

### Group.from_key

[Show source in Group.py:51](https://github.com/litmus-ritten/slurpy/blob/main/src/Group.py#L51)

Parse a group from a key/value pair.

#### Arguments

- `k` *str* - The key.
- `d` *dict* - The dictionary containing group data.

#### Returns

- [Group](#group) - A new Group instance.

#### Signature

```python
@classmethod
def from_key(cls, k: str, d: dict) -> "Group": ...
```