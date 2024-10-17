# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScanListParams"]


class ScanListParams(TypedDict, total=False):
    account_scans: bool
    """Return only scans created by account."""

    asn: str
    """
    Filter scans by Autonomous System Number (ASN) of _any_ request made by the
    webpage.
    """

    date_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter scans requested before date (inclusive)."""

    date_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter scans requested after date (inclusive)."""

    hash: str
    """Filter scans by hash of any html/js/css request made by the webpage."""

    hostname: str
    """Filter scans by hostname of _any_ request made by the webpage."""

    ip: str
    """Filter scans by IP address (IPv4 or IPv6) of _any_ request made by the webpage."""

    is_malicious: bool
    """Filter scans by malicious verdict."""

    limit: int
    """Limit the number of objects in the response."""

    next_cursor: str
    """Pagination cursor to get the next set of results."""

    page_asn: str
    """Filter scans by main page Autonomous System Number (ASN)."""

    page_hostname: str
    """Filter scans by main page hostname (domain of effective URL)."""

    page_ip: str
    """Filter scans by main page IP address (IPv4 or IPv6)."""

    page_path: str
    """
    Filter scans by exact match of effective URL path (also supports suffix search).
    """

    page_url: str
    """Filter scans by submitted or scanned URL"""

    path: str
    """Filter scans by url path of _any_ request made by the webpage."""

    scan_id: Annotated[str, PropertyInfo(alias="scanId")]
    """Scan uuid"""

    url: str
    """Filter scans by URL of _any_ request made by the webpage"""
