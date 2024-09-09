# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ListListParams"]


class ListListParams(TypedDict, total=False):
    account_id: Required[str]

    type: Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]
    """The type of list."""
