# Chat

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Chat

> Auto-generated documentation for [src.Chat](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py) module.

- [Chat](#chat)
  - [Chat](#chat-1)
    - [Chat.from_dict](#chatfrom_dict)
  - [Post](#post)
    - [Post.from_dict](#postfrom_dict)
    - [Post().tile](#post()tile)
  - [Posts](#posts)
    - [Posts.from_dict](#postsfrom_dict)

## Chat

[Show source in Chat.py:97](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py#L97)

docstring for Chat

#### Signature

```python
class Chat(BaseModel):
    def __init__(self, **kwargs): ...
```

### Chat.from_dict

[Show source in Chat.py:108](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py#L108)

#### Signature

```python
@classmethod
def from_dict(cls, d: dict): ...
```



## Post

[Show source in Chat.py:15](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py#L15)

#### Signature

```python
class Post(BaseModel):
    def __init__(self, **kwargs): ...
```

### Post.from_dict

[Show source in Chat.py:46](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py#L46)

We don't need the key as this information is stored in the seal.

#### Signature

```python
@classmethod
def from_dict(cls, v: dict): ...
```

### Post().tile

[Show source in Chat.py:73](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py#L73)

#### Signature

```python
@property
def tile(self): ...
```



## Posts

[Show source in Chat.py:83](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py#L83)

docstring for Posts

#### Signature

```python
class Posts(BaseModel):
    def __init__(self, **kwargs): ...
```

### Posts.from_dict

[Show source in Chat.py:91](https://github.com/litmus-ritten/slurpy/blob/main/src/Chat.py#L91)

#### Signature

```python
@classmethod
def from_dict(cls, d: dict): ...
```