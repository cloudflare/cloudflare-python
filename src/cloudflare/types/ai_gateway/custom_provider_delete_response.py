# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CustomProviderDeleteResponse"]


class CustomProviderDeleteResponse(BaseModel):
    id: str

    base_url: str

    created_at: datetime

    modified_at: datetime

    name: str

    slug: str

    beta: Optional[bool] = None

    curl_example: Optional[str] = None

    description: Optional[str] = None

    enable: Optional[bool] = None

    headers: Optional[str] = None

    js_example: Optional[str] = None

    link: Optional[str] = None

    logo: Optional[str] = None

    position: Optional[int] = None
