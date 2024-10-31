# Post

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Post

> Auto-generated documentation for [src.Post](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py) module.

- [Post](#post)
  - [Post](#post-1)
    - [Post().__ge__](#post()__ge__)
    - [Post().__gt__](#post()__gt__)
    - [Post().__hash__](#post()__hash__)
    - [Post().__le__](#post()__le__)
    - [Post().__lt__](#post()__lt__)
    - [Post.from_dict](#postfrom_dict)

## Post

[Show source in Post.py:16](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py#L16)

Representation of a any Tlon rich text post, i.e. a Chat message, Heap post, or Diary post.

#### Attributes

- `index` *int* - The unique identifier of the post.
- `author` *Point* - The author of the post.
- `sent` *datetime.datetime* - The timestamp when the post was sent.
- `title` *str* - The title of the post.
image (Url | None): The URL of the associated image, if any.
- `content` *list* - The content of the post.

#### Signature

```python
class Post(BaseModel):
    def __init__(self, **kwargs) -> None: ...
```

### Post().__ge__

[Show source in Post.py:111](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py#L111)

Compare if this Post is greater than or equal to another Post.

#### Arguments

- `other` *Post* - Another Post instance to compare with.

#### Returns

- `bool` - True if this Post's index is greater than or equal to the other Post's index, False otherwise.

#### Signature

```python
def __ge__(self, other: "Post") -> bool: ...
```

### Post().__gt__

[Show source in Post.py:87](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py#L87)

Compare if this Post is greater than another Post.

#### Arguments

- `other` *Post* - Another Post instance to compare with.

#### Returns

- `bool` - True if this Post's index is greater than the other Post's index, False otherwise.

#### Signature

```python
def __gt__(self, other: "Post") -> bool: ...
```

### Post().__hash__

[Show source in Post.py:66](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py#L66)

Compute the hash value for the Post instance.

#### Returns

- `int` - The hash value based on the Post's index.

#### Signature

```python
def __hash__(self) -> int: ...
```

### Post().__le__

[Show source in Post.py:99](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py#L99)

Compare if this Post is less than or equal to another Post.

#### Arguments

- `other` *Post* - Another Post instance to compare with.

#### Returns

- `bool` - True if this Post's index is less than or equal to the other Post's index, False otherwise.

#### Signature

```python
def __le__(self, other: "Post") -> bool: ...
```

### Post().__lt__

[Show source in Post.py:75](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py#L75)

Compare if this Post is less than another Post.

#### Arguments

- `other` *Post* - Another Post instance to compare with.

#### Returns

- `bool` - True if this Post's index is less than the other Post's index, False otherwise.

#### Signature

```python
def __lt__(self, other: "Post") -> bool: ...
```

### Post.from_dict

[Show source in Post.py:45](https://github.com/litmus-ritten/slurpy/blob/main/src/Post.py#L45)

Create a Post instance from a dictionary.

#### Arguments

- `d` *dict* - A dictionary containing post data.

#### Returns

- [Post](#post) - A new Post instance created from the dictionary data.

#### Signature

```python
@classmethod
def from_dict(cls, d: dict) -> "Post": ...
```