# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TSIGUpdateParams"]


class TSIGUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    algo: Required[str]
    """TSIG algorithm."""

    name: Required[str]
    """TSIG key name."""

    secret: Required[str]
    """TSIG secret."""
