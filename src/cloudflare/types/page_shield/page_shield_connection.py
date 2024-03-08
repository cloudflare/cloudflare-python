# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PageShieldConnection"]


class PageShieldConnection(BaseModel):
    id: Optional[object] = None

    added_at: Optional[object] = None

    domain_reported_malicious: Optional[object] = None

    first_page_url: Optional[object] = None

    first_seen_at: Optional[object] = None

    host: Optional[object] = None

    last_seen_at: Optional[object] = None

    page_urls: Optional[object] = None

    url: Optional[object] = None

    url_contains_cdn_cgi_path: Optional[object] = None
