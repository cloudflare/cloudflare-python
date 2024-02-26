# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPGetParams"]


class IPGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    ipv4: str

    ipv6: str
