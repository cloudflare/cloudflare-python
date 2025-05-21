# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RegistrationBulkDeleteParams"]


class RegistrationBulkDeleteParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[List[str]]
    """A list of registration IDs to delete."""
