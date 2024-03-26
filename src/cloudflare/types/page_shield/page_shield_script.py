# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PageShieldScript"]


class PageShieldScript(BaseModel):
    id: Optional[str] = None

    added_at: Optional[str] = None

    dataflow_score: Optional[float] = None

    domain_reported_malicious: Optional[bool] = None

    fetched_at: Optional[str] = None

    first_page_url: Optional[str] = None

    first_seen_at: Optional[str] = None

    hash: Optional[str] = None

    host: Optional[str] = None

    js_integrity_score: Optional[float] = None

    last_seen_at: Optional[str] = None

    obfuscation_score: Optional[float] = None

    page_urls: Optional[List[str]] = None

    url: Optional[str] = None

    url_contains_cdn_cgi_path: Optional[bool] = None
