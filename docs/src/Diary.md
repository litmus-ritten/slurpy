# Diary

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Diary

> Auto-generated documentation for [src.Diary](https://github.com/litmus-ritten/slurpy/blob/main/src/Diary.py) module.

- [Diary](#diary)
  - [Diary](#diary-1)
    - [Diary.from_dict](#diaryfrom_dict)
  - [Notes](#notes)
    - [Notes.from_dict](#notesfrom_dict)

## Diary

[Show source in Diary.py:47](https://github.com/litmus-ritten/slurpy/blob/main/src/Diary.py#L47)

Representation of a Tlon diary (Notebook) containing zero or more Notes.

#### Attributes

- `posts` *Notes* - Collection of Notes in the diary.
- `total_records` *int* - Total number of records in the diary.
index_newer (int | None): Index of newer records, if available.
index_older (int | None): Index of older records, if available.

#### Signature

```python
class Diary(Channel):
    def __init__(self, **kwargs): ...
```

### Diary.from_dict

[Show source in Diary.py:66](https://github.com/litmus-ritten/slurpy/blob/main/src/Diary.py#L66)

Create a Diary instance from a dictionary.

#### Arguments

- `d` *dict* - Dictionary containing diary data.

#### Returns

- [Diary](#diary) - A new Diary instance.

#### Signature

```python
@classmethod
def from_dict(cls, d: dict) -> "Diary": ...
```



## Notes

[Show source in Diary.py:16](https://github.com/litmus-ritten/slurpy/blob/main/src/Diary.py#L16)

A collection of Note objects.

#### Attributes

- `contents` *List[Note]* - A list of Note objects.

#### Signature

```python
class Notes(BaseModel):
    def __init__(self, **kwargs): ...
```

### Notes.from_dict

[Show source in Diary.py:33](https://github.com/litmus-ritten/slurpy/blob/main/src/Diary.py#L33)

Create a Notes object from a dictionary.

#### Arguments

- `d` *dict* - A dictionary containing Note objects.

#### Returns

- [Notes](#notes) - A new Notes object.

#### Signature

```python
@classmethod
def from_dict(cls, d: dict) -> "Notes": ...
```