# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .allowed_headers import AllowedHeaders
from .allowed_origins import AllowedOrigins
from .allowed_http_methods import AllowedHTTPMethods

__all__ = ["CORSHeaders"]


class CORSHeaders(BaseModel):
    allow_all_headers: Optional[bool] = None
    """Allows all HTTP request headers."""

    allow_all_methods: Optional[bool] = None
    """Allows all HTTP request methods."""

    allow_all_origins: Optional[bool] = None
    """Allows all origins."""

    allow_credentials: Optional[bool] = None
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: Optional[List[AllowedHeaders]] = None
    """Allowed HTTP request headers."""

    allowed_methods: Optional[AllowedHTTPMethods] = None
    """Allowed HTTP request methods."""

    allowed_origins: Optional[List[AllowedOrigins]] = None
    """Allowed origins."""

    max_age: Optional[float] = None
    """The maximum number of seconds the results of a preflight request can be cached."""
