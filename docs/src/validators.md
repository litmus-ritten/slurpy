# Validators

[Slurpy Index](../README.md#slurpy-index) / [Src](./index.md#src) / Validators

> Auto-generated documentation for [src.validators](https://github.com/litmus-ritten/slurpy/blob/main/src/validators.py) module.

- [Validators](#validators)
  - [valid_code](#valid_code)
  - [valid_cover](#valid_cover)

## valid_code

[Show source in validators.py:19](https://github.com/litmus-ritten/slurpy/blob/main/src/validators.py#L19)

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

[Show source in validators.py:48](https://github.com/litmus-ritten/slurpy/blob/main/src/validators.py#L48)

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
def valid_cover(v: str) -> Color | Url | None: ...
```