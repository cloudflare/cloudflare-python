# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["InstanceArchiveParams"]


class InstanceArchiveParams(TypedDict, total=False):
    account_id: Required[str]

    check_instances: Required[SequenceNotStr[str]]
    """A list of finding instance IDs to pass along."""
