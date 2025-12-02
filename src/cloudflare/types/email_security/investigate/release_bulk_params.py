# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ReleaseBulkParams"]


class ReleaseBulkParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    body: Required[SequenceNotStr[str]]
    """A list of messages identfied by their `postfix_id`s that should be released."""
