# Chat

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Chat

> Auto-generated documentation for [slurpy.Chat](../../slurpy/Chat.py) module.

- [Chat](#chat)
  - [Chat](#chat-1)
    - [Chat.from_dict](#chatfrom_dict)
    - [Chat.from_empty](#chatfrom_empty)
  - [Post](#post)
    - [Post.from_dict](#postfrom_dict)
    - [Post().tile](#post()tile)
  - [Posts](#posts)
    - [Posts.from_dict](#postsfrom_dict)

## Chat

[Show source in Chat.py:97](../../slurpy/Chat.py#L97)

docstring for Chat

#### Signature

```python
class Chat(BaseModel): ...
```

### Chat.from_dict

[Show source in Chat.py:105](../../slurpy/Chat.py#L105)

#### Signature

```python
@classmethod
def from_dict(cls, d: dict): ...
```

### Chat.from_empty

[Show source in Chat.py:113](../../slurpy/Chat.py#L113)

#### Signature

```python
@classmethod
def from_empty(cls): ...
```



## Post

[Show source in Chat.py:14](../../slurpy/Chat.py#L14)

#### Signature

```python
class Post(BaseModel): ...
```

### Post.from_dict

[Show source in Chat.py:42](../../slurpy/Chat.py#L42)

We don't need the key as this information is stored in the seal.

#### Signature

```python
@classmethod
def from_dict(cls, v: dict): ...
```

### Post().tile

[Show source in Chat.py:69](../../slurpy/Chat.py#L69)

#### Signature

```python
@property
def tile(self): ...
```



## Posts

[Show source in Chat.py:83](../../slurpy/Chat.py#L83)

docstring for Posts

#### Signature

```python
class Posts(BaseModel):
    def __init__(self, **kwargs): ...
```

### Posts.from_dict

[Show source in Chat.py:91](../../slurpy/Chat.py#L91)

#### Signature

```python
@classmethod
def from_dict(cls, d: dict): ...
```