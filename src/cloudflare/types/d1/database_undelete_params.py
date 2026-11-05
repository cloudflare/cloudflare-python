# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatabaseUndeleteParams"]


class DatabaseUndeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    new_name: str
    """
    Restore the database with this name instead of the name it had when it was
    deleted. Required if another database in the account already uses that name.
    """
