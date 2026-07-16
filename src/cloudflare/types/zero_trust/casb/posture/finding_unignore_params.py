# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["FindingUnignoreParams"]


class FindingUnignoreParams(TypedDict, total=False):
    account_id: Required[str]

    checks: Required[SequenceNotStr[str]]
    """A list of finding IDs to pass along."""
