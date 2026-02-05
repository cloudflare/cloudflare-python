# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from ...._types import SequenceNotStr
from .allowed_headers import AllowedHeaders
from .allowed_methods import AllowedMethods
from .allowed_origins import AllowedOrigins

__all__ = ["CORSHeadersParam"]


class CORSHeadersParam(TypedDict, total=False):
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

    allowed_headers: SequenceNotStr[AllowedHeaders]
    """Allowed HTTP request headers."""

    allowed_methods: List[AllowedMethods]
    """Allowed HTTP request methods."""

    allowed_origins: SequenceNotStr[AllowedOrigins]
    """Allowed origins."""

    max_age: float
    """The maximum number of seconds the results of a preflight request can be cached."""
