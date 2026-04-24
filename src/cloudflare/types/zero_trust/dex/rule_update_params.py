# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    description: str

    match: str
    """The wirefilter expression to match."""

    name: str
    """The name of the Rule."""
