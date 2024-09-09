# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    content: str
    """Content of message"""
