# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PatternValidateParams"]


class PatternValidateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    regex: Required[str]
    """The regex pattern."""
