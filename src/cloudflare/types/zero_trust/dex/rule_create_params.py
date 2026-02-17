# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    account_id: Required[str]

    match: Required[str]
    """The wirefilter expression to match."""

    name: Required[str]
    """The name of the Rule."""

    description: str
