# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HTTPConfiguration"]


class HTTPConfiguration(BaseModel):
    allow_insecure: Optional[bool] = None
    """Do not validate the certificate when the health check uses HTTPS."""

    expected_body: Optional[str] = None
    """A case-insensitive sub-string to look for in the response body.

    If this string is not found, the origin will be marked as unhealthy.
    """

    expected_codes: Optional[List[str]] = None
    """The expected HTTP response codes (e.g.

    "200") or code ranges (e.g. "2xx" for all codes starting with 2) of the health
    check.
    """

    follow_redirects: Optional[bool] = None
    """Follow redirects if the origin returns a 3xx status code."""

    header: Optional[Dict[str, List[str]]] = None
    """The HTTP request headers to send in the health check.

    It is recommended you set a Host header by default. The User-Agent header cannot
    be overridden.
    """

    method: Optional[Literal["GET", "HEAD"]] = None
    """The HTTP method to use for the health check."""

    path: Optional[str] = None
    """The endpoint path to health check against."""

    port: Optional[int] = None
    """Port number to connect to for the health check.

    Defaults to 80 if type is HTTP or 443 if type is HTTPS.
    """
