# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["CookieListParams"]


class CookieListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """The direction used to sort returned cookies.'"""

    domain: str
    """Filters the returned cookies that match the specified domain attribute"""

    export: Literal["csv"]
    """Export the list of cookies as a file.

    Cannot be used with per_page or page options.
    """

    hosts: str
    """
    Includes cookies that match one or more URL-encoded hostnames separated by
    commas.

    Wildcards are supported at the start and end of each hostname to support starts
    with, ends with and contains. If no wildcards are used, results will be filtered
    by exact match
    """

    http_only: bool
    """Filters the returned cookies that are set with HttpOnly"""

    name: str
    """
    Filters the returned cookies that match the specified name. Wildcards are
    supported at the start and end to support starts with, ends with and contains.
    e.g. session\\**
    """

    order_by: Literal["first_seen_at", "last_seen_at"]
    """The field used to sort returned cookies."""

    page: str
    """The current page number of the paginated results."""

    page_url: str
    """
    Includes connections that match one or more page URLs (separated by commas)
    where they were last seen

    Wildcards are supported at the start and end of each page URL to support starts
    with, ends with and contains. If no wildcards are used, results will be filtered
    by exact match
    """

    path: str
    """Filters the returned cookies that match the specified path attribute"""

    per_page: float
    """The number of results per page."""

    same_site: Literal["lax", "strict", "none"]
    """Filters the returned cookies that match the specified same_site attribute"""

    secure: bool
    """Filters the returned cookies that are set with Secure"""

    type: Literal["first_party", "unknown"]
    """Filters the returned cookies that match the specified type attribute"""
