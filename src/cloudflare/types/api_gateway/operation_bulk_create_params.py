# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationBulkCreateParams", "Body"]


class OperationBulkCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    endpoint: Required[str]
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: Required[str]
    """RFC3986-compliant host."""

    method: Required[Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]]
    """The HTTP method used to access the endpoint."""
