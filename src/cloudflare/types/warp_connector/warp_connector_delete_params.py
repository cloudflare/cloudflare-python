# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WARPConnectorDeleteParams"]


class WARPConnectorDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    body: Required[object]
