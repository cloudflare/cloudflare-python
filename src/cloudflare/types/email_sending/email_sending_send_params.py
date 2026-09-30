# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailSendingSendParams", "Body"]


class EmailSendingSendParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of the account."""

    body: Required[Body]


class Body(total=False):
    pass
