# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["Pattern"]


class Pattern(BaseModel):
    regex: str

    validation: Optional[Literal["luhn"]] = None
