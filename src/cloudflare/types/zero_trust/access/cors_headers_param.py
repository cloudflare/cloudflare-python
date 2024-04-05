# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .allowed_headers_item import AllowedHeadersItem
from .allowed_methods_item import AllowedMethodsItem
from .allowed_origins_item import AllowedOriginsItem

__all__ = ["CorsHeadersParam"]


class CorsHeadersParam(TypedDict, total=False):
    allow_all_headers: bool
    """Allows all HTTP request headers."""

    allow_all_methods: bool
    """Allows all HTTP request methods."""

    allow_all_origins: bool
    """Allows all origins."""

    allow_credentials: bool
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: List[AllowedHeadersItem]
    """Allowed HTTP request headers."""

    allowed_methods: List[AllowedMethodsItem]
    """Allowed HTTP request methods."""

    allowed_origins: List[AllowedOriginsItem]
    """Allowed origins."""

    max_age: float
    """The maximum number of seconds the results of a preflight request can be cached."""
