# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceMoveParams"]


class InstanceMoveParams(TypedDict, total=False):
    account_id: Required[str]

    namespace: Required[str]
    """Current namespace of the instance."""

    new_namespace: Required[str]
    """Target namespace to move the instance into."""
