# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["ConfigCreateResponse"]


class ConfigCreateResponse(BaseModel):
    account_id: str

    frequency: float

    ips: List[str]
