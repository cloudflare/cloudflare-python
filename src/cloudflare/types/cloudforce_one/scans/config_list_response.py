# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["ConfigListResponse"]


class ConfigListResponse(BaseModel):
    account_id: str

    frequency: float

    ips: List[str]
