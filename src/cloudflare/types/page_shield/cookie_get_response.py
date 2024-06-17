# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CookieGetResponse"]


class CookieGetResponse(BaseModel):
    id: str
    """Identifier"""

    first_seen_at: datetime

    host: str

    last_seen_at: datetime

    name: str

    type: Literal["first_party", "unknown"]

    domain_attribute: Optional[str] = None

    expires_attribute: Optional[datetime] = None

    http_only_attribute: Optional[bool] = None

    max_age_attribute: Optional[int] = None

    page_urls: Optional[List[str]] = None

    path_attribute: Optional[str] = None

    same_site_attribute: Optional[Literal["lax", "strict", "none"]] = None

    secure_attribute: Optional[bool] = None
