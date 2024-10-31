# Heap

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Heap

> Auto-generated documentation for [src.Heap](https://github.com/litmus-ritten/slurpy/blob/main/src/Heap.py) module.

- [Heap](#heap)
  - [Heap](#heap-1)
    - [Heap.from_dict](#heapfrom_dict)
  - [HeapPost](#heappost)
    - [HeapPost.from_dict](#heappostfrom_dict)
  - [main](#main)

## Heap

[Show source in Heap.py:55](https://github.com/litmus-ritten/slurpy/blob/main/src/Heap.py#L55)

Representation of Tlon Heap, a gallery of user-submitted HeapPosts.

#### Attributes

- `contents` *List[HeapPost]* - A list of HeapPost objects.
- `total` *int* - The total number of posts.
newer_posts (datetime | None): Timestamp of newer posts, if available.
older_posts (datetime | None): Timestamp of older posts, if available.

#### Signature

```python
class Heap(BaseModel):
    def __init__(self, **kwargs) -> None: ...
```

### Heap.from_dict

[Show source in Heap.py:74](https://github.com/litmus-ritten/slurpy/blob/main/src/Heap.py#L74)

Create a Heap instance from a dictionary.

#### Arguments

- `d` *dict* - A dictionary containing Heap data.

#### Returns

- [Heap](#heap) - An instance of Heap.

#### Signature

```python
@classmethod
def from_dict(cls, d: dict) -> "Heap": ...
```



## HeapPost

[Show source in Heap.py:17](https://github.com/litmus-ritten/slurpy/blob/main/src/Heap.py#L17)

Representation of a unitary Heap post.

#### Attributes

- `index` *int* - The unique identifier of the post.
- `author` *Point* - The author of the post.
- `sent` *datetime* - The timestamp when the post was sent.
- `content` *str* - The content of the post.

#### Signature

```python
class HeapPost(BaseModel):
    def __init__(self, **kwargs) -> None: ...
```

### HeapPost.from_dict

[Show source in Heap.py:36](https://github.com/litmus-ritten/slurpy/blob/main/src/Heap.py#L36)

Create a HeapPost instance from a dictionary.

#### Arguments

- `d` *dict* - A dictionary containing post data.

#### Returns

- [HeapPost](#heappost) - An instance of HeapPost.

#### Signature

```python
@classmethod
def from_dict(cls, d: dict) -> "HeapPost": ...
```



## main

[Show source in Heap.py:97](https://github.com/litmus-ritten/slurpy/blob/main/src/Heap.py#L97)

#### Signature

```python
def main(): ...
```