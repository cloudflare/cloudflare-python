# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["HTTPConfigurationParam"]


class HTTPConfigurationParam(TypedDict, total=False):
    allow_insecure: bool
    """Do not validate the certificate when the health check uses HTTPS."""

    expected_body: str
    """A case-insensitive sub-string to look for in the response body.

    If this string is not found, the origin will be marked as unhealthy.
    """

    expected_codes: Optional[List[str]]
    """The expected HTTP response codes (e.g.

    "200") or code ranges (e.g. "2xx" for all codes starting with 2) of the health
    check.
    """

    follow_redirects: bool
    """Follow redirects if the origin returns a 3xx status code."""

    header: Optional[Dict[str, List[str]]]
    """The HTTP request headers to send in the health check.

    It is recommended you set a Host header by default. The User-Agent header cannot
    be overridden.
    """

    method: Literal["GET", "HEAD"]
    """The HTTP method to use for the health check."""

    path: str
    """The endpoint path to health check against."""

    port: int
    """Port number to connect to for the health check.

    Defaults to 80 if type is HTTP or 443 if type is HTTPS.
    """
