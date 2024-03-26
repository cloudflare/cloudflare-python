# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    versions: Optional[List[Version]] = None
