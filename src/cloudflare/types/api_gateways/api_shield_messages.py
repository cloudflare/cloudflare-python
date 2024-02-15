# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["APIShieldMessages", "APIShieldMessageItem"]


class APIShieldMessageItem(BaseModel):
    code: int

    message: str


APIShieldMessages = List[APIShieldMessageItem]
