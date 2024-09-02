# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Script"]


class Script(BaseModel):
    id: str
    """Identifier"""

    added_at: datetime

    first_seen_at: datetime

    host: str

    last_seen_at: datetime

    url: str

    url_contains_cdn_cgi_path: bool

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

    malicious_domain_categories: Optional[List[str]] = None

    malicious_url_categories: Optional[List[str]] = None

    obfuscation_score: Optional[int] = None
    """The obfuscation score of the JavaScript content."""

    page_urls: Optional[List[str]] = None

    url_reported_malicious: Optional[bool] = None
