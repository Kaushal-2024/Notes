
# 🚀 Pydantic Core Cheat Sheet (v2)

A quick reference for Pydantic v2 features — focused on validation, serialization, and modern Python typing.

---

## 📌 What is Pydantic?
Pydantic is a data-validation library that:
- Uses Python type hints for validation
- Automatically converts data types
- Ensures safe and structured input/output for backend systems

Used widely in:
- FastAPI
- Microservices
- ETL/Data pipelines
- Messaging systems

---

## ⚡ Key Engine: `pydantic-core`
- Rust-based validation and serialization engine
- 2–10x faster than Pydantic v1
- Enables high performance API and backend systems

---

## 🧱 Base Components

### `BaseModel`
The core class for data models.
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
````

### `BaseSettings`

Validates **environment variables** (best for `.env` config)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
```

---

## 🔍 Field Validation

### `Field()`

Add constraints and metadata.

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    price: float = Field(gt=0)
```

### `field_validator`

Validate **specific fields** (replaces `@validator`)

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    def no_space(cls, v):
        if " " in v:
            raise ValueError("Spaces not allowed")
        return v.lower()
```

---

## 🧠 Model-Level Validation

### `model_validator`

Used when field values depend on each other.

```python
from pydantic import BaseModel, model_validator

class DateRange(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")
    def check_range(self):
        if self.start > self.end:
            raise ValueError("start must <= end")
        return self
```

---

## 🧊 Serialization & Parsing (v2 changes)

| Use Case                | v1             | v2                  |
| ----------------------- | -------------- | ------------------- |
| Serialize model to dict | `.dict()`      | `.model_dump()`     |
| Validate/parse input    | `.parse_obj()` | `.model_validate()` |

Examples:

```python
user_dict = user.model_dump()
user = User.model_validate({"name": "Kaushal", "age": "23"})
```

---

## 🧩 Mapping JSON Keys

### Field `alias`

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    full_name: str = Field(alias="fullName")
```

Incoming JSON:

```json
{"fullName": "Kaushal Tarpara"}
```

---

## 🛢️ ORM/Database Support

### `from_attributes`

Replacement for `orm_mode=True`

```python
class User(BaseModel):
    model_config = {"from_attributes": True}
```

---

## 📦 Root Types

### `RootModel`

Used when a model wraps a single value.

```python
from pydantic import RootModel

IntList = RootModel[list[int]]
items = IntList([1, 2, 3])
```

---

## 🔄 Dataclasses

Lightweight models with validation support.

```python
from pydantic.dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
```

---

## 🛑 FastAPI-Specific: `response_model`

Not a Pydantic concept — used in FastAPI for output validation.

```python
@app.get("/user", response_model=User)
```

---

# ⚔️ Pydantic v1 vs v2 Summary

| Feature           | v1               | v2                      |
| ----------------- | ---------------- | ----------------------- |
| Validation engine | Python           | Rust (pydantic-core) 🚀 |
| Field validators  | `@validator`     | `@field_validator`      |
| Model validation  | `root_validator` | `@model_validator`      |
| Serialization     | `.dict()`        | `.model_dump()`         |
| Parsing           | `.parse_x`       | `.model_validate()`     |
| ORM Mode          | `orm_mode=True`  | `from_attributes=True`  |
| Speed             | Good             | **Much faster**         |
| Typing            | Less strict      | Fully typed             |

---

## 🧠 Best Practices

* Keep models small & reusable
* Use enums instead of free-form strings
* Validate complex business logic using `model_validator`
* Use `BaseSettings` for config instead of manual `.env` parsing

---
