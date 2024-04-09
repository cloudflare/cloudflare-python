# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .allowed_headersh import AllowedHeadersh
from .allowed_methodsh import AllowedMethodsh
from .allowed_originsh import AllowedOriginsh

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

    allowed_headers: List[AllowedHeadersh]
    """Allowed HTTP request headers."""

    allowed_methods: List[AllowedMethodsh]
    """Allowed HTTP request methods."""

    allowed_origins: List[AllowedOriginsh]
    """Allowed origins."""

    max_age: float
    """The maximum number of seconds the results of a preflight request can be cached."""
