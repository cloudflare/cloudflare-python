# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ScriptGetResponse", "Version"]


class Version(BaseModel):
    dataflow_score: Optional[int] = None
    """The dataflow score of the JavaScript content."""

    fetched_at: Optional[str] = None
    """The timestamp of when the script was last fetched."""

    hash: Optional[str] = None
    """The computed hash of the analyzed script."""

    js_integrity_score: Optional[int] = None
    """The integrity score of the JavaScript content."""

    obfuscation_score: Optional[int] = None
    """The obfuscation score of the JavaScript content."""


class ScriptGetResponse(BaseModel):
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

    versions: Optional[List[Version]] = None
