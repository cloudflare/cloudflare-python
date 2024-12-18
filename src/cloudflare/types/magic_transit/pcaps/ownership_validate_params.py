# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OwnershipValidateParams"]


class OwnershipValidateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    destination_conf: Required[str]
    """The full URI for the bucket. This field only applies to `full` packet captures."""

    ownership_challenge: Required[str]
    """The ownership challenge filename stored in the bucket."""
