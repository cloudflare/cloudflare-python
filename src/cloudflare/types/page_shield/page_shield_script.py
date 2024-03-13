# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PageShieldScript"]


class PageShieldScript(BaseModel):
    id: Optional[object] = None

    added_at: Optional[object] = None

    dataflow_score: Optional[object] = None

    domain_reported_malicious: Optional[object] = None

    fetched_at: Optional[object] = None

    first_page_url: Optional[object] = None

    first_seen_at: Optional[object] = None

    hash: Optional[object] = None

    host: Optional[object] = None

    js_integrity_score: Optional[object] = None

    last_seen_at: Optional[object] = None

    obfuscation_score: Optional[object] = None

    page_urls: Optional[object] = None

    url: Optional[object] = None

    url_contains_cdn_cgi_path: Optional[object] = None
