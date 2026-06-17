# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenRotateParams"]


class TokenRotateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account identifier."""

    type: Required[Literal["publish_subscribe", "subscribe"]]
    """Which token type to rotate."""
