# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ScriptGetResponse", "Version"]


class Version(BaseModel):
    cryptomining_score: Optional[int] = None
    """The cryptomining score of the JavaScript content."""

    dataflow_score: Optional[int] = None
    """The dataflow score of the JavaScript content."""

    fetched_at: Optional[str] = None
    """The timestamp of when the script was last fetched."""

    hash: Optional[str] = None
    """The computed hash of the analyzed script."""

    js_integrity_score: Optional[int] = None
    """The integrity score of the JavaScript content."""

    magecart_score: Optional[int] = None
    """The magecart score of the JavaScript content."""

    malware_score: Optional[int] = None
    """The malware score of the JavaScript content."""

    obfuscation_score: Optional[int] = None
    """The obfuscation score of the JavaScript content."""


class ScriptGetResponse(BaseModel):
    id: str
    """Identifier"""

    added_at: datetime

    first_seen_at: datetime

    host: str

    last_seen_at: datetime

    url: str

    url_contains_cdn_cgi_path: bool

    cryptomining_score: Optional[int] = None
    """The cryptomining score of the JavaScript content."""

    dataflow_score: Optional[int] = None
    """The dataflow score of the JavaScript content."""

    domain_reported_malicious: Optional[bool] = None

    fetched_at: Optional[str] = None
    """The timestamp of when the script was last fetched."""

    first_page_url: Optional[str] = None

    hash: Optional[str] = None
    """The computed hash of the analyzed script."""

    js_integrity_score: Optional[int] = None
    """The integrity score of the JavaScript content."""

    magecart_score: Optional[int] = None
    """The magecart score of the JavaScript content."""

    malicious_domain_categories: Optional[List[str]] = None

    malicious_url_categories: Optional[List[str]] = None

    malware_score: Optional[int] = None
    """The malware score of the JavaScript content."""

    obfuscation_score: Optional[int] = None
    """The obfuscation score of the JavaScript content."""

    page_urls: Optional[List[str]] = None

    url_reported_malicious: Optional[bool] = None

    versions: Optional[List[Version]] = None
