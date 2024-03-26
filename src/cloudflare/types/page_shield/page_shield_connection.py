# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PageShieldConnection"]


class PageShieldConnection(BaseModel):
    id: Optional[str] = None

    added_at: Optional[str] = None

    domain_reported_malicious: Optional[bool] = None

    first_page_url: Optional[str] = None

    first_seen_at: Optional[str] = None

    host: Optional[str] = None

    last_seen_at: Optional[str] = None

    page_urls: Optional[List[str]] = None

    url: Optional[str] = None

    url_contains_cdn_cgi_path: Optional[bool] = None
