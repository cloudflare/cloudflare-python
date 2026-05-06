# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SpendingLimitGetResponse", "Config"]


class Config(BaseModel):
    amount: Optional[float] = None

    duration: Optional[str] = None

    strategy: Optional[str] = None


class SpendingLimitGetResponse(BaseModel):
    config: Config

    enabled: bool
