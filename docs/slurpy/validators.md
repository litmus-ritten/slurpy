# Validators

[Slurpy Index](../README.md#slurpy-index) / [Slurpy](./index.md#slurpy) / Validators

> Auto-generated documentation for [slurpy.validators](../../slurpy/validators.py) module.

- [Validators](#validators)
  - [valid_code](#valid_code)
  - [valid_cover](#valid_cover)

## valid_code

[Show source in validators.py:20](../../slurpy/validators.py#L20)

Pydantic BeforeValidator for an Urbit login code.

This validator checks if the input string consists of valid prefix-suffix pairs.
TODO: It should be refactored into a hierarchical validator for Urbit syllables.

#### Arguments

- `v` *str* - The input string to validate.

#### Returns

- `str` - The validated and lowercase input string.

#### Raises

- `MalformedCodeError` - If the input string is malformed or contains invalid syllables.

#### Signature

```python
def valid_code(v: str) -> str: ...
```



## valid_cover

[Show source in validators.py:49](../../slurpy/validators.py#L49)

Pydantic BeforeValidator for a cover, which can be a Color, Url, or empty.

#### Arguments

- `v` *str* - The input value to validate.

#### Returns

Color | Url | None: A Color object if the input is a valid color,
    a Url object if the input is a valid URL, or None if the input is empty.

#### Raises

- `ValidationError` - If the input is neither a valid color nor a valid URL.

#### Signature

```python
def valid_cover(v: Union[str, None]) -> Color | Url | None: ...
```