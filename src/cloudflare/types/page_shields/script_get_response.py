# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ScriptGetResponse", "Version"]


class Version(BaseModel):
    fetched_at: Optional[str] = None
    """The timestamp of when the script was last fetched."""

    hash: Optional[str] = None
    """The computed hash of the analyzed script."""

    js_integrity_score: Optional[int] = None
    """The integrity score of the JavaScript content."""


class ScriptGetResponse(BaseModel):
    id: Optional[object] = None

    added_at: Optional[object] = None

    domain_reported_malicious: Optional[object] = None

    fetched_at: Optional[object] = None

    first_page_url: Optional[object] = None

    first_seen_at: Optional[object] = None

    hash: Optional[object] = None

    host: Optional[object] = None

    js_integrity_score: Optional[object] = None

    last_seen_at: Optional[object] = None

    page_urls: Optional[object] = None

    url: Optional[object] = None

    url_contains_cdn_cgi_path: Optional[object] = None

    versions: Optional[List[Version]] = None
