# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PreviewCreateParams"]


class PreviewCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    postfix_id: Required[str]
    """The identifier of the message."""
