# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    request_identifier: Required[str]
    """UUID"""

    content: str
    """Content of message"""
