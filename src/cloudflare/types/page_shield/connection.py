# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Connection"]


class Connection(BaseModel):
    id: str
    """Identifier"""

    added_at: datetime

    first_seen_at: datetime

    host: str

    last_seen_at: datetime

    url: str

    url_contains_cdn_cgi_path: bool

    domain_reported_malicious: Optional[bool] = None

    first_page_url: Optional[str] = None

    malicious_domain_categories: Optional[List[str]] = None

    malicious_url_categories: Optional[List[str]] = None

    page_urls: Optional[List[str]] = None

    url_reported_malicious: Optional[bool] = None
