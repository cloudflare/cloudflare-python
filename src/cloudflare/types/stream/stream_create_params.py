# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StreamCreateParams"]


class StreamCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    body: Required[object]
